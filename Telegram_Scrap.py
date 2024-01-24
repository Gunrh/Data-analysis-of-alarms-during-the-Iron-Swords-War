

from pyrogram import Client
from telethon.sync import TelegramClient
import datetime
import os


# Replace with your own values
api_id = "Replace with your own values"
api_hash = "Replace with your own values"


chats = ['PikudHaOref_all']


target_date = datetime.date(2023, 10, 7)  # Specify the target date (The date of the start of the war)

file_path = os.path.join(os.getcwd(), f"new_data_{target_date}.txt")



total_alerts= 0

with TelegramClient('test', api_id, api_hash) as client:
    with open(file_path, "w", encoding="utf-8") as file:
        for chat in chats:
            for message in client.iter_messages(chat, offset_date=target_date, reverse=True):
                # print(message)
                total_alerts +=1

                message_str = f"Text: {message.text}\n \n"
                file.write(message_str)

print(total_alerts )

print("Data saved to text file.")
