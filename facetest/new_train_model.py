#! /usr/bin/python

# import the necessary packages
from imutils import paths
import face_recognition
#import argparse
import pickle
import cv2
import os

def trainHere():
	# our images are located in the dataset folder
	print("[INFO] start processing faces...")
	imagePaths = list(paths.list_images("dataset"))

	#load pickle file
	data=[]
	with (open("encodings.pickle", "rb")) as fr:
		while True:
			try:
				data.append(pickle.load(fr))
			except EOFError:
				break

	# initialize the list of known encodings and known names
	try:
		knownEncodings = data[0]['encodings']
		knownNames = data[0]['names']
	except:
		knownEncodings=[]
		knownNames=[]
	pastName =  False

	# loop over the image paths
	for (i, imagePath) in enumerate(imagePaths):
		# extract the person name from the image path
		print("[INFO] processing image {}/{}".format(i + 1,
			len(imagePaths)))
		name = imagePath.split(os.path.sep)[-2]

		#check if name already exist
		for x in knownNames:
			if x == name:
				pastName = True
				break
		
		if pastName == True:
			pastName = False
			continue

		# load the input image and convert it from RGB (OpenCV ordering)
		# to dlib ordering (RGB)
		image = cv2.imread(imagePath)
		rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		# detect the (x, y)-coordinates of the bounding boxes
		# corresponding to each face in the input image
		boxes = face_recognition.face_locations(rgb,
			model="hog")

		# compute the facial embedding for the face
		encodings = face_recognition.face_encodings(rgb, boxes)

		# loop over the encodings
		for encoding in encodings:
			# add each encoding + name to our set of known names and
			# encodings
			knownEncodings.append(encoding)
			knownNames.append(name)
	
	# dump the facial encodings + names to disk
	print("[INFO] serializing encodings...")
	data = {"encodings": knownEncodings, "names": knownNames}
	f=open("encodings.pickle", "wb")
	f.write(pickle.dumps(data))
	f.close()

def train():
	# our images are located in the dataset folder
	print("[INFO] start processing faces...")
	imagePaths = list(paths.list_images("facetest/dataset"))

	#load pickle file
	data=[]
	try:
		with (open("facetest/encodings.pickle", "rb")) as fr:
			while True:
				try:
					data.append(pickle.load(fr))
				except EOFError:
					break
	except FileNotFoundError:
		x=open("encodings.pickle", "x")
		x.close()

	# initialize the list of known encodings and known names
	try:
		knownEncodings = data[0]['encodings']
		knownNames = data[0]['names']
	except:
		knownEncodings=[]
		knownNames=[]
	pastName =  False
	oldName = ""

	# loop over the image paths
	for (i, imagePath) in enumerate(imagePaths):
		# extract the person name from the image path
		print("[INFO] processing image {}/{}".format(i + 1,
			len(imagePaths)))
		name = imagePath.split(os.path.sep)[-2]

		#check if name already exist
		for x in knownNames:
			if name == oldName:
				print(name)
				break
			elif x == name:
				print("Known Name")
				pastName = True
				break
			else:
				print("New name")
				oldName = name
		if len(knownNames) == 0:
			oldName = name
				
		if pastName == True:
			pastName = False
			continue

		# load the input image and convert it from RGB (OpenCV ordering)
		# to dlib ordering (RGB)
		image = cv2.imread(imagePath)
		rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		# detect the (x, y)-coordinates of the bounding boxes
		# corresponding to each face in the input image
		boxes = face_recognition.face_locations(rgb,
			model="hog")

		# compute the facial embedding for the face
		encodings = face_recognition.face_encodings(rgb, boxes)

		# loop over the encodings
		for encoding in encodings:
			# add each encoding + name to our set of known names and
			# encodings
			knownEncodings.append(encoding)
			knownNames.append(name)

	# dump the facial encodings + names to disk
	print("[INFO] serializing encodings...")
	data = {"encodings": knownEncodings, "names": knownNames}
	f=open("facetest/encodings.pickle", "wb")
	f.write(pickle.dumps(data))
	f.close()

#trainHere()
