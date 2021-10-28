#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/14 16:04
# @File    : 5jiaoben.py
# @Function:

from pydub import AudioSegment

path =r'E:\办公\服务端\服务端测试工具\it公司测试工具\test_tool_0928\iat_ws_python3_demo\test\iat01db3a7f@ch03930c8a9a1f47b400.pcm'

video = AudioSegment.from_mp3(path).set_frame_rate(16000)
video.export(path,format='pcm',bitrate='16k')
