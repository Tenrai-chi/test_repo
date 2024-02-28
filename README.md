# Stripe Store
 Решение тестового задания для вакансии "Python Backend Developer (Django)"
 
## ТЗ
Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
* Django Модель Item с полями (name, description, price) 
* API с двумя методами:
    - **GET /buy/{id}**, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
    - **GET /item/{id}**, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)
* Разместить решение и описать запуск в README.md
* Опубликовать решение, чтобы его можно было легко и быстро протестировать
* **Бонусные задачи:**
    - Запуск с помощью Docker
    - Использование environment variables
    - Просмотр Django Моделей в админ панели
    - Запуск приложения на удаленном сервере, доступном для тестирования
    - Модель Order, которая объединяет несколько item, а платеж в Stripe происходит на содержимое Order с общей стоимостью всех items
    - Модели Discount и Tax, которые подкрепляются к Order и связываются с соответсвующими атрибутами при создании платежа в Stripe.
    - Добавить поле в модели Item "currency", добавить 2 Dtripe Keypair на две разные валюты. В зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте.
    - Вместо Stripe Session реализовать Stripe Payment Intent
      
## Установка проекта
Проверьте установлен ли Docker
```bash
docker version
```
Если Docker отсутствует, установите его.
Клонируйте рипозиторий на свое устройство:
```bash
git clone https://github.com/Tenrai-chi/test_repo.git
```
Перейдите в папку проекта
```bash
cd store
```
Измените файл .env.docker. В параметре STRIPE_SECRET_KEY_TEST установите собственный секретный ключ Stripe. Для этого необходимо зарегистрироваться на этом сервисе и зайти [сюда](https://dashboard.stripe.com/test/apikeys)
Теперь вы можете создать образ. Вместо docker_test_store можете указать свое собственное имя образа.
```bash
docker build . --tag docker_test_store
```
Запустите контейнер на основе созданного образа.
```bash
docker run -p 8000:8000  docker_test_store 
```
Теперь проект работает на вашем [localhost](http://127.0.0.1:8000/)
## Административная панель
Зайти в административную панель вы можете [здесь](http://127.0.0.1:8000/admin/)
| Пользователь  | Логин | Пароль  |
|---------------|-------|---------|
| Администратор | admin | password|












