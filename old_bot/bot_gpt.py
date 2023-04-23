import openai
import time

# Установите ваш API ключ
openai.api_key = "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"

# Задайте параметры для создания сеанса GPT-3
session_prompt = "Ты задумываешь число от 1 до 50 и будешь мне давать подсказки больше или меньше.А я буду его угадывать"
max_tokens = 200
temperature = 0.5

# Начните чат с пользователем
while True:
    # Получите ввод от пользователя
    user_input = input("Вы: ")

    # Отправьте запрос к GPT-3 с текущим состоянием диалога
    response = openai.Completion.create(
        engine="davinci",
        prompt=session_prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        stop=None,
    )

    # Получите ответ от GPT-3
    bot_response = response.choices[0].text.strip()

    # Обновите состояние диалога
    session_prompt += f"\nВы: {user_input}\nБот: {bot_response}"

    # Выведите ответ бота на экран
    print(f"Бот: {bot_response}")

    # Подождите немного перед следующим запросом к GPT-3
    time.sleep(1)