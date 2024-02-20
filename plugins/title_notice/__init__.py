from typing import Annotated

from nonebot import get_driver, on_notice, logger
from nonebot.adapters.onebot.v11 import Event, NoticeEvent, Message
from nonebot.internal.rule import Rule
from nonebot.params import EventMessage
from nonebot.plugin import PluginMetadata

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="title_notice",
    description="",
    usage="",
    config=Config,
)

from ..update_members import membersService

global_config = get_driver().config
config = Config.parse_obj(global_config)

async def is_notice_notify_title(event: Event) -> bool:
    return isinstance(event, NoticeEvent) and event.get_event_name() == "notice.notify.title"

rule = Rule(is_notice_notify_title)

title_notice = on_notice(rule=rule)

@title_notice.handle()
async def handle_function(event: Event):
    # 获取新人的id
    user_id = event.get_user_id()
    # 获取群号
    group_id = event.group_id
    t=event.dict()["title"]
    logger.warning(f"title_notice: {group_id} {user_id} {type(t)} {t}")
    membersService.updateTitle(group_id, user_id, t)
    await title_notice.finish()