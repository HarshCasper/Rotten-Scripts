import numpy as np
import cv2
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from scipy import signal
from PIL import ImageFilter
from skimage import feature


np.set_printoptions(threshold=np.nan)
#filt runs a filter on the image and returns array of endpoints
#argument is the image
def filt(image):
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

	edges = findSigma(gray)
	edges = edges.astype('uint8')
	
	#plt.imshow(edges, 'Greys')
	#plt.show()

	#######hough lines#############
	minLine = 1000
	maxGap = 100
	segs = cv2.HoughLinesP(edges,8,np.pi/180,100,minLine,maxGap,75)

	####find the vertical segments with a low tolerance####
	vertSegs = vertical(image)
	vertSegs = findVert(vertSegs)
	segs = segs[0,:,:]

	if (len(vertSegs.shape)>1):
		segs =np.concatenate((segs,vertSegs),axis=0)
	
	return segs

#segfinds will make sure lines are desired length
#argument is the array of endpoints and the image
def segFind(segs,image):

	minSeg = (len(image)+len(image[0]))/80 ###this is the minimum line segment based on size of image
	
	###distance formula to find long-ish segments####
	i=-1
	for x1,y1,x2,y2 in segs:
		i=i+1
		dist = np.sqrt((x2-x1)**2 + (y2-y1)**2)

		#random tolerance for now... seems to produce good segments
		if dist<minSeg:
			segs[i]=0

	return segs

#this function finds a suitable sigma (tolerance) for the canny edge detector
#argument is the image
def findSigma(image):
	sig = 3.5
	total = len(image)*len(image[0])
	flag = True
	cnt = 0
	while(flag):
		cnt = cnt+1
		edges = feature.canny(image, sigma=sig)

		edSum = np.sum(edges)
		tmp = total/edSum
		print sig
		print tmp
		###if there are too many pixels, increase sig
		if tmp<200:
			sig = sig + .13
		###too few pixels, decr sig
		if tmp>500:
			sig = sig - .13
		elif tmp>200 and tmp <500:
			return edges

		##sometimes any sigma we put in will be incorct so we let feature decide after some trying
		elif cnt>10 and tmp == 0:
			edges = feature.canny(image)
			return edges

		elif cnt>50:
			edges = feature.canny(image)
			plt.imshow(edges)
			plt.show()
			return edges

#this draws the line segments on the image
#arguments are the image and the array of line segment endpoints
def draw(image, segs, objs):

	if ((len(segs.shape)) == 2):
		for i in range(len(segs)):
			x1=segs[i,0]
			y1=segs[i,1]
			x2=segs[i,2]
			y2=segs[i,3]
			cv2.line(image,(x1,y1),(x2,y2),objs[i].color,5)

	if ((len(segs.shape)) == 1):
		for i in range(len(segs)):
			x1=segs[0]
			y1=segs[1]
			x2=segs[2]
			y2=segs[3]
			cv2.line(image,(x1,y1),(x2,y2),(255,0,0),5)

	return image


def profile(segs,imNum):

	objs = []

	for i in range(len(segs)):
		objs.append(Segment(segs[1],imNum))

		##calc length of seg
		dist = np.sqrt((segs[i,2]-segs[i,0])**2 + (segs[i,3]-segs[i,1])**2)
		objs[i].setDistance(dist)

		##slope of line####
		rise = float(segs[i,3]-segs[i,1])
		run = float(segs[i,2] - segs[i,0])
		if run == 0:
			slope = 100000 ###vertical line if run == 0
		elif (run != 0):
			slope = float(rise/run)
		print rise,'/',run,' = ',slope

		objs[i].setSlope(slope)

		###for now lets set the color based on the slope of the line
		color = colorFind(slope)
		objs[i].setColor(color)

	return objs

def colorFind(slope):
	color = (250,0,0)

	if slope > .5 and slope <1:
		color = (0,255,0)

	if slope >= 1 and slope <2:
		color = (160,32,240)

	if slope <= .5 and slope >0:
		color = (0,0,255)

	if slope < 0.0 and slope > -1.3:
		color = (255,255,0)

	if slope >-1.3 and slope <-2.0:
		color = (255,50,150)

	if slope > 8:
		color = (0,255,255)

	if slope > -.2 and slope < .2:
		color = (255,165,0)

	if slope <-2:
		color = (255,0,255)

	return color


###finds vertical lines with a very low tolerance
def vertical(image):
	image = np.asarray(image)
	image = image[:,:,0]
	edges = feature.canny(image)
	edges = edges.astype('uint8')
	#plt.imshow(edges)
	#plt.show()

	vertSeg = cv2.HoughLinesP(edges, 1, np.pi/180, 2, None, 25, 1);

	return vertSeg

###finds all vertical segments by finding the slope and then combine them if they seem close enough
def findVert(segs):
	vert = []
	slope = .001
	for i in range(len(segs[0])):
		vertical = False
		x1=segs[0,i,0]
		y1=segs[0,i,1]
		x2=segs[0,i,2]
		y2=segs[0,i,3]

		rise = (y2-y1)
		run = (x2-x1)

		if (run == 0):
			vertical = True

		elif (run != 0):
			slope = rise/run

		if (slope>10):
			vertical = True

		if (vertical):
			vert.append([x1,y1,x2,y2])

	vert = np.asarray(vert)
	return vert


def main():

	pic1 = 'am.jpg'
	pic2 = 'am1.jpg'

	print 'Image 1'
	image = cv2.imread(pic1)
	segs =segFind(filt(image),image)
	objs = profile(segs,1)
	im1 = draw(image,segs, objs)
	

	print '\nImage 2'
	image = cv2.imread(pic2)
	segs =segFind(filt(image),image)
	objs = profile(segs,2)
	im2 = draw(image,segs, objs)


	fig = plt.figure()
	a = fig.add_subplot(1,2,1)
	im1plot = plt.imshow(im1)
	a = fig.add_subplot(1,2,2)
	im2plot = plt.imshow(im2)

	plt.show()
	



class Segment:
	def __init__(self,points,Num):
		self.points=points
		self.Num = Num

	def setColor(self, color):
		self.color = color

	def setSlope(self,slope):
		self.slope = slope

	def setDistance(self,dist):
		self.dist = dist


main()
