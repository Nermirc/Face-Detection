import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpFaceDetection = mp.solutions.face_detection
FaceDetection = mpFaceDetection.FaceDetection(0.2)

mpDraw = mp.solutions.drawing_utils
while True:
        success,img = cap.read()
        if not cap.isOpened():
            print("Goruntuleme basarisiz")
            break
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        results = FaceDetection.process(imgRGB)
        
        #print(results.detections)
        if results.detections:
            for id , detection in enumerate(results.detections):
                bboxC = detection.location_data.relative_bounding_box
                print(bboxC)
                h, w , _ = img.shape
                bbox = int(bboxC.xmin*w), int(bboxC.ymin*h), int(bboxC.width*w),int(bboxC.height*h )
                cv2.rectangle(img,bbox,(0,255,0),2)        
                
                #İsim yazdırma
                cv2.putText(img,"Serap",(bbox[0],bbox[1]-10), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)    
                cv2.putText(img, "21", (bbox[0], bbox[1] + bbox[3] + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("img",img)
        cv2.waitKey(20)