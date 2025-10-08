# EmotionalAnalyze

**EmotionalAnalyze** — это сервис на **Django + DRF**, который анализирует эмоции по фотографии.
Он использует [DeepFace](https://pypi.org/project/deepface/) для распознавания лиц и определения эмоционального состояния (neutral, happy, sad, angry и др.).

---

## Основные возможности

* **Приём изображений** через API (поддержка `JPG`, `PNG` и других форматов)
* **Детекция лица** на фото
* **Определение эмоций** с помощью DeepFace
* **REST API**, готовое к интеграции с любыми фронтендами или внешними системами
* Поддержка `JSON` и `multipart/form-data` запросов
* Автогенерация OpenAPI схем через **drf-spectacular**

---

## Технологический стек

* [Python 3.10+](https://www.python.org/)
* [Django 4+](https://www.djangoproject.com/)
* [Django REST Framework](https://www.django-rest-framework.org/)
* [DeepFace](https://github.com/serengil/deepface)
* [drf-spectacular](https://drf-spectacular.readthedocs.io/)

---

## Установка и запуск проекта

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
[http://127.0.0.1:8000/api/v1/emotions/analyze/](http://127.0.0.1:8000/api/v1/emotions/analyze/)

---

## Пример запроса

### cURL

```bash
curl -X POST http://127.0.0.1:8000/api/v1/emotions/analyze/ \
  -F "image=@face.jpg"
```

### Пример успешного ответа

```json
{
  "result": [
    {
      "emotion": {
        "angry": 0.009361479431390762,
        "disgust": 3.557223919870012e-7,
        "fear": 0.0072294375859200954,
        "happy": 0.00009973931446438655,
        "sad": 0.07172159850597382,
        "surprise": 0.0012769456952810287,
        "neutral": 99.91031646728516
      },
      "dominant_emotion": "neutral",
      "region": {
        "x": 80,
        "y": 19,
        "w": 67,
        "h": 67,
        "left_eye": null,
        "right_eye": null
      },
      "face_confidence": 0.92
    },
    {
      "emotion": {
        "angry": 0.0005845140549354255,
        "disgust": 5.310060169350095e-10,
        "fear": 99.95538330078125,
        "happy": 0.000496282649692148,
        "sad": 0.04309580847620964,
        "surprise": 0.00006916822894709185,
        "neutral": 0.000369494897313416
      },
      "dominant_emotion": "fear",
      "region": {
        "x": 22,
        "y": 25,
        "w": 57,
        "h": 57,
        "left_eye": null,
        "right_eye": null
      },
      "face_confidence": 0.98
    }
  ]
}
```

### Пример ошибки (лицо не найдено)

```json
[
  "Не удалось распознать лицо на изображении. Пожалуйста, загрузите фото с видимым лицом."
]
```

---

## Документация API

После запуска проекта открой Swagger UI по адресу:
[http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)

