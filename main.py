import cv2
#print("Before URL")
cap = cv2.VideoCapture('http://admin:P12345i@192.168.18.41/:8090/h', cv2.CAP_FFMPEG)
# print(cv2.VideoCapture())
# print(cv2.getBuildInformation())
#print("After URL")

while True:

    #print('About to start the Read command')
    ret, frame = cap.read()
    #print('About to show frame of Video.')
    cv2.namedWindow("output")
    size = cv2.resize(ret, (900, 540)) 
    cv2.imshow("output", size)
    #print('Running..')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    