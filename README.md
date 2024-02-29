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
    - [x] Запуск с помощью Docker
    - [x] Использование environment variables
    - [x] Просмотр Django Моделей в админ панели
    - [ ] Запуск приложения на удаленном сервере, доступном для тестирования
    - [x] Модель Order, которая объединяет несколько item, а платеж в Stripe происходит на содержимое Order с общей стоимостью всех items
    - [ ] Модели Discount и Tax, которые подкрепляются к Order и связываются с соответсвующими атрибутами при создании платежа в Stripe.
    - [ ] Добавить поле в модели Item "currency", добавить 2 Dtripe Keypair на две разные валюты. В зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте.
    - [ ] Вместо Stripe Session реализовать Stripe Payment Intent
      
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
Перейдите в папку проекта Store
```bash
cd store
```
Измените файл .env.docker. В параметре STRIPE_SECRET_KEY_TEST установите собственный секретный ключ Stripe. Для этого необходимо зарегистрироваться на этом сервисе и зайти [сюда](https://dashboard.stripe.com/test/apikeys).
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

## Тестовые карты
Для тестирования оплаты предлагаю воспользоваться этими картами. У всех карт CVC - любые 3 цифры, а дата окончания - любая будущая дата окончания.
|   Платеж  |       Номер      |       Ошибка       |
|-----------|------------------|--------------------|
|  Успешно  | 4242424242424242 |          Х         |
| Неуспешно | 4000000000009995 |Недостаточно средств|
| Неуспешно | 4000000000000127 |  Неправильный CVC  |
| Неуспешно | 4242424242424241 |   Неверный номер   |

## Реализация
* На главной странице выводится информация обо всех товарах. Все названия кликабельные и перенаправляют на страницу с подробным описанием товара. Также на странице есть кнопка, которая перенаправляет пользователя на страницу с его текущей карзиной.
  
![image](https://github.com/Tenrai-chi/test_repo/assets/79309888/046a2400-8f25-4313-ba86-bdafc1f775fd)
* При просмотре товара выдается информация о его названии, описании и цене. На странице есть кнопки "Добавить в корзину" и "Купить". Первая добавляет товар в корзину, а вторая перенаправляет пользователя на страницу оплаты с использованием Stripe.
  
![image](https://github.com/Tenrai-chi/test_repo/assets/79309888/c1f5d976-23be-4325-bdb8-48887a6d2d30)
* В корзине отображаются все добавленные товары и их количество, а также показывается итоговая сумма возможного заказа. На этой странице есть кнопка "BUY", которая перенаправляет на страницу оплаты Stripe.
* После оплаты. Если оплата прошла успешно, пользователя перенаправлет на страницу с успешной оплатой. Статус заказа становится "Оплачен". Если оплата была неуспешной, то пользователя перенаправит на другую страницу, уведомляющую о неудаче при оплате.

Со списком используемых библиотек можно ознакомиться [здесь](https://github.com/Tenrai-chi/test_repo/blob/main/store/requirements.txt)
