import telebot
from telebot.types import Chat, ChatFullInfo, Message, MessageEntity, User
from random_unicode_emoji import random_emoji
import time

from settings import settings

bot = telebot.TeleBot(settings, parse_mode=None)

ID = int
UserID = ID
ChatID = ID

def get_text_and_entities_for_users(users: list[UserID], chat_id: ChatID) -> list[(str, list[MessageEntity] | None)]:
    emojis = random_emoji(count=len(users))
    current_string = ""
    message_entities = None

    offset = 0

    for i, user in enumerate(users):
        user_info = bot.get_chat_member(
            chat_id=chat_id,
            user_id=user
        )

        if user_info.user.is_bot:
            continue

        # user_status = user_info.status

        # if user_status == 'administrator' or user_status == 'creator':
        #     continue

        if message_entities is None:
            message_entities = []

        emoji = emojis[i]
        length = len(emoji)
        current_string += emoji

        message_entities.append(
            MessageEntity(
                type="text_mention", offset=offset, length=length, user=user_info.user
            )
        )
        offset += length
    
    return [(current_string, message_entities)]


def get_user_ids(chat_id: ChatID) -> list[UserID]:
    pass


@bot.message_handler(func=lambda x: x == "@all")
def ping_all(message: Message):
    time.sleep(2)

    chat_id = message.chat.id
    user_ids = get_user_ids(message.chat.id)

    for string, mes_entities in get_text_and_entities_for_users(users=user_ids, message=message):
        bot.send_message(
            chat_id=chat_id,
            text=string if string else "No users to call",
            entities=mes_entities
        )

bot.infinity_polling()