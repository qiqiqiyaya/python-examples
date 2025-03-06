import cv2

# 创建video writer 为多媒体文件
fourcc = cv2.VideoWriter.fourcc(*"mp4v")
# 输出1920*1080，24帧的视频
vw = cv2.VideoWriter("./out.mp4", fourcc, 24, (1920, 1080))

# 创建窗口
cv2.namedWindow("video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("video", 640, 360)

# 从视频文件中读取视频帧
cap = cv2.VideoCapture("E:\\3-1 明晰课程项目【淘宝-资源库小店-整理】.mp4")

while True:
    # 从cap对象读视频帧
    ret, frame = cap.read()

    # 将视频帧在窗口中显示
    cv2.imshow("video", frame)
    # 写数据到多媒体文件
    vw.write(frame)

    # 等待键盘事件，如果为q，退出
    key = cv2.waitKey(1)
    if key & 0xFF == ord("q"):
        break

# 释放VideoCapture
cap.release()
vw.release()
cv2.destroyAllWindows()
