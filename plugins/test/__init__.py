from nonebot import get_driver, on_command, get_bots, logger
from nonebot.adapters.onebot.v11 import Event, Message, MessageSegment
from nonebot.internal.rule import Rule
from nonebot.plugin import PluginMetadata

from GetPathUtil import getTheBot
from common.MessageBuilder import MessageBuilder
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="test",
    description="",
    usage="",
    config=Config,
)

from ..bot_utils.CustomChecker import is_me

global_config = get_driver().config
config = Config.parse_obj(global_config)


rule = Rule(is_me)
test_command = on_command("test", rule=rule)

@test_command.handle()
async def handle_function(event: Event):
    bot = getTheBot()
    group_id=0
    user_id=0
    oneData =""
    # oneData = await bot.call_api("get_group_member_info", group_id=group_id, user_id=user_id)
    # oneData = await bot.call_api("set_group_kick", group_id=group_id, user_id=user_id, reject_add_request=False)
    # oneData = await bot.call_api("send_private_msg", user_id=user_id,message="test")
    # oneData = await bot.call_api("send_private_msg", user_id=user_id, message=Message([MessageSegment.image(r"http://gchat.qpic.cn/gchatpic_new/0/0-0-B8F694B7886F0E94481D91958E8AE31F/0?term=2")]))
    # oneData = await bot.call_api("send_group_msg", group_id=group_id, message=Message(MessageBuilder().appendImage(file="http://gchat.qpic.cn/gchatpic_new/0/0-0-B8F694B7886F0E94481D91958E8AE31F/0?term=2").appendText("test...").appendAt(user_id).build()))
    oneData = await bot.call_api("send_group_msg", group_id=group_id, message=Message(MessageBuilder().appendImage(file=r"C:\Users\13395\Pictures\22f4e0e7-0c16-4807-ade6-ae373c0f8bc4.jpg").appendText("test...").appendAt(user_id).build()))
    # oneData = await bot.call_api("get_group_list")

    logger.warning(oneData)
