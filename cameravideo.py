# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 播放网络rtsp测试
import cv2
import threading


class Producer(threading.Thread):
    """docstring for ClassName"""

    def __init__(self, str_rtsp):
        super(Producer, self).__init__()
        self.str_rtsp = str_rtsp
        # 通过cv2中的类获取视频流操作对象cap
        self.cap = cv2.VideoCapture(self.str_rtsp)
        # 调用cv2方法获取cap的视频帧（帧：每秒多少张图片）
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        print(fps)
        # 获取cap视频流的每帧大小
        size = (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        print(size)
        # 定义编码格式mpge-4
        fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', '2')
        # 定义视频文件输入对象
        self.outVideo = cv2.VideoWriter('saveDir.avi', fourcc, fps, size)
        cv2.namedWindow("cap video", 0)

    def run(self):
        print('in producer')
        while True:
            ret, image = self.cap.read()
            if (ret == True):
                cv2.imshow('cap video', image)
                self.outVideo.write(image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.outVideo.release()
                self.cap.release()
                cv2.destroyAllWindows()
                break
                # continue


if __name__ == '__main__':
    print('run program')
    rtsp_str = 'rtmp://202.69.69.180:443/webcast/bshdlive-pc'
    # {rtmp测试地址（可用）
    # 香港卫视: rtmp://live.hkstv.hk.lxdns.com/live/hks1
    # 香港财经 rtmp://202.69.69.180:443/webcast/bshdlive-pc
    # 韩国GoodTV,rtmp://mobliestream.c3tv.com:554/live/goodtv.sdp
    # 韩国朝鲜日报,rtmp://live.chosun.gscdn.com/live/tvchosun1.stream
    # 美国1,rtmp://ns8.indexforce.com/home/mystream
    # 美国2,rtmp://media3.scctv.net/live/scctv_800
    # 美国中文电视,rtmp://media3.sinovision.net:1935/live/livestream
    # 湖南卫视 rtmp://58.200.131.2:1935/livetv/hunantv}
    producer = Producer(rtsp_str)
    producer.start()