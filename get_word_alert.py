from telethon import TelegramClient, events

# Укажите данные для подключения к Telegram API
api_id = '26280627'           # Ваш api_id
api_hash = '1702f036546c8bad81a60098d4a6bf5d'       # Ваш api_hash
phone_number = '+77770975579'      # Ваш номер телефона

# Создаём клиент
client = TelegramClient('session_name', api_id, api_hash)

# Слово для отслеживания
TRIGGER_WORD = "TRIGGER_WORD"

# Событие для обработки входящих сообщений из канала или чата
@client.on(events.NewMessage)
async def handler(event):
    message = event.message.message
    
    # Проверяем наличие триггерного слова
    if TRIGGER_WORD in message:
        print(f"Найдено триггерное слово в сообщении: {message}")
    
# Запуск клиента
async def main():
    await client.start(phone=phone_number)
    
    # Подписка на определённый канал и пользователя (вместо 'channel_name' и 'user_name')
    await client.get_entity('channel_name')
    await client.get_entity('user_name')
    
    # Бесконечная прослушка событий
    await client.run_until_disconnected()

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())

