# import the necessary packages
import cv2
import numpy as np
import scipy
import scipy.ndimage
 
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False

def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping
 
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
 
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        cropping = False
 
    # draw a rectangle around the region of interest
    cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
    cv2.imshow("image", image)
    cv2.waitKey()
    

if __name__ == '__main__':
    image = cv2.imread('cracks.jpg', cv2.COLOR_BGR2GRAY)

    # tomar canal azul y aplicar filtro
    b, g, r = cv2.split(image)

    #image = b
    
    image_channel = cv2.medianBlur(b, 5)
    
    # aplicar threshold
    image_channel = cv2.adaptiveThreshold(image_channel, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite('binary_image.jpg', image_channel)
    image = cv2.imread('binary_image.jpg')
    clone = image_channel.copy()


    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)

    # keep looping until the 'q' key is pressed
    while True:
        # display the image and wait for a keypress
        cv2.imshow("image", image_channel)
        key = cv2.waitKey(0) & 0xFF
 
        # if the 'r' key is pressed, reset the cropping region
        if key == ord("r"):
             image_channel = clone.copy()
 
        # if the 'c' key is pressed, break from the loop
        elif key == ord("c"):
            break
 
    # if there are two reference points, then crop the region of interest
    # from teh image and display it
    if len(refPt) == 2:
        roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
        cv2.imwrite('roi.jpg', roi)
        cv2.imshow("ROI", roi)
        cv2.waitKey(0)
 
    # close all open windows
    cv2.destroyAllWindows()
        
    # struct compuesto por una matriz de 2 dimensiones y conectividad 2
#    struct = scipy.ndimage.morphology.generate_binary_structure(2, 4)
#    erosion = scipy.ndimage.morphology.binary_erosion(roi, structure=struct,\
#                iterations=1).astype(roi.dtype)
#    for i in range(len(erosion)):
#        for j in range (len(erosion[1])):
#            if erosion[i][j] == 1:
#                erosion[i][j] = 255

    erosion = cv2.medianBlur(roi, 5)
    cv2.imwrite('blur.jpg', erosion)
    
    struct = scipy.ndimage.morphology.generate_binary_structure(2, 4)
    erosion = scipy.ndimage.morphology.binary_erosion(roi, structure=struct,\
                iterations=1).astype(roi.dtype)
    for i in range(len(erosion)):
        for j in range (len(erosion[1])):
            if erosion[i][j] == 1:
                erosion[i][j] = 255
    cv2.imwrite('erosion.jpg', erosion)
    
    
    # calcula contorno de todos los blobs, se usa para calcular sus perimetros
    im2, contours, hierarchy = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    perimetro = []

    # se guardan los perimetros de todos los blobs en una lista
    for i in range(len(contours)):
        cnt = contours[i]
        perimetro.append(cv2.arcLength(cnt,True))
    
    
#    cv2.drawContours(im2, contours, -1, 0, 1)
#    cv2.imwrite("contours.jpg", im2)

    connectivity = 8
    output = cv2.connectedComponentsWithStats(erosion, connectivity,\
                cv2.CV_32S)
    # Get the results
    # The first cell is the number of labels
    num_labels = output[0]
    # The second cell is the label matrix
    labels = output[1]
    # The third cell is the stat matrix
    stats = output[2]
    # The fourth cell is the centroid matrix
    centroids = output[3]

#    avg_area = 0
#    
#    for label in range(num_labels):
#        avg_area += stats[label, cv2.CC_STAT_AREA]
#        
#    avg_area = avg_area/num_labels
#        
#    for i in range(len(labels)):
#        for j in range (len(labels[1])):
#            if labels[i][j] > 0:
#                labels[i][j] = 255
#    cv2.imwrite('labels.jpg', labels)
#
#    for label in range(num_labels):
#        if stats[label, cv2.CC_STAT_AREA] < avg_area:
#            for i in range(len(labels)):
#                for j in range (len(labels[1])):
#                    if labels[i][j] == label:
#                        labels[i][j] = 255
#
#    cv2.imwrite('labels2.jpg', labels)