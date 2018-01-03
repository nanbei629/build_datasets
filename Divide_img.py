# -- coding: utf-8 --
import cv2
global img
global point1, point2
# 要截取的图片的大小
width =50
height =50
imgpath='img.jpg'
def on_mouse(event, x, y, flags, param):
    flag = 1
    global img, point1, point2,count
    img2 = img.copy()
    # while (flag):
    if event == cv2.EVENT_LBUTTONDOWN:  # 左键点击
        point1 = (x, y)
        cv2.circle(img2, point1, 10, (0, 255, 0), 5)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):  # 按住左键拖曳
        cv2.rectangle(img2, point1, (x, y), (255, 0, 0), 5)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_LBUTTONUP:  # 左键释放
        point2 = (x, y)
        cv2.rectangle(img2, point1, point2, (0, 0, 255), 5)
        cv2.imshow('image', img2)
        min_x = min(point1[0], point2[0])
        min_y = min(point1[1], point2[1])
        # width = abs(point1[0] - point2[0])
        # height = abs(point1[1] -point2[1])
        cut_img = img[min_y:min_y + width, min_x:min_x + height]
        cv2.imwrite('smaple\\%s_remote'%(count) + '.bmp', cut_img)
        count = count + 1
        print count
def main():
    global img,count
    count =2000
    img = cv2.imread(imgpath)
    cv2.namedWindow('image')
    # while(1):
    cv2.setMouseCallback('image', on_mouse)
    while(1):
        cv2.imshow('image', img)
        if (cv2.waitKey(0) == 27):
            break;
if __name__ == '__main__':
    main()