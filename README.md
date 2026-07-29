# 🚫 Image Moderation API

## 🇷🇺 Описание на русском

Демонстрационный пример сервиса модерации изображений. Приложение реализует REST API для проверки загружаемых изображений с использованием внешнего сервиса Sightengine API, который принимает изображение и отправляет его на проверку в [Sightengine API](https://sightengine.com/) для определения нежелательного контента (NSFW).  

Если вероятность неприемлемого контента превышает 0.7, изображение отклоняется.

---

## 📦 Стек

- Python 3.10
- FastAPI
- Sightengine API
- Docker
- pytest

---

## 🚀 Запуск локально

1. Клонируйте репозиторий и установите зависимости:

pip install -r requirements.txt

2. Заполните .env файл в корне проекта:

SIGHTENGINE_USER=your_user_id
SIGHTENGINE_SECRET=your_api_secret

3. Запустите сервер:

uvicorn main:app --reload

Сервер будет доступен по адресу: http://localhost:8000

## 📸 Пример запроса (curl)
curl -X POST http://localhost:8000/moderate \
  -F "file=@example.jpg"
### 📥 Ответы:
- Безопасное изображение:
{"status": "OK"}
- Обнаружен NSFW-контент:
{"status": "REJECTED", "reason": "NSFW content"}

## 📬 Пример запроса в Postman

1. Откройте Postman и создайте новый запрос
2. Выберите метод: `POST`
3. Вставьте URL: http://localhost:8000/moderate
4. Перейдите во вкладку **Body** → выберите `form-data`
5. Добавьте поля:
   - **Key**: `file`
   - **Type**: `File`
   - **Value**: выберите `.jpg` или `.png` изображение
6. Нажмите **Send**

### 📥 Ответы:
- Безопасное изображение:
{
  "status": "OK"
}
- Обнаружен NSFW-контент:
{
  "status": "REJECTED",
  "reason": "NSFW content"
}

## 🐳 Запуск через Docker

### Сборка образа:
docker build -t nsfw-api .
### Запуск контейнера с передачей .env:
docker run --env-file .env -p 8000:8000 nsfw-api

## 🧪 Тестирование

Проект включает базовый тест на /moderate.

### Запуск тестов в Docker:
docker build -t nsfw-api .
docker run --rm -v $(pwd):/app nsfw-api pytest

### Запуск тестов локально:
pytest

## 📝 Примечание

Для использования Sightengine API необходимо зарегистрироваться на sightengine.com и получить API credentials.

---

## 🧩 Идеи для развития проекта

Это минимальный MVP, демонстрирующий отправку изображения и интеграцию с сервисом модерации контента. Для полноценного приложения можно было бы реализовать:

### 🔐 Авторизация и пользователи
- Регистрация и аутентификация пользователей (например, через JWT или Telegram)
- Ограничение доступа к API по токену

### 🗃️ Хранение данных
- Сохранение истории проверок в базу данных (PostgreSQL, MySQL и др.)
- Привязка изображений к пользователям
- Возможность просмотра статистики

### 💾 Обработка и хранение изображений
- Сохранение загруженных файлов на диск или в S3
- Предварительное изменение размера или сжатие

### 📊 Админ-панель
- Интерфейс для просмотра результатов проверок
- Возможность ручной модерации
---

Такие шаги позволят превратить проект в полноценный сервис с авторизацией, историей, аналитикой и масштабируемостью.


## 🇬🇧 English version

A simple backend application built with FastAPI that accepts an uploaded image and sends it to the Sightengine API to detect unwanted (NSFW) content.

If the probability of NSFW content exceeds 0.7, the image is automatically rejected.
---

## 📦 Tech Stack

- Python 3.10
- FastAPI
- Sightengine API
- Docker
- pytest

---

## 🚀 Running Locally

1. Clone the repository and install dependencies:

pip install -r requirements.txt

2. Create a .env file in the project root and fill in your API credentials:

SIGHTENGINE_USER=your_user_id
SIGHTENGINE_SECRET=your_api_secret

3. Start the development server:

uvicorn main:app --reload
Server will be available at: http://localhost:8000

## 📸 Example request (curl)
curl -X POST http://localhost:8000/moderate \
  -F "file=@example.jpg"
### 📥 Possible responses:
- Safe image:
{"status": "OK"}
- NSFW content detected:
{"status": "REJECTED", "reason": "NSFW content"}

## 📬 Example request in Postman

1. Open Postman and create a new request
2. Method: POST
3. URL: http://localhost:8000/moderate
4. Go to the Body tab → choose form-data
5. Add fields:
   - **Key**: `file`
   - **Type**: `File`
   - **Value**: choose a .jpg or .png image
6. Click **Send**

### 📥 Ответы:
- Safe image:
{
  "status": "OK"
}- NSFW content detected:
{
  "status": "REJECTED",
  "reason": "NSFW content"
}

## 🐳 Running via Docker

### Build the image:
docker build -t nsfw-api .
### Run the container with .env:
docker run --env-file .env -p 8000:8000 nsfw-api

## 🧪 Testing

The project includes a basic test for the /moderate endpoint.

### Run tests in Docker:
docker build -t nsfw-api .
docker run --rm -v $(pwd):/app nsfw-api pytest

### Run tests locally:
pytest

## 📝 Note

To use the Sightengine API, you must sign up at sightengine.com and obtain API credentials.

---

## 🧩 Ideas for further development

This is a minimal MVP that demonstrates basic integration with an image moderation API. To build a full-fledged service, consider adding:

### 🔐 Authentication & Users
- User registration and authentication (e.g. via JWT or Telegram login)
- API access control via token

### 🗃️ Data Storage
- Save moderation history to a database (PostgreSQL, MySQL, etc.)
- Associate images with users
- View moderation statistics

### 💾 Image Handling
- Save uploaded files locally or to S3
- Preprocess: resize, compress, etc.

### 📊 Admin Dashboard
- Interface to view moderation results
- Manual moderation option
---
These additions would allow the project to evolve into a scalable image moderation platform with auth, analytics, and persistence.



