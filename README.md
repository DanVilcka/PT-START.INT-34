# PT-START.INT-34
for INT-34

# Server on Python
Для проверки работы сервера:
1. Клонируйте репозиторий и перейдите в папку проекта.
2. Соберите проект через ``` docker build -t http-server . ```.
3. Запустите сервер с помощью ``` docker run -p 8000:8000 http-srerver ```.
4. В браузере перейдите на ``` http://localhost:8000/healthz ```.