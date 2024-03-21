import cv2
# import pickle 

image = cv2.imread('resources/photos/car slot.png')
slot_width = 89
slot_height = 39
positionList = [ ]

def mouseClick(event,x,y,flags,params):
    if event ==  cv2.EVENT_LBUTTONDOWN:
        positionList.append((x,y))

print(positionList)

while True:
    # cv2.rectangle(image,(35,200),(124,239),(0,0,255),2)
    for pos in positionList:
        cv2.rectangle(image , pos,(pos[1] + slot_width,pos[0] + slot_height),(0,0,255),2)
        print(pos[1])
    cv2.imshow("Packing",image)
    cv2.setMouseCallback("Packing",mouseClick)
    cv2.waitKey(0)
    