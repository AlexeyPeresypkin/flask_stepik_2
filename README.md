# flask_stepik_2

### Описание

Сайт, на котором пользователи могут найти себе репетитора.

### Технологии

Python      
Flask       
SQLAlchemy
PostrgeSQL      

### Запуск проекта

- Склонируйте репозиторий:

```
git clone https://github.com/AlexeyPeresypkin/flask_stepik_2.git
```
Cоздайте и активируйте виртуальное окружение:

```
python -m venv venv
```
```
source venv/bin/activate 
```
Обновите pip и установите зависимости:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Создайте в папке приложения файл .env со следующими переменными:
```
DATABASE_URL=postgresql://<login>:<password>@127.0.0.1:5432/<psql_db_name>
APP_SECRET_KEY=my-super-secret-phrase-I-dont-tell-this-to-nobody
```
Создайте таблицы в базе данных:
```
python db_create.py
```
Наполните таблицы данными из JSON файлов:
```
python db_dump_data.py
```
Запустите приложение
```
python app.py
```
![alt text](screenshots/01.png "Главная страница")

![alt text](screenshots/02.png "Все преподаватели")

![alt text](screenshots/03.png "заявка на подбор преподавателя")
