<p align="center">
  <img src="assets/AI-Recommend.png" alt="preview" width="600"/>
</p>

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-orange?logo=streamlit)
![Status](https://img.shields.io/badge/Project-Ready-success)

## 🎯 AI-рекомендатель: чем заняться вечером?

Интерактивное приложение, которое подскажет, как провести вечер, учитывая:
- текущую погоду,
- личные интересы пользователя.

Проект создан как часть портфолио в области AI-разработки.


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

## 🚀 Установка и запуск

```bash
# 1. Клонировать репозиторий
git clone git clone https://github.com/XTrapp1r/ai-evening-recommender.git
cd evening-recommender

# 2. Создать и активировать окружение
python -m venv venv
.\venv\Scripts\activate   # Windows
# или
source venv/bin/activate # Mac/Linux

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Вставить API-ключ в src/ui_app.py
# API_KEY = "твой_ключ_сюда"

# 5. Запуск
streamlit run src/ui_app.py
