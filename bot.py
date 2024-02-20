# -*- coding: utf-8 -*-
import logging
import sys

import nonebot
from nonebot import logger
from nonebot.adapters.onebot import V11Adapter
from nonebot.log import default_filter, default_format

from GetPathUtil import getPath

logger.remove()
logger_id = logger.add(
    sys.stdout,
    level=0,
    diagnose=False,
    filter=default_filter,
    format=default_format,
)
logger_file_id = logger.add(
    "main.log",
    level=0,
    diagnose=False,
    filter=default_filter,
    format=default_format,
)

SUPER_ADMIN = 0
toKickList = []


class BotStarter:
    def __init__(self):
        # 初始化 NoneBot
        nonebot.init()

        # 注册适配器
        driver = nonebot.get_driver()
        driver.register_adapter(V11Adapter)

        # 在这里加载插件
        # nonebot.load_builtin_plugins("echo")  # 内置插件
        nonebot.load_plugin("nonebot_plugin_apscheduler")  # 第三方插件
        nonebot.load_plugins(getPath("plugins"))  # 本地插件

    def start(self):
        nonebot.run()


if __name__ == "__main__":
    starter = BotStarter()
    starter.start()
