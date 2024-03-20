import cv2
import pandas as pd
from ultralytics import YOLO
import numpy as np
from paddleocr import PaddleOCR,draw_ocr
ocr=PaddleOCR(use_angle_cls=True,lang='en')

model = YOLO("/home/sukrit/Downloads/helmet_det/best.pt")
output_dir = ("/")

def take_inp(address):
    img=cv2.imread(address)    
    return img
target_index=3
def check_helmet(img):
    result = model.predict(source=img,task="detect")
    if (1 in (result[0].boxes.cls)):
        for box in result[0].boxes:
            if box.cls == target_index:  # Check if the class index matches the target class
                x1, y1, x2, y2 = box.xyxy.tolist()[0] # Extract the bounding box coordinates      
                print(f"Found {model.model.names[target_index]} at ({x1},{y1}), ({x2},{y2})")
                return (x1,y1,x2,y2,img)

def perform_ocr(x1,y1,x2,y2,img):
    x1 = int(max(0, x1))
    y1 = int(max(0, y1))
    x2 = int(min(x2, img.shape[1]))
    y2 = int(min(y2, img.shape[0]))

    # Crop the image using NumPy array slicing
    crop = img[y1:y2, x1:x2]
    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    gray = cv2.bilateralFilter(gray, 10, 25, 20)
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    im = cv2.filter2D(gray, -1, kernel)

    # if crop.size > 0:
    #     # Display the cropped image
    #     #cv2.imshow(gray)
    #     cv2.imshow('im', im)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
    # else:
    #     print("Invalid bounding box coordinates")

    #cv2.imwrite('/content/drive/MyDrive/Final_helmet_detection/croppedimg/crop.jpg',im)
    result = ocr.ocr(im, cls=True)
    print(result[0][0][1][0])
    fin=result[0][0][1][0]
    return(fin)

perform_ocr(*check_helmet(take_inp("/home/sukrit/Downloads/helmet_det/72.png")))