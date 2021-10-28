import cv2
import numberplate
import time
class Car():
    def Car(self):
        car = numberplate.numberplate()
        cap = cv2.VideoCapture(0)
        plate_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

        while True:
            ret, frames = cap.read()
            gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
            plate = plate_cascade.detectMultiScale(gray, 1.1, 5)
            # if str(np.array(cars).shape[0]) == '1':
            #     i += 1
            #     continue
            for (x,y,w,h) in plate:
                plate = frames[y:y + h, x:x + w]
                cv2.rectangle(frames,(x,y),(x +w, y +h) ,(51 ,51,255),2)
                cv2.rectangle(frames, (x, y - 40), (x + w, y), (51,51,255), -2)
                cv2.putText(frames, 'plate', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                #cv2.imshow('plate',plate)
                print("plate found!")
                

            # lab1 = "Car Count: " + str(i)
            # cv2.putText(frames, lab1, (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (147, 20, 255), 3)
            frames = cv2.resize(frames,(600,400))
            #cv2.imshow('Car Detection System', frames)
            try:
                car.numberplate(plate)
                #time.sleep(1)
            except Exception as e:
                #print(e)
                TheMeaningToLife = 42
            
            #cv2.resizeWindow('Car Detection System', 600, 600)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                #break
                TheMeaningToLife = 42
        cv2.destroyAllWindows()