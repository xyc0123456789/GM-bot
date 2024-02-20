from nonebot import get_driver, on_command, on_message
from nonebot.adapters.onebot.v11 import Event
from nonebot.plugin import PluginMetadata
from nonebot.rule import startswith

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="menu",
    description="",
    usage="",
    config=Config,
)

GROUPS = [536348689, 494611635]

global_config = get_driver().config
config = Config.parse_obj(global_config)

rule = startswith(("help", "#help", "menu"),ignorecase=True)

menu = on_message(rule=rule)

@menu.handle()
async def handle_function(event: Event):
    if event.message_type == "group":
        # 获取群聊的 ID
        group_id = event.group_id
        if group_id in GROUPS:
            m=("菜单: help #help menu\n"
               "检查头衔: #detect #detectn(不at)\n"
               "踢人: #kicklast(要求先调用检查头衔)")
            await menu.finish(m)
