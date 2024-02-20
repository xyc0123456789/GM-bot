# -*- coding: utf-8 -*-
import datetime
import time


def get_offset_time(days=0, hours=0, mins=0, seconds=0):
    current_datetime = datetime.datetime.now()
    tomorrow_datetime = current_datetime + datetime.timedelta(days=days, hours=hours, minutes=mins, seconds=seconds)
    return tomorrow_datetime.timestamp()


def get_timestamp(tStp, format="%Y-%m-%d %H:%M:%S"):
    dt_obj = datetime.datetime.fromtimestamp(tStp)
    formatted_date = dt_obj.strftime(format)
    return formatted_date
