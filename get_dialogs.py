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

async def list_chats():
    # Connect to Telegram
    await client.start()

    # Get all dialogs (chats)
    dialogs = await client.get_dialogs()

    # Print chat names and IDs
    for dialog in dialogs:
        print(f"Chat Name: {dialog.name}, Chat ID: {dialog.id}")


if __name__ == "__main__":
    # Run the script
    with client:
        client.loop.run_until_complete(list_chats())
