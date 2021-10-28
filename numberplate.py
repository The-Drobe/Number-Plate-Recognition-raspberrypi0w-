import numpy as np
import cv2
import imutils
import sys
import pytesseract
import pandas as pd
import time


class numberplate:
        def numberplate(self, img):
                #image = cv2.imread('Vehicle-Number-Plate-Reading-master\\car.jpeg')
                image = img 
                #image = imutils.resize(image, width=500)

               # cv2.imshow("Original Image", image)

                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                #cv2.imshow("1 - Grayscale Conversion", gray)

                # gray = cv2.bilateralFilter(gray, 11, 17, 17)
                # cv2.imshow("2 - Bilateral Filter", gray)

                gray = cv2.GaussianBlur(gray, (3,3), 0)
                #cv2.imshow("3 - GaussianBlur", gray)

                gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
                #cv2.imshow("threshold", gray)

                # Morph open to remove noise and invert image
                kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
                opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel, iterations=1)
                gray = 255 - opening
               # cv2.imshow("invert", gray)

                edged = cv2.Canny(gray, 170, 200)
                #cv2.imshow("4 - Canny Edges", edged)

                cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                cnts = imutils.grab_contours(cnts)
                cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10] 
                NumberPlateCnt = None 

                count = 0
                for c in cnts:
                        peri = cv2.arcLength(c, True)
                        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
                        if len(approx) == 4:  
                                NumberPlateCnt = approx 
                                break

                # Masking the part other than the number plate
                # gray = np.zeros(gray.shape,np.uint8)
                # cv2.imshow("Final_image",gray)
                try:
                        #new_image = cv2.drawContours(mask,[NumberPlateCnt],0,255,-1)
                        #new_image = cv2.drawContours(gray,[NumberPlateCnt],0,255,-1)
                        #new_image = cv2.bitwise_and(image,image,mask=mask)
                        #new_image = cv2.bitwise_and(image,image,mask=gray)
                        #cv2.namedWindow("Final_image",cv2.WINDOW_NORMAL)
                        #cv2.imshow("Final_image",new_image)
                        # Configuration for tesseract
                        config = ('-l eng --oem 3 --psm 7')

                        # Run tesseract OCR on image
                        text = pytesseract.image_to_string(image, config=config)

                        #check that if it has deteted nothing i.e. this character 
                        text = text.replace("","")
                        text = text.strip()
                        if (text != ""):
                                #Data is stored in CSV file
                                raw_data = {'date': [time.asctime( time.localtime(time.time()) )], 
                                        'v_number': [text] }

                                df = pd.DataFrame(raw_data, columns = ['date', 'v_number'])
                                df.to_csv('data.csv', mode='a', header=False)

                                # Print recognized text
                                print("number plate is:")
                                print(text)
                                hs = open("licence.txt","a")
                                hs.write(text + "\n")
                                hs.close() 
                except Exception as e:
                        #print(e)
                        TheMeaningToLife = 42

                # cv2.waitKey(0)

# image = cv2.imread('Vehicle-Number-Plate-Reading-master\\car.jpeg')
# a = numberplate()
# a.numberplate(image)
