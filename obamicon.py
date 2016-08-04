from PIL import Image

darkBlue = (0,51,76)
rojo = (217, 26, 33)
lightBlue = (112,150,158)
yellow = (252,227,166)

im = Image.open("puppy.jpg")

data = im.getdata()
data_list = list(data)

def colorize(image_data):
	new_pic = [] #this list will hold all the pixels of our new image
	
	for pixel in image_data: #for each pixel of image_data
		# store the red, blue, and green values of each pixel separately
		# each pixel has RGB values that are stored in tuples
		red = pixel[0]
		green = pixel[1]
		blue = pixel[2]
		
		# intensity is found by adding red, green, and blue
		total = red + green + blue
		
		
		
	

	

colors = colorize(data_list)

new_image = Image.new(im.mode, im.size)
new_image.putdata(colors)
new_image.show()
new_image.save("output.jpg", "jpeg")




