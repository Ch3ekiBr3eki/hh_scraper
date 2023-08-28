import requests
from bs4 import BeautifulSoup
import lxml
import time
import re
import csv

search_rq = 'data' # тут пишем то, что хотим искать по вакансиям в поиске
area = '1' # тут пишем регион, в котором хотим получить вакансии в поиске. Я ставлю 1, тк это Москва.
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def get_links(text):
    # Отправляем GET-запрос на сайт с указанными параметрами и получаем список вакансий
    res = requests.get(
        f"https://hh.ru/search/vacancy?text={text}&area={area}&page=1",
        headers=headers
    )
    if res.status_code != 200:
        return  # Если запрос не успешен, завершаем функцию
    
    soup = BeautifulSoup(res.content, "lxml")  # Создаем объект BeautifulSoup для парсинга страницы
    try:
        # Ищем количество страниц с вакансиями (для пагинации)
        page_count = int(soup.find("div",attrs={"class":"pager"}).find_all("span",recursive=False)[-1].find("a").find("span").text)
    except:
        return  # Если количество страниц не найдено, завершаем функцию
    
    # Итерируемся по всем страницам с вакансиями
    for page in range(page_count):
        try:
            # Отправляем GET-запрос на каждую страницу и парсим вакансии
            res = requests.get(
                url=f"https://hh.ru/search/vacancy?text={text}&area={area}&page={page}",
                headers=headers
            )
            if res.status_code == 200:
                soup = BeautifulSoup(res.content, "lxml")
                # Итерируемся по всем ссылкам на вакансии на текущей странице
                for a in soup.find_all("a",attrs={"class":"serp-item__title"}):
                    yield f'{a.attrs["href"]}'  # Возвращаем ссылку на вакансию
        except Exception as e:
            print(f"{e}")  # В случае ошибки выводим сообщение
        time.sleep(1)  # Добавляем небольшую задержку между запросами

def get_vacancy(link):
    # Отправляем GET-запрос на страницу вакансии
    data1 = requests.get(
        url=link,
        headers=headers
    )
    if data1.status_code != 200:
        return  # Если запрос не успешен, завершаем функцию
    
    soup = BeautifulSoup(data1.content, "lxml")  # Создаем объект BeautifulSoup для парсинга страницы

    try:
        # Ищем название вакансии
        name = soup.find(attrs={"class":"bloko-header-section-1"}).text
    except:
        name = ""

    try:
        # Ищем текст с информацией о зарплате
        salary_text = soup.find(attrs={"class":"bloko-header-section-2 bloko-header-section-2_lite"}).text
        
        # Убираем неразрывные пробелы и разделяем текст на слова
        words = salary_text.replace(u'\xa0', u'').split()

        # Ищем числа в тексте зарплаты с помощью регулярного выражения
        salary_numbers = re.findall(r'\d+', ' '.join(words))  # Объединяем слова с пробелами

        # Если найдено два числа, это означает диапазон
        if len(salary_numbers) == 2:
            min_salary = salary_numbers[0]
            max_salary = salary_numbers[1]
        else:
            min_salary = max_salary = salary_numbers[0] if salary_numbers else ""

        # Попытаемся найти валюту в тексте (€, $, ₽)
        currency = next((word for word in words if word in ('€', '$', '₽')), "")
    except:
        min_salary = max_salary = currency = ""

    try:
        # Ищем теги вакансии (скиллы)
        tags = [tag.text for tag in soup.find(attrs={"class":"bloko-tag-list"}).find_all("span",attrs={"class":"bloko-tag__section_text"})]
    except:
        tags = []

    try:
        # Ищем опыт, требуемый для вакансии
        exp = soup.find(attrs={"class":"vacancy-description-list-item"}).text
    except:
        exp = ''

    # Создаем словарь с данными о вакансии
    vacancy = {
        "name": name,
        "tags": tags,
        "link": link,
        'experience': exp,
        'lower_salary': min_salary,
        'upper_salary': max_salary,
        'currency': currency
    }
    return vacancy


if __name__ == '__main__':
    links = get_links(search_rq)  # Получаем список ссылок на вакансии
    vacancies = []

    for link in links:
        vacancy_data = get_vacancy(link)  # Получаем данные о вакансии
        vacancies.append(vacancy_data)  # Добавляем данные в список

        # Добавьте паузу перед каждым запросом (если требуется)
        time.sleep(1)

    # Задаем имена полей для CSV
    field_names = ["name", "tags", "link", "experience", "lower_salary", "upper_salary", "currency"]

    # Открываем CSV файл для записи
    with open('vacancies.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()  # Записываем заголовок

        for vacancy in vacancies:
            writer.writerow(vacancy)  # Записываем данные в файл
