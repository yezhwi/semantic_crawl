# -*- coding: utf-8 -*-

import time
import re
from crawl_selected.utils.string_util import *


class TimeUtils(object):

    defualt_time_formats = ["%Y-%m-%d %H:%M:%S",
                           "%Y-%m-%d %H:%M",
                           "%Y-%m-%d",
                           "%Y/%m/%d",
                           "%Y.%m.%d",
                           "%Y年%m月%d日 %H:%M:%S",
                           "%Y年%m月%d日 %H:%M",
                           "%Y年%m月%d日",
                           "%Y年%m月%d日%H:%M",
                           "%Y年%m月%d日%H时%M分",
                           "%Y年%m月%d日%H时%M分%S秒",
                           "%Y年%m月%d日 %H时%M分",
                            "%Y年%m月%d日 %H时%M分%S秒",]

    @classmethod
    def convert2Mill4Format(cls,timeStr, format):
        try:
            return int(time.mktime(time.strptime(timeStr, format)) * 1000)
        except ValueError as e:
            return None

    @classmethod
    def convert2Mill4Default(cls, timeStr, format):
        result = None
        if StringUtils.isNotEmpty(format) and "pre_time" == format:
            result = TimeUtils.convert2Mill(timeStr)
        if result is not None:
            return result
        if StringUtils.isNotEmpty(format):
            if len(timeStr) < 10 and "-" in timeStr:
                timeStr = "20"+timeStr
            result = TimeUtils.convert2Mill4Format(timeStr,format)
        if result is not None:
            return result
        for timeFormat in TimeUtils.defualt_time_formats:
            result = TimeUtils.convert2Mill4Format(timeStr, timeFormat)
            if result is not None:
                return result
        if "小时" in timeStr or "天" in timeStr or "分" in timeStr:
            return TimeUtils.convert2Mill(timeStr)
        return None


    @classmethod
    def convert2Mill(cls, timeStr):
        number = re.search(u'(\d+)',timeStr).group()
        numberInt = 0
        if number is not None and len(number)>0:
            numberInt = int(number)
        if u"小时" in timeStr:
            numberInt = numberInt*3600*1000
        elif u"分" in timeStr:
            numberInt = numberInt*60*1000
        elif u"天" in timeStr:
            numberInt = numberInt*24*3600*1000

        now = TimeUtils.getNowMill()
        return now - numberInt

    @classmethod
    def getNowMill(cls):
            return int(time.time()*1000)