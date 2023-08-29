# HH scraper
<p align="center">
      <img src="https://i.ibb.co/yqymhWY/unnamed-pic-32ratio-1200x800-1200x800-80570.jpg" width="236">
</p>

<p align="center">
   <img src="https://img.shields.io/badge/python-blue" alt="python">
   <img src="https://img.shields.io/badge/scraper-violet" alt="kaggle">
   <img src="https://img.shields.io/badge/beautifulsoup-red" alt="bs4"> 
</p>

[HeadHunter Website Link](https://hh.ru/)
## About
I researched what skills are required for junior positions in data analytics, did a data visualization, and drew conclusions that will help me get a job (I hope).
Web scrapper written specifically for the headhunter website that can collect data on your request. In this case I need it for the query "data". With the help of the obtained data I plan to make an extended analysis to understand the market of data specialists, as I myself started actively looking for a job after June 2023.
The project is an automated script for collecting data on vacancies from the popular recruiting portal HeadHunter. With the help of this script you can get information about various vacancies in a certain field (for example, "data") and region (for example, Moscow), as well as descriptions, salaries, required experience and tags for each vacancy.
In addition to this, the results obtained about the vacancies were analyzed, especially those of juniors and junior positions. 

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Я изучил, какие навыки требуются на младших должностях в области анализа данных, сделал визуализацию данных и сделал выводы, которые помогут мне найти работу (я надеюсь).
Веб-скраппер, написанный специально для сайта headhunter, который может собирать данные по вашему запросу. В данном случае он нужен для запроса "data". С помощью полученных данных я планирую провести расширенный анализ, чтобы понять рынок специалистов по работе с данными, так как сам я начал активно искать работу после июня 2023 года.
Проект представляет собой автоматизированный скрипт для сбора данных о вакансиях с популярного рекрутингового портала HeadHunter. С помощью этого скрипта можно получить информацию о различных вакансиях в определенной области (например, "данные") и регионе (например, Москва), а также описание, зарплату, необходимый опыт и теги для каждой вакансии.
Помимо этого был проведён анализ полученных результатов о вакансиях, особенно о вакансиях джунов и младших позиций. 

## Main functions
Collecting links to job vacancies: The script sends GET requests to search engine pages on HeadHunter using specified parameters (e.g. query text and region). It extracts links to various jobs from each page and creates a list of links for further processing.

Extracting job data: For each extracted link, the script goes to the job page and extracts the following data:

- Job title.
- Salary range (if specified) and currency.
- Tags (skills) associated with the vacancy.
- Experience required for the vacancy.
- Link to the vacancy.
- Saving data to a CSV file: The received vacancy data is written to a CSV file named "vacancies.csv". Each row of the file represents a different vacancy and the columns - - contain information about the title, salary, experience and other attributes of the vacancy.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Сбор ссылок на вакансии: Скрипт отправляет GET-запросы на страницы поисковой выдачи на HeadHunter, используя заданные параметры (например, текст запроса и регион). Он извлекает ссылки на различные вакансии с каждой страницы и создает список ссылок для дальнейшей обработки.

Извлечение данных о вакансиях: Для каждой извлеченной ссылки, скрипт переходит на страницу вакансии и извлекает следующие данные:

- Название вакансии.
- Зарплатный диапазон (если указан) и валюта.
- Теги (навыки) связанные с вакансией.
- Опыт, требуемый для вакансии.
- Ссылка на вакансию.
- Сохранение данных в CSV файл: Полученные данные о вакансиях записываются в CSV файл с именем "vacancies.csv". Каждая строка файла представляет отдельную вакансию, а столбцы содержат информацию о названии, зарплате, опыте и других атрибутах вакансии.


## Tech stack
- Python: A programming language for writing a script.
- Requests: A library for sending HTTP requests.
- BeautifulSoup: Library for parsing HTML code of web pages.
- re: A module for working with regular expressions.
- csv: A module for working with CSV files.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
- Python: Язык программирования для написания скрипта.
- requests: Библиотека для отправки HTTP-запросов.
- BeautifulSoup: Библиотека для парсинга HTML-кода веб-страниц.
- re: Модуль для работы с регулярными выражениями.
- csv: Модуль для работы с CSV файлами.

## Project usability  
Automation: The project allows you to automate the process of collecting data on vacancies, which saves time and reduces routine work.
Access to up-to-date information: The script allows you to quickly get up-to-date information about vacancies on HeadHunter.
Adaptability: You can customize search parameters (query text, region) and easily adapt the script to your needs.
Research analysis of the data has led to some interesting results, which can be found in the notebook here in the github or on the kaggle website. the link is at the bottom.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Автоматизация: Проект позволяет автоматизировать процесс сбора данных о вакансиях, что экономит время и уменьшает рутинную работу.
Доступ к актуальной информации: Скрипт позволяет быстро получить актуальную информацию о вакансиях на HeadHunter.
Адаптируемость: Вы можете настроить параметры поиска (текст запроса, регион) и легко адаптировать скрипт под свои потребности.
Анализ полученных данных привел к интересным результатам, с которыми можно ознакомиться в notebook здесь, на github, или на сайте kaggle. ссылка внизу.

## Developers

- [Anton Belyaev]([GitHub Profile Link](https://github.com/Ch3ekiBr3eki))
- [Anton Belyaev]([Kaggle Profile Link](https://www.kaggle.com/antonbelyaevd))
- ([Kaggle Dataset Link](https://www.kaggle.com/datasets/antonbelyaevd/headhunter-vacancies-for-data-search))
- ([Kaggle Notebook Link](https://www.kaggle.com/code/antonbelyaevd/an-introduction-to-headhunter-vacancies))
