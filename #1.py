import cv2 as cv
import numpy as np

def video_demo():
    capture = cv.VideoCapture(0)
    while(True):
        ret,frame = capture.read()
        cv.imshow("video",frame)
        c= cv.waitKey(50)
        if c==27:
            break


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)


src = cv.imread("./example_images/example.png")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
get_image_info(src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imwrite("./example_images/result.png", gray)


# video_demo()
cv.waitKey(0)


cv.destroyAllWindows()

