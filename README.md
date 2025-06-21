# 🎯 AI-рекомендатель: чем заняться вечером?

Интерактивное приложение, которое подскажет, как провести вечер, учитывая:
- текущую погоду,
- личные интересы пользователя.

Проект создан как часть портфолио в области AI-разработки.

![preview](assets/screenshot.png)


## 🚀 Возможности

- Получение реальной погоды через OpenWeather API
- Интерактивный интерфейс (Streamlit)
- Выбор интересов (кино, прогулки, еда и т.д.)
- Персональные рекомендации в зависимости от условий
- Модульная структура, легко расширяется

## 🧱 Стек технологий

- Python 3.10+
- Streamlit
- Requests
- OpenWeather API

1. Клонировать репозиторий:

```bash
1. git clone https://github.com/твоя-ссылка.git

cd evening-recommender

2. Создать виртуальное окружение и активировать:

python -m venv venv
.\venv\Scripts\activate        # для Windows
                               # или
source venv/bin/activate       # для Mac/Linux

3. Установить зависимости:

pip install -r requirements.txt

4. Вставить свой API-ключ в src/ui_app.py:

API_KEY = "твой_ключ_сюда"

▶️ Запуск

streamlit run src/ui_app.py
