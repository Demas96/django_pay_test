# Django + Stripe API
Тестовое задание  

Для запуска необходимо скачать репозиторий, создать виртуальное окружение, установить библиотеки из requirements.txt и 
запустить django сервер.  

Для удобства данный проект размещен по адресу https://dmitrykizima.pythonanywhere.com/. Логин/пароль от админки: admin/admin  

Наверху расположены ссылки на админ-панель django, список с моделями Item и список с моделями Order.
Все модели доступны по адресам:  
https://dmitrykizima.pythonanywhere.com/item/{id}  
https://dmitrykizima.pythonanywhere.com/order/{id}  
(id указаны на странице со списком моделей)  

В админ-панеле, помимо моделей Order и Item, также отображаются модели Discounts и Tax. 
С помощью этих моделей можно изменять цену модели Order в процентах в формате десятичной дроби 
для последующей оплаты.  

При создании Order и Item можно выбрать валюту. Если используются Item с разными валютами, 
то в Order они конвертируются по условному 70 рублей за 1 доллар.