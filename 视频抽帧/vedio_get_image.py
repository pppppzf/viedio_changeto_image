import cv2
import matplotlib.pyplot as plt

# 打开一个视频文件
video = cv2.VideoCapture("./") #此处输入视频地址
# 读取一帧
ret, frame = video.read()

plt.imshow(frame)

plt.imshow(cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2BGR))

video = cv2.VideoCapture("") # 引号内输入地址
num = 0 # 计数器
save_step =30 
while True:
    ret, frame = video.read()
    if not ret:
        break
    num +=1
    if num % save_step == 0:
        cv2.imwrite("" + str(num) + ".jpg",frame) #第一个引号写视频转换为图片的输出地址
