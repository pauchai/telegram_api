from telethon import TelegramClient
from dotenv import load_dotenv
import os

# Загружаем переменные окружения из файла .env
load_dotenv()

# Replace 'your_api_id' and 'your_api_hash' with your actual API credentials
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')



# Create a new Telegram client
client = TelegramClient('session_name', api_id, api_hash)


async def get_last_messages():
    # Подключаемся к Telegram
    await client.start()

    # Получаем объект чата по имени группы или ссылке
    group = await client.get_entity('https://t.me/+ZTzmreYWp5kwYTBi')

    # Получаем последние 10 сообщений из группы
    messages = await client.get_messages(group, limit=10)

    # Выводим текст последних сообщений
    for message in messages:
        print(message.sender_id, message.text)

    # Закрываем сессию
    await client.disconnect()

if __name__ == "__main__":
    # Run the script
    with client:
        client.loop.run_until_complete(get_last_messages())
