
base_width = 360

image = Image.open('example-image.jpg')

width_percent = (base_width / float(image.size[0]))

hsize = int((float(image.size[1]) * float(width_percent)))

image = image.resize((base_width, hsize), PIL.Image.ANTIALIAS)

image.save('resized_compressed_image.jpg') 
