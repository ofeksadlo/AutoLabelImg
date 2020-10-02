import cv2
import numpy as np
from mss import mss
import os


def detectAndWriteTxt(filename):
    frame = cv2.imread(filename)
    blob = cv2.dnn.blobFromImage(frame, 1/255, (416,416),[0,0,0],1,crop=False)

    net.setInput(blob)
    layerNames = net.getLayerNames()
    outputNames = [layerNames[i[0]-1] for i in net.getUnconnectedOutLayers()]

    outputs = net.forward(outputNames)

    hT, wT, cT = frame.shape

    detectionsBoxes = []
    bbox = []
    classIds = []
    confs = []
    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > 0.8:
                detectionsBoxes.append([det[0], det[1], det[2], det[3]])
                w, h = int(det[2] * wT), int(det[3] * hT)
                x, y = int(det[0] * wT - (w/2)), int(det[1] * hT - (h/2))
                bbox.append([x,y,w,h])
                classIds.append(classId)
                confs.append(float(confidence))
    indices = cv2.dnn.NMSBoxes(bbox, confs, 0.8, 0.3)
    for i in indices:
        i = i[0]
        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        det = detectionsBoxes[i]
        f = open(filename.split('.')[0] + '.txt', 'a')
        f.write(str(classIds[i]) + ' ' + str(det[0]) + ' ' + str(det[1]) + ' ' + str(det[2]) + ' ' + str(det[3])+'\n')
        f.close()


classNames = ["hand"]


net = cv2.dnn.readNetFromDarknet('yolov4-obj.cfg', 'yolov4-obj_final.weights')
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


filepath = 'test'

if os.path.exists(filepath + '/' + 'classes.txt') == False:
    for name in classNames:
        with open(filepath + '/classes.txt', 'a') as f:
            f.write(name+'\n')

print(os.listdir(filepath))
for item in os.listdir(filepath):
    filetype = item.split('.')[1]
    if filetype == 'jpg' or filetype == 'png' or filetype == 'jpeg':
        detectAndWriteTxt(filepath + '/'+ item)
# sct = mss()

# monitor = {"top": 0, "left": 0, "width": 1920, "height:": 1080}

# while True:
#     frame = sct.grab(monitor)
#     frame = cv2.cvtColor(np.array(frame), cv2.COLOR_RGBA2RGB)



# img = cv2.imread('New Folder/frame.png')
# img = cv2.resize(img, (416,416))
# cv2.imwrite('newFrame.png', img)