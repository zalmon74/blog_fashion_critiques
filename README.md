# Проект на django. Blog Fashion Critiques

Для проекта исопользуется БД postgresql
_______


1. В requirements/base.txt приведен список необходимых модулей для проекта. Установить требуемые модули можно следующим образом:

```
pip install -r requirements/base.txt
```

2. Все 'секретные' данные (`SECRET_KEY`, настройки подключения к БД: `NAME`, `USER`, `PASSWORD`) должны находиться в файле .env, который расположен на уровень выше проекта. Данный функционал реализуется благодаря модулю `python-dotenv`. Все перечисленные 'секретные данные необходимо добавить в файл .env'. В данном проекте перечисленные поля называются в файле следующим образом:
   
  Имя настроечного параметра  |           Имя необходимое задать в файле .env            |                           Комментарии                            |
|:----------------------------:|:--------------------------------------------------------:|:----------------------------------------------------------------:|
|          SECRET_KEY          |                        SECRET_KEY                        |    Ключевой параметр для защиты отправляемых данных на сервер    |
|       DATABESES: NAME        |      NAME_BD_DJANGO_PROJECT_BLOG_FASHION_CRITIQUES       |  Имя базы данных в postgresql, которое использует данный проект  |
|       DATABESES: USER        |    NAME_USER_BD_DJANGO_PROJECT_BLOG_FASHION_CRITIQUES    |        Имя пользователя для подключение к БД в postgresql        |
|     DATABASES: PASSWORD      |  PASSWORD_USER_BD_DJANGO_PROJECT_BLOG_FASHION_CRITIQUES  |             Пароль пользователя для подключения к БД             |

   