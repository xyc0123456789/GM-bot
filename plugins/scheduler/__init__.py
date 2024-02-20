from nonebot import get_driver
from nonebot import logger
from nonebot import require
from nonebot.plugin import PluginMetadata

from .config import Config
from ..update_members import membersService

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler

__plugin_meta__ = PluginMetadata(
    name="scheduler",
    description="",
    usage="",
    config=Config,
)

global_config = get_driver().config
config = Config.parse_obj(global_config)



# 基于装饰器的方式
@scheduler.scheduled_job("cron", hour="3", minute="0", second="0", id="job_0")
async def update():
    logger.info("start scheduled_job update 536348689")
    await membersService.updateGroup(536348689)
