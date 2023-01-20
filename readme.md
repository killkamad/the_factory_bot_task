# Factory test task

Были выполнены все пункты

## Инструкция для запуска.

1. Настройка виртуального окружения

   1.1 Создать и активировать виртуальное окружение

    ```bash
   # Windows:
    python -m venv venv
   .\venv\Scripts\activate
   
   # Linux:
   virtualenv -p python3.8 .venv
   source .venv/bin/activate
    ```
   1.2 Установка необходимых библиотек

    ```bash
    pip install -r requirements.txt
    ```

2. Установить и запустить Redis сервер

   ```bash
    # Windows 
    Установить "Redis 5.0.10 for Windows" используя msi
   
   # Linux
   sudo apt install redis-server
    ```
3. Запуск celery

   4.1 В командой строке выполнить следующую команду
   ```bash
   # Windows
    celery -A the_factory_bot_task worker --loglevel=info -P gevent
   
   # Linux
    celery -A the_factory_bot_task worker --loglevel=info
    ```

4. Сделать миграции и создать супер пользователя

    ```bash
    ./manage.py makemigrations
    ./manage.py migrate
    ```

    ```bash
    ./manage.py createsuperuser
   
   email: admin@gmail.com
   password: admin
    ```

5. Запустить сервер и проверить его работу открыв `localhost:8000` в браузере

    ```bash
    ./manage.py runserver
    ```


6. Для удобства все запросы собраны в файле Insomnia.json

   7.1 Нужно установить программу Insomnia

   7.2 Импортировать из файла Insomnia.json
