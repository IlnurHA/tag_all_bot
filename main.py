from pyrogram import Client, filters
from pyrogram.types import Message, ChatMember, MessageEntity
from pyrogram.enums import ChatMemberStatus, ParseMode, UserStatus
from random_unicode_emoji import random_emoji
import logging

from settings import settings
from logger import log_file

logger = logging.getLogger(__name__)

FORMAT = '%(asctime)s %(message)s'

logging.basicConfig(
    filename=log_file,
    level=settings.logger_level,
    format=FORMAT
)

app = Client("my_bot_test", api_id=settings.api_id, api_hash=settings.api_hash, bot_token=settings.telegram_token)

ID = int
UserID = ID
ChatID = ID


def mention_text(users: list[ChatMember], limit=20, exclude: list[UserID] | None=None) -> list[str]:
    logger.debug("Trying to collect mention text for users %s and excluding %s", users, exclude)

    strs = []
    current_str = ""
    emojis_str = ""

    if exclude is None:
        exclude = []

    emojis = random_emoji(count=len(users))

    for emoji, chat_member in zip(emojis, users):
        if chat_member.user.id in exclude:
            continue

        current_str += f"[{emoji}](tg://user?id={chat_member.user.id})"
        emojis_str += emoji

        if len(emojis_str) >= limit:
            strs.append(current_str)
            current_str = ""
            emojis = ""
    
    if current_str != "":
        strs.append(current_str)
    
    return strs


async def get_chatmembers(chat_id: int, client: Client) -> list[ChatMember]:

    users = []
    async for member in client.get_chat_members(chat_id):
        member: ChatMember

        if member.user.is_bot:
            continue

        users.append(member)
    
    return users
 
@app.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    logger.info("User %d wrote 'start' command in chat %d", user_id, chat_id)
    
    await client.send_message(
        chat_id=chat_id,
        text="""**Welcome!**
Add me to some group and send either '@all' or 'Где все?' to tag all users"""
    )


@app.on_message(filters.regex("(?i)(^@all$)|(^Где все[\?\!]*$)"))
async def tag_all(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    logger.info("User %d trying to tag all chat members in chat %d", user_id, chat_id)

    if chat_id == message.from_user.id:
        await client.send_message(chat_id=chat_id, text="I can work only in group chats. "\
                                  "Please, add me to some chat. So, I can start to work!")
        logger.info("User %d trying to tag all chat members in private chat", user_id)
        return

    sender_chat_member = await client.get_chat_member(chat_id=chat_id, user_id=message.from_user.id)
    if sender_chat_member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        if message.text == "@all":
            await client.send_message(chat_id=chat_id, text="You cannot tag all chat members in this group. " \
                                        "Only administrators or owners can do that")
        logger.info("User %d trying to tag all chat members in chat %d without permission", user_id, chat_id)
        return
    
    users: list[ChatMember] = await get_chatmembers(message.chat.id, client)
    data = mention_text(users, limit=settings.emoji_limit, exclude=[sender_chat_member.user.id])

    if not data:
        await client.send_message(chat_id=chat_id, text="No users to tag")
        logger.info("No users found to tag in chat %d", chat_id)
        return

    await client.send_message(chat_id=chat_id, text=f"[Someone](tg://user?id={sender_chat_member.user.id}) started tagging all users in the chat")

    for string in data:
        await client.send_message(
            chat_id=chat_id,
            text=string,
            parse_mode=ParseMode.MARKDOWN
        )
    
    logger.info("Tagged chat members in chat %d successfully. Requested by user %d", chat_id, user_id)


app.run()
