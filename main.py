import threading
import mindwave
import cv2
import time
import os
LOW_THRESHOLD_OPENCV = 2
# Anything 2 and under is considered not paying attention
LOW_THRESHOLD_MINDWAVE = 75
# Anything below 75 is considered not paying attention
STRICT_MODE = False
# False is basically (LOW_THRESHOLD_OPENCV OR LOW_THRESHOLD_MINDWAVE) and True is (LOW_THRESHOLD_OPENCV AND LOW_THRESHOLD_MINDWAVE)
try:
	headset = mindwave.Headset("/dev/rfcomm0")
	headset.connect()
except:
	pass
eye_detect_list = []

def get_rolling_average():
	print eye_detect_list
	if len(eye_detect_list) < 10:
		for i in range(10-len(eye_detect_list)):
			print("Inserting data for rolling average...")
			eye_detect_list.insert(0,3)
	return sum(eye_detect_list) / float(len(eye_detect_list))

def get_headset_attention():
	try:
		val = headset.attention
	except:
		val = 0
	return val

def score(opencvval, attentionval):
	if not (opencvval == 0 or attentionval == 0):
		# This means both values were grabbed correctly
		if (opencvval > LOW_THRESHOLD_OPENCV) and (attentionval > LOW_THRESHOLD_MINDWAVE):
			return True
		return False
	else:
		if (opencvval > LOW_THRESHOLD_OPENCV) or (attentionval > LOW_THRESHOLD_MINDWAVE):
			return True
		return False

def return_detect_count(frame):
	frame = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
	faces = cv2.CascadeClassifier('static/haarcascade_eye.xml')
	detected = faces.detectMultiScale(frame, 1.3, 5)
	return len(detected)

def start():
	# Sets ups Mindwave Headset
	cap = cv2.VideoCapture(0) 	#640,480
	w = 640
	h = 480
	e = 0
	while(cap.isOpened()):
	    ret, frame = cap.read()
	    if ret==True:
	    	opencvcount = return_detect_count(frame)
	    	eye_detect_list.append(opencvcount)
	    	if len(eye_detect_list) > 10:
		    	eye_detect_list.pop(0)
	    e += 1
	    if e % 15 == 0:
	    	if score(get_rolling_average(), get_headset_attention()):
	    		print("Score returned paying attention...")
	    		os.system("echo 1 > response.txt")
	    	else:
	    		print("Score returned not paying attention...")
	    		os.system("echo 0 > response.txt")

	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	start()
