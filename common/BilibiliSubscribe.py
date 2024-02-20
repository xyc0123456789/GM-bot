# -*- coding: utf-8 -*-
from typing import Type

import requests
import json
import logging

from nonebot import logger

GET_INFO_URL = "https://api.live.bilibili.com/room/v1/Room/get_info?room_id="
ROOM_URL = "https://live.bilibili.com/"

platformName = "哔哩哔哩"


def getBilibiliLiveStatus(roomId: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    s = requests.get(GET_INFO_URL + roomId, headers=headers).text
    object = json.loads(s)
    if object["code"] == 1:
        logging.error("live room{" + roomId + "} not exist,msg{" + object["msg"] + "}")
        return None
    data = object["data"]
    subscriptionInfo = {}
    subscriptionInfo["platformName"] = platformName
    packageData(data, subscriptionInfo)
    return subscriptionInfo


def packageData(data, subscriptionInfo):
    info = data
    uid = info["uid"]
    roomId = info["room_id"]
    attention = info["attention"]
    online = info["online"]
    description = info["description"]
    areaName = info["area_name"]
    backgroundUrl = info["background"]
    title = info["title"]
    userCoverUrl = info["user_cover"]
    keyFrameUrl = info["keyframe"]
    liveTime = info["live_time"]
    tags = info["tags"]
    liveStatus = info["live_status"]
    subscriptionInfo["uid"] = uid
    subscriptionInfo["roomId"] = roomId
    subscriptionInfo["attention"] = attention
    subscriptionInfo["online"] = online
    subscriptionInfo["description"] = description
    subscriptionInfo["areaName"] = areaName
    subscriptionInfo["backgroundUrl"] = backgroundUrl
    subscriptionInfo["title"] = title
    subscriptionInfo["userCoverUrl"] = userCoverUrl
    subscriptionInfo["keyframeUrl"] = keyFrameUrl
    subscriptionInfo["liveStatus"] = liveStatus
    subscriptionInfo["liveTime"] = liveTime
    subscriptionInfo["tags"] = tags
    subscriptionInfo["roomUrl"] = ROOM_URL + str(roomId)


STATUS_DICT = {0: "未开播", 1: "直播中", 2: "轮放录像中"}


def construct(subscriptionInfo):
    # subscriptionInfo 是一个字典，包含以下键值对：
    # platformName: 平台名称
    # roomId: 房间号
    # title: 标题
    # userName: 主播昵称
    # liveStatusStr: 直播状态
    # areaName: 分区名称
    # attention: 关注人数
    # online: 直播在线
    # roomUrl: 直播链接

    # 使用字符串拼接构建输出信息
    message = f"平台-房间号: {subscriptionInfo['platformName']} - {subscriptionInfo['roomId']}\n"
    message += f"标题: {subscriptionInfo['title']}\n"
    # 如果主播昵称不为空，添加到信息中
    if subscriptionInfo.get("userName", None):
        message += f"主播昵称: {subscriptionInfo['userName']}\n"
    message += f"直播状态: {STATUS_DICT[subscriptionInfo['liveStatus']]}\n"
    # 如果分区名称不为空，添加到信息中
    if subscriptionInfo.get("areaName", None):
        message += f"分区名称: {subscriptionInfo['areaName']}\n"
    # 如果关注人数不为空，添加到信息中
    if subscriptionInfo["attention"]:
        message += f"关注人数: {subscriptionInfo['attention']}\n"
    # 如果直播在线不为空，添加到信息中
    if subscriptionInfo["online"]:
        message += f"直播在线: {subscriptionInfo['online']}\n"
    message += f"直播链接: {subscriptionInfo['roomUrl']}\n"
    # 返回信息字符串
    return message


class BiliSubscribeManager:

    def __init__(self, room_id: list[int]):
        self.room_ids = room_id
        self.status_dict = {r_id: 0 for r_id in room_id}
        self.content_dict = {r_id: None for r_id in room_id}
        self.need_notice = {r_id: False for r_id in room_id}

    def addOne(self, room_id:int):
        if room_id not in self.status_dict.keys():
            self.status_dict[room_id]=0
            self.content_dict[room_id] = None
            self.need_notice[room_id] = False

    def update(self):
        for r_id in self.room_ids:
            data = getBilibiliLiveStatus(str(r_id))
            self.content_dict[r_id] = data
            status = data["liveStatus"]
            if status == 1 and self.status_dict[r_id] in [0, 2]:
                self.need_notice[r_id] = True
            else:
                self.need_notice[r_id] = False
            self.status_dict[r_id] = status
        self.logStatus()

    def logStatus(self):
        rid = 2721650
        logger.warning(f"{rid} - {self.content_dict[rid]['title']} - {int(self.status_dict[rid])}")

    def query(self, room_id):
        if isinstance(room_id, str):
            room_id = int(room_id)
        if self.need_notice[room_id]:
            content = construct(self.content_dict[room_id])
            return content
        else:
            return None


if __name__ == '__main__':
    bm = BiliSubscribeManager([2721650])
    bm.update()
    print(bm.query(2721650))
