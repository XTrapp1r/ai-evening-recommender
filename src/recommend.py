def generate_recommendation(weather: dict, interests: list[str]) -> str:
    if not interests:
        return "Пожалуйста, выберите хотя бы один интерес."

    temp = weather.get("температура", 0)
    description = weather.get("погодное описание", "").lower()

    if temp > 20 and "Прогулки" in interests:
        return "🌞 Отличная погода — отправляйтесь на прогулку!"
    if "дожд" in description and "Кино" in interests:
        return "🎬 Идеально для кино — сходите в кинотеатр или устройте домашний просмотр."
    if "Кафе/еда" in interests:
        return "☕ Почему бы не попробовать новое кафе?"
    if "Спортзал" in interests:
        return "🏋️ Самое время размяться в спортзале."
    if "Музеи" in interests:
        return "🖼 Неплохой повод сходить в музей."
    if "Домашний отдых" in interests:
        return "🏠 Наслаждайтесь уютом дома с книгой или фильмом."

    return "📚 Можно выбрать что-то нейтральное — кафе, музей или прогулка."
