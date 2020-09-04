# flask读取摄像头并实时显示
import cv2


class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        # 通过opencv获取实时视频流
        self.video = cv2.VideoCapture(0) #本机摄像头
        # If you decide to use video.mp4, you must have this file in the folder or net
        # as the main.py.
        # self.video = cv2.VideoCapture('path+video.mp4') #视频文件

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        # 因为opencv读取的图片并非jpeg格式，因此要用motion JPEG模式需要先将图片转码成jpg格式图片
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()