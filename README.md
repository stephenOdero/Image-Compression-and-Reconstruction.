# Image-Compression-and-Reconstruction.
The program aims at compressing images captured using a Webcam by a Raspberry Pi 4 B. 
The python modules used include PIL (Python Imaging Library) and OS. 
The image is captured, stored in a directory that is created (if it does not exists) compressed and the compressed version stored in a 
separate directory (If the directory is not present) 
The final compressed images stored in the compressed images directory can be transferred over SCP from the Raspberry PI to the local machine
using the command
  scp -r currentDirectory hostNameToTransferTo
  
  
