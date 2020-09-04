import os
from flask import Flask,render_template,Response, make_response
from camera import VideoCamera


app=Flask(__name__)

# 测试服务
@app.route('/')
def servicehomepage():
    return 'this flask serverice is working'

# 播放本地视频（前端方法）
@app.route('/localvideo')
def localvideo():
    return render_template('localvideo.html')

# 播放网络视频（待定）
@app.route('/netvideo')
def cameravideo():
    return render_template('netvideo.html')

#相机推流
def gen(camera):
    while True:
        frame = camera.get_frame()
        # 使用generator函数输出视频流， 每次请求输出的content类型是image/jpeg
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

#相机喂流（不使用templates）
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

#相机喂流(使用templates)
@app.route('/cur_camera')
def cur_camera():
    return render_template('cur_camer.html')

if __name__ == '__main__':
    app.run(debug=True)