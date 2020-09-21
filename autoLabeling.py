import cv2
import numpy as np
from pyautogui import moveTo, screenshot, press, dragTo, write, hotkey
from time import sleep
import sys

# Enter what class the object you're detecting will be labeled as.
className = ''

# Change the modelConfig.cfg and modelWeights.weights to your own custom model config and weights path.
net = cv2.dnn.readNetFromDarknet('modelConfig.cfg', 'modelWeights.weights')
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


def findObjects(outputs, img):
    hT, wT, cT = img.shape
    bbox = []
    classIds = []
    confs = []

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > 0.5:
                w, h = int(detection[2] * wT), int(detection[3] * hT)
                x, y = int((detection[0]*wT) - (w / 2)), int((detection[1] * hT) - (h / 2))
                bbox.append([x,y,w,h])
                classIds.append(classId)
                confs.append(float(confidence))

    indices = cv2.dnn.NMSBoxes(bbox, confs, 0.5, 0.3)
    for i in indices:
        i = i[0]
        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        cv2.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), (0,0,255), thickness=2)
        return ((x,y), (x+w, y+h))
        

detectedFlag = False
while True:
    input('Press enter for next detection...')
    sleep(1)
    img = screenshot()
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)


    blob = cv2.dnn.blobFromImage(img, 1/255, (416,416), [0,0,0],crop=False)
    net.setInput(blob)

    layerNames = net.getLayerNames()
    outputNames = []
    for i in net.getUnconnectedOutLayers():
        outputNames.append(layerNames[i[0] - 1])
    outputs = net.forward(outputNames)
    
    prediction = findObjects(outputs, img)
    if prediction is not None and detectedFlag == False:
        detectedFlag = True
        pt1, pt2 = prediction
        print("Found " + className + " At " + str(pt1))
        x, y = pt1
        press('w')
        moveTo(x, y)

        x, y = pt2
        dragTo(x, y, duration=0.5)
        cv2.waitKey(50)
        write(className)
        press('enter', presses=2)
    hotkey('ctrl', 's')