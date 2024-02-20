from nonebot import get_driver, on_command
from nonebot.adapters.onebot.v11 import GROUP_ADMIN, Event
from nonebot.internal.permission import Permission
from nonebot.plugin import PluginMetadata

import bot
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="kick_last",
    description="",
    usage="",
    config=Config,
)

from ..bot_utils.CustomChecker import is_admin, is_me

from ..bot_utils.kickImpl import KickReq, kick

global_config = get_driver().config
config = Config.parse_obj(global_config)

p = Permission(is_admin, is_me)
kick_last = on_command("kicklast", permission=p)


@kick_last.handle()
async def handle_function(event: Event):
    if event.message_type != "group":
        await kick_last.finish()
    group_id = event.group_id
    if len(bot.toKickList) == 0:
        await kick_last.finish("请先调用#detect")
    kReq = KickReq(group_id, bot.toKickList)
    await kick(kReq)
    await kick_last.finish(str(kReq))
