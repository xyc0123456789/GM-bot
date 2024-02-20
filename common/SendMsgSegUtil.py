# -*- coding: utf-8 -*-
import time

from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11.message import MessageSegment, Message

from common.MessageBuilder import MessageBuilder
from plugins.update_members import membersService


def get_normal_member_str(group_id, user_id):
    mem = membersService.query(group_id,user_id)
    if mem is None:
        return str(user_id)
    elif len(mem.name_card.strip())!=0:
        return mem.name_card + f"<{mem.special_title}>"
    else:
        return mem.nick_name+f"<{mem.special_title}>"



async def send_message_for_ids(longs, message_str, contact, event, is_at):
    page_size = 30
    lists = [longs[i:i+page_size] for i in range(0, len(longs), page_size)]
    page = 0
    total = len(lists)
    for items in lists:
        page += 1
        message_chain = MessageBuilder()
        for user_id in items:
            if is_at:
                mem = membersService.query(event.group_id, user_id)
                if mem is None:
                    message_chain.appendAt(user_id)
                else:
                    message_chain.appendAt(user_id, mem.name_card if mem.name_card else mem.nick_name)
            else:
                tmp = get_normal_member_str(event.group_id, user_id)
                # print(tmp)
                message_chain.appendText(tmp+", ")
        message_chain.appendText(f"\ncurrent/pageSize: {len(items)}/{page_size} page: {page}/{total}\n")
        message_chain.appendText(message_str)
        await contact.send(message_chain.build())
        time.sleep(2)
