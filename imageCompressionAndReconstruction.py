'''
	Name: Stephen Odero 
	Reg. No: F17/81917/2017
	Program: imageCompressionAndResonctruction.py
	Description: The program is intended to capture images using fswebcam after an interval of 15 seconds
				 Within the intervals, the captured image is compressed, stored in a different directory
				 Transmitted to the PC and the original image is deleted
				 The compression used is from PIL which uses convolution to compress the images.
'''


#importing necessary libraries
import os					#to handle directories and files
from time import sleep		#to implement delay in capturing image
from PIL import Image		#for image manipulation

#Getting current working directory 
myDirectory=os.getcwd()
#Cheching whether the directory already exists, if not, create the directory

if not os.path.exists('capturedImages'):
	#creating a directory to store captured images
	os.mkdir('capturedImages')

if not os.path.exists('compressedImages'):
	#creating a directory to store the compressed images. 
	os.mkdir('compressedImages')

'''
	function to capture images at a resolution of 1280 by 720 pixels at an interval of 15 seconds and store
	the captured image in the capturedImages file. 
'''
def imageCapture():
	os.system('fswebcam -r 1280x720 --no-banner --save /home/pi/Documents/project/capturedImages/%H%M%S.jpg')
	#time.sleep(15)

#function to open file
def imageCompression(directory=False):
	'''
		if the program is run on a different directory, then change to the directory 
	'''
	if directory:
		os.chdir(myDirectory+'/capturedImages')
	#Obtaining images in current directory
	myFiles=os.listdir(os.getcwd())
	myImages=[file for file in myFiles if file.endswith('.jpg')] # list comprehension

	#Going through the entire directory and compressing all images.
	for image in myImages:
		compressedImage=Image.open(image)
		'''
			saving the compressed image with a new name and storing it in compressed folder
		'''
		compressedImage.save(myDirectory+'/compressedImages/{}'.format('compressed'+image),optimize=True, quality=30)	

#Implementing the code
while True: 
	imageCapture()
	capturedImagesDirectory=os.getcwd()+'/capturedImages'
	imageCompression(directory=capturedImagesDirectory)
	'''
		Delay of 10 seconds to allow for compression and transmission before 
		the next image is captured. 
	'''
	time.sleep(10)
