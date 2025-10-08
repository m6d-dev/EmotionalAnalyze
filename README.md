Вот улучшенная, аккуратно оформленная и читабельная версия твоего `README.md` файла 👇
(С красивыми блоками, иконками, кодовыми блоками и единым стилем оформления)

---

# 🧠 EmotionalAnalyze

**EmotionalAnalyze** — это сервис на **Django + DRF**, который анализирует эмоции по фотографии.
Он использует [DeepFace](https://pypi.org/project/deepface/) для распознавания лиц и определения эмоционального состояния (🎭 neutral, 😃 happy, 😢 sad, 😡 angry и др.).

---

## 🚀 Основные возможности

* 📸 **Приём изображений** через API (поддержка `JPG`, `PNG` и других форматов)
* 🧍‍♂️ **Детекция лица** на фото
* 😃 **Определение эмоций** с помощью DeepFace
* 🌐 **REST API**, готовое к интеграции с любыми фронтендами или внешними системами
* 📝 Поддержка `JSON` и `multipart/form-data` запросов
* 📄 Автогенерация OpenAPI схем через **drf-spectacular**

---

## 🛠️ Технологический стек

* [🐍 Python 3.10+](https://www.python.org/)
* [🌿 Django 4+](https://www.djangoproject.com/)
* [🧰 Django REST Framework](https://www.django-rest-framework.org/)
* [🧠 DeepFace](https://github.com/serengil/deepface)
* [📜 drf-spectacular](https://drf-spectacular.readthedocs.io/)

---

## 📂 Установка и запуск проекта

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/m6d-dev/EmotionalAnalyze.git
cd EmotionalAnalyze
```

### 2. Создайте и активируйте виртуальное окружение

```bash
# Linux / macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Установите зависимости

```bash
pip install -r requirements.txt
```

### 4. Примените миграции и запустите сервер

```bash
python manage.py migrate
python manage.py runserver
```

После запуска API будет доступно по адресу:
👉 [http://127.0.0.1:8000/api/v1/emotions/analyze/](http://127.0.0.1:8000/api/v1/emotions/analyze/)

---

## 🧪 Пример запроса

### cURL

```bash
curl -X POST http://127.0.0.1:8000/api/v1/emotions/analyze/ \
  -F "image=@face.jpg"
```

### Пример успешного ответа

```json
{
  "emotion": "happy",
  "confidence": 0.97
}
```

### Пример ошибки (лицо не найдено)

```json
[
  "Не удалось распознать лицо на изображении. Пожалуйста, загрузите фото с видимым лицом."
]
```

---

## 📜 Документация API

После запуска проекта открой Swagger UI по адресу:
👉 [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)

---

## 🧰 Структура проекта

```
EmotionalAnalyze/
├── src/
│   ├── apps/
│   │   └── emotions/
│   │       ├── serializers.py
│   │       ├── use_case.py
│   │       └── views.py
│   ├── settings.py
│   └── urls.py
├── requirements.txt
└── manage.py
```

---

## 🤝 Вклад в проект

PR’ы и идеи приветствуются.
Если хотите внести вклад — создайте **issue** или **pull request**.

---