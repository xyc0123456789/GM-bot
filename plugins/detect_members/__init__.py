import time

from nonebot import get_driver, on_command
from nonebot.adapters.onebot.v11 import GROUP_ADMIN, Event, MessageSegment, Message
from nonebot.adapters.onebot.v11.permission import _group_admin
from nonebot.internal.permission import Permission
from nonebot.plugin import PluginMetadata

import bot
from common.SendMsgSegUtil import send_message_for_ids
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="detect_members",
    description="",
    usage="",
    config=Config,
)

from ..bot_utils.CustomChecker import is_me, is_admin

from ..update_members import membersService

global_config = get_driver().config
config = Config.parse_obj(global_config)



p = Permission(is_admin, is_me)

detect_members = on_command("detect", permission=p)


@detect_members.handle()
async def handle_function(event: Event):
    if event.message_type != "group":
        await detect_members.finish()
    group_id = event.group_id
    msg: str = event.get_message().__str__()
    isAt = True
    if len(msg) > 7 and msg[7:8].lower() == "n":
        isAt = False

    idList = membersService.detect(group_id)

    bot.toKickList = idList
    message_str = "以上成员仍未找群主验证获得群头衔，请及时修改群名片，找群主验证获取群头衔。相关证明请私信群主或者直接发群里，学信网、校园卡、录取通知等均可"

    await send_message_for_ids(idList, message_str, detect_members, event, isAt)
