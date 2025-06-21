import streamlit as st
from data_loader import get_weather
from recommend import generate_recommendation

API_KEY = "e7b8f1f1c4796a59a6dd3230aaaa6b9a"

st.title("AI-рекомендатель: чем заняться вечером?")

city = st.text_input("Введите город", value="Санкт-Петербург")

st.subheader("Ваши интересы:")
interests = st.multiselect(
    "Выберите, что вам нравится:",
    ["Кино", "Прогулки", "Кафе/еда", "Спортзал", "Музеи", "Домашний отдых"]
)

if st.button("Получить рекомендации"):
    weather = get_weather(city, API_KEY)

    if weather:
        st.subheader("Погода сейчас:")
        st.write(f"Температура: {weather['температура']}°C")
        st.write(f"Ощущается как: {weather['ощущается как']}°C")
        st.write(f"Описание: {weather['погодное описание']}")
        st.write(f"Скорость ветра: {weather['ветер']} м/с")

        st.subheader("Рекомендации:")
        message = generate_recommendation(weather, interests)
        st.write(message)

        