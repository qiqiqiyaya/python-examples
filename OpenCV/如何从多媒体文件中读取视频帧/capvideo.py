import cv2

cv2.namedWindow('video',cv2.WINDOW_NORMAL)
cv2.resizeWindow('video',640,480)

cap= cv2.VideoCapture("E:\\3-1 明晰课程项目【淘宝-资源库小店-整理】.mp4")
while True:
    # 从视频读取视频帧
    ret,frame= cap.read()

    cv2.imshow('video',frame)

    key= cv2.waitKey(40)
    if(key& 0xFF == ord('q')):
        break

cv2.destroyAllWindows()