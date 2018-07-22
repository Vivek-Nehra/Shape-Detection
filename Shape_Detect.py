
def contours (image,color,):
	image = cv2.GaussianBlur(image,(5,5),0)
	image,contours, hierarchy = cv2.findContours(image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	font=cv2.FONT_HERSHEY_SIMPLEX
	for i in contours:
	  if cv2.contourArea(i)>200:		# Boundary check
		shape=[]
		shape.append(color)
		vertices = cv2.approxPolyDP(i,0.01*cv2.arcLength(i,True),True)

		# Calculate centroid
		M = cv2.moments(i)		
		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])

		if len(vertices) == 3:	# It is a triangle
			shape.insert(1,"Triangle")
			cv2.putText(img,color,(cx-35,cy-25),font,0.51,(0,0,0),2	)
			cv2.putText(img,'Triangle',(cx-20,cy),font,0.51,(0,0,0),2)	
			cv2.putText(img,'(%d,%d)' % (cx,cy),(cx-5,cy+25),font,0.51,(0,0,0),2)
		elif len(vertices) == 4: # It is either a trapezium or a rhombus
			x,y,w,h, = cv2.boundingRect(i)
			apratio = cv2.contourArea(i)/(w*h)

			if apratio>0.73 : # It is a trapezium
				shape.insert(1,"Trapezium")
				cv2.putText(img,color,(cx-35,cy-25),font,0.51,(0,0,0),2)
				cv2.putText(img,'Trapezium',(cx-20,cy),font,0.51,(0,0,0),2)	
				cv2.putText(img,'(%d,%d)' % (cx,cy),(cx-5,cy+25),font,0.51,(0,0,0),2)

			elif apratio<0.73 : 	# It is a rhombus
				shape.insert(1,"Rhombus")
				cv2.putText(img,color,(cx-35,cy-25),font,0.51,(0,0,0),2)
				cv2.putText(img,'Rhombus',(cx-20,cy),font,0.51,(0,0,0),2)	
				cv2.putText(img,'(%d,%d)' % (cx,cy),(cx-5,cy+25),font,0.51,(0,0,0),2)


		elif len(vertices) == 5: # It is a pentagon
			shape.insert(1,"Pentagon")
			cv2.putText(img,color,(cx-35,cy-25),font,0.51,(0,0,0),2)
			cv2.putText(img,'Pentagon',(cx-20,cy),font,0.51,(0,0,0),2)	
			cv2.putText(img,'(%d,%d)' % (cx,cy),(cx-5,cy+25),font,0.51,(0,0,0),2)

		elif len(vertices) == 6: # It is a hexagon
			shape.insert(1,"Hexagon")
			cv2.putText(img,color,(cx-35,cy-25),font,0.51,(0,0,0),2)
			cv2.putText(img,'Hexagon',(cx-20,cy),font,0.51,(0,0,0),2)	
			cv2.putText(img,'(%d,%d)' % (cx,cy),(cx-5,cy+25),font,0.51,(0,0,0),2)
		
		else : # It is a circle
			shape.insert(1,"Circle")
			cv2.putText(img,color,(cx-35,cy-25),font,0.51,(0,0,0),2)
			cv2.putText(img,'Circle',(cx-20,cy),font,0.51,(0,0,0),2)	
			cv2.putText(img,'(%d,%d)' % (cx,cy),(cx-5,cy+25),font,0.51,(0,0,0),2)

		shape.extend([cx,cy])
		#b=["-".join("%s" %(k) for k in b)]
		output.append(shape)
import numpy as np
import cv2
global output
output=[]
#image = raw_input("Enter the name of the image:")
global img
img = cv2.imread(raw_input("Enter name of image: "))


img = cv2.GaussianBlur(img,(5,5),0)		#Blur Image
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)	# Color detection is easy on HSV image
#output.append(image)


# Blue Mask
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
contours(mask,'Blue')				# Detect blue contours
#cv2.imshow("Imagew",mask)


# Green Mask
lower_green = np.array([50,50,50])
upper_green = np.array([70,255,255])
mask2 = cv2.inRange(hsv, lower_green, upper_green)
contours(mask2,'Green')				# Detect Green Contours
#cv2.imshow("Imagge",mask2)


# Red Mask
lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])
mask3 = cv2.inRange(hsv, lower_red, upper_red)
contours(mask3,'Red')				# Detect Red contours
#cv2.imshow("Imnage",mask3)


#canny=cv2.Canny(dilate,100,200)
#cv2.imshow("Canny",canny)


print output
cv2.imshow("Image",img)
#print fp	
cv2.waitKey(0)
cv2.destroyAllWindows()

	
