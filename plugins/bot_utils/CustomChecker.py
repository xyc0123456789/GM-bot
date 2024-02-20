# -*- coding: utf-8 -*-
from nonebot.adapters.onebot.v11 import Event, PrivateMessageEvent, GroupMessageEvent

import bot


async def is_me(event: Event):
    return event.get_user_id() == str(bot.SUPER_ADMIN)

async def is_private(event: Event):
    return isinstance(event, PrivateMessageEvent)

async def is_admin(event: GroupMessageEvent):
    return event.sender.role == "admin"