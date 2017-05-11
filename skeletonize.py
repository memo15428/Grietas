import cv2
import numpy as np

def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray,(3,3),0)
    detected_edges = cv2.Canny(detected_edges,lowThreshold,lowThreshold*ratio,apertureSize = kernel_size)
    dst = cv2.bitwise_and(lap_image,lap_image,mask = detected_edges)  # just add some colours to edges from original image.
    cv2.imshow('canny demo',dst)

if __name__ == '__main__':
    scale = 1
    delta = 0
    # ddepth = cv2.CV_64F
    
    img = cv2.imread('cracks.jpg')
    img = cv2.GaussianBlur(img,(3,3),0)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    # Gradient-X
    grad_x = cv2.Sobel(gray,-1,1,0,ksize = 3, scale = scale, delta = delta,borderType = cv2.BORDER_DEFAULT)
    #grad_x = cv2.Scharr(gray,ddepth,1,0)
    
    # Gradient-Y
    grad_y = cv2.Sobel(gray,-1,1,0,ksize = 3, scale = scale, delta = delta, borderType = cv2.BORDER_DEFAULT)
    #grad_y = cv2.Scharr(gray,ddepth,0,1)
    
    abs_grad_x = cv2.convertScaleAbs(grad_x)   # converting back to uint8
    abs_grad_y = cv2.convertScaleAbs(grad_y)
    
    sobel_img = cv2.addWeighted(abs_grad_x,0.5,abs_grad_y,0.5,0)
    # sobel_img = cv2.add(abs_grad_x,abs_grad_y)
    
    cv2.imshow('Sobel demo',sobel_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    # aplicamos scharr filter
    grad_x = cv2.Scharr(sobel_img,-1,1,0)
    grad_y = cv2.Scharr(sobel_img,-1,0,1)
    
    abs_grad_x = cv2.convertScaleAbs(grad_x)   # converting back to uint8
    abs_grad_y = cv2.convertScaleAbs(grad_y)
    
    scharr_img = cv2.add(abs_grad_x,abs_grad_y)
    
    cv2.imshow('Scharr demo',scharr_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()





    # laplacian operator
    kernel_size = 3
    
    gray_lap = cv2.Laplacian(scharr_img,-1,ksize = kernel_size,scale = scale,delta = delta)
    lap_image = cv2.convertScaleAbs(gray_lap)
    
    
    lowThreshold = 0
    max_lowThreshold = 100
    ratio = 3
    
    img = cv2.imread('cracks.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    cv2.namedWindow('canny demo')
    
    cv2.createTrackbar('Min threshold','canny demo',lowThreshold, max_lowThreshold, CannyThreshold)
    
    CannyThreshold(0)  # initialization
    if cv2.waitKey(0) == 27:
        cv2.destroyAllWindows()
    
    
    cv2.imshow('scharr_img',scharr_img)
    cv2.imshow('sobel_img',sobel_img)
    cv2.imshow('laplacian',lap_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()