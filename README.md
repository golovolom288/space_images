# TG SPACE

## Описание
Скачивает новейшие фотографии наса и отправляет их в тг чат
## Как установить
Скачиваем с помощью git clone проект
### Зависимости
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```python
pip install -r requirements.txt
```
### Переменные окружения
Создайте файл .env без расширения.
Вставьте этот код в файл, заменив текст на свой токен
```python
NASA_TOKEN="Вставьте сюда свой токен"
TG_BOT_TOKEN="Вставьте сюда токен бота"
TG_GROUP_ID="Вставьте сюда айди группы в тг"
TG_TIME="Укажите время отправки фото в тг"
```
#### Как получить токен
  Зайдите на сайт api.nasa.gov, после чего введите почту и пароль, создайте апи токен
  Напишите боту @BotFather и создайте бота, где получите токен
  Создайте тг группу и скопируйте её адрес, напишите боту @username_to_id_bot ссылку на группу и получите айди группы.
## Запуск
откройте консоль, введите команду cd "Вставьте сюда путь до проекта".
Введите в консоль python main.py "Раз в сколько часов бот отправляет фото или не указывайте вообще"
## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.