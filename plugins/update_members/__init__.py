import re

from nonebot import get_driver, on_command
from nonebot.adapters.onebot.v11 import Event, PrivateMessageEvent
from nonebot.internal.permission import Permission
from nonebot.plugin import PluginMetadata

from .MembersUtil import MembersService
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="update_members",
    description="",
    usage="",
    config=Config,
)

from ..bot_utils.CustomChecker import is_me, is_private

global_config = get_driver().config
config = Config.parse_obj(global_config)


p = Permission(is_me, is_private)
member_update = on_command("update", permission=p)
membersService = MembersService()


@member_update.handle()
async def handle_function(event: Event):
    msg: str = event.get_message().__str__()
    print(msg, event.get_user_id(), event.get_session_id())

    ans = []
    if msg.strip() != "#update":
        todo = re.split(r"\s+", msg)[1:]
    else:
        todo = ["536348689"]
    print("start update ", todo)
    for i in todo:
        tmp = await membersService.updateGroup(i)
        toAp = "OK" if tmp else "FAIL"
        ans.append(i + ":" + toAp)
    await member_update.finish(str(ans))
