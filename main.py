import numpy as np
import cv2
import random
import csv

LEARNING_RATE = 0.1
DISCOUNT = 0.95
EPISODES = 2000

image_in = cv2.imread('smile_test.png')                     #import image           (form of every pixel  [255, 255, 255] or [0, 0, 0]
image_out = np.ones( ( image_in.shape ),np.uint8)*255      #declaration  output image
image_in_array = np.zeros(image_in.shape)                   #declaration input array to have the image in another form (easier to work with)     black->1   white->0
image_out_array = np.zeros(image_in.shape)                  #declaration output array to have the image in another form (easier to change the value of pixels)     black->1   white->0
a = []
c = []
for y_pixel in range(0, image_in.shape[1]):
    for x_pixel in range(0, image_in.shape[0]):
        if all(image_in[x_pixel, y_pixel]) == True:
            image_in_array[x_pixel, y_pixel] = 0               #transform image to array           1 means black   0 means white
        else:
            image_in_array[x_pixel, y_pixel] = 1

            a.append(x_pixel)
            c = c + [[x_pixel, y_pixel]]
idx = a.index(max(a))
b = max(a)
# print(idx)
# print(c[idx])
cv2.imshow("input image", image_in)
x_pixel = (c[idx])[0]
y_pixel = (c[idx])[1]
which_action = random.randrange(1, 5, 1)

for i in range(0, 20):

    matrix_3x3 = [
                  [image_in_array[x_pixel-1][y_pixel-1], image_in_array[x_pixel][y_pixel-1], image_in_array[x_pixel+1][y_pixel-1]],
                  [image_in_array[x_pixel-1][y_pixel], image_in_array[x_pixel][y_pixel], image_in_array[x_pixel+1][y_pixel]],
                  [image_in_array[x_pixel-1][y_pixel+1], image_in_array[x_pixel][y_pixel+1], image_in_array[x_pixel+1][y_pixel+1]]
                 ]

    image_out_array[x_pixel][y_pixel]=1
    x1 = np.argmax(matrix_3x3)
    if x1==1:
        which_action = 1
    elif x1==5:
        which_action = 2
    elif x1==7:
        which_action = 3
    elif x1 ==3:
        which_action = 4
    else:
        which_action = random.randrange(1, 5, 1)

    if which_action == 1:
        y_pixel = y_pixel - 1
    elif which_action == 2:
        x_pixel = x_pixel + 1
    elif which_action == 3:
        y_pixel = y_pixel + 1
    elif which_action == 4:
        x_pixel = x_pixel - 1



d=[]
for y_pixel in range(0, image_out_array.shape[1]):              #transform array to image       1->[0, 0, 0]    0->[255, 255, 255]
    for x_pixel in range(0, image_out_array.shape[0]):
        if all(image_out_array[x_pixel, y_pixel]) == True:
            image_out[x_pixel, y_pixel] = [0, 0, 0]
            d = d + [[x_pixel, y_pixel]]
            print(d[-1])
            with open('main.csv', 'w') as file:
                writer = csv.writer(file, lineterminator='\n')
                writer.writerows(d)



        else:
            image_out[x_pixel, y_pixel] = [255, 255, 255]

cv2.imshow("output image", image_out)                          #displaying out image

font = cv2.FONT_HERSHEY_SIMPLEX                                # text property
bottomLeftCornerOfText = (5, 5)
fontScale = 2
fontColor = (255, 255, 255)
lineType = 3


q_table = np.random.randint(-100, 100, [256, 8])            #temporary declaration of table to Qlearning

cv2.putText(image_in, 'before Qlearning', bottomLeftCornerOfText, font, fontScale, fontColor, lineType)
cv2.putText(image_out, 'After ... epochs' , bottomLeftCornerOfText, font, fontScale, fontColor, lineType)
cv2.waitKey()
