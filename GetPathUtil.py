# -*- coding: utf-8 -*-
import os

import nonebot

project_path = os.path.dirname(__file__)


def getPath(*relativePath: str) -> str:
    relativePathFiltered = [path for path in relativePath if path is not None and path != '']
    p = os.path.join(project_path, *relativePathFiltered)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    return p


def getTheBot():
    bots = nonebot.get_bots()
    for id in bots.keys():
        return bots[id]  # 获取 bot 对象
