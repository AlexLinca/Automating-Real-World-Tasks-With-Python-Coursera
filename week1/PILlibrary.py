import PIL
from PIL import Image
# im = Image.open("/Users/djadmin/Desktop/Coursera classes/Automating_Real_World_Tasks_With_Python/dog.jpeg")
# im.rotate(45).show()
# help(PIL)
#For example, if we wanted to resize an image and save the new image with a new name, we could do it with:
im = Image.open("/Users/djadmin/Desktop/Coursera classes/Automating_Real_World_Tasks_With_Python/dog.jpeg")
new_im = im.resize((640,480))
new_im.save("new_dog.jpeg")

im = Image.open("/Users/djadmin/Desktop/Coursera classes/Automating_Real_World_Tasks_With_Python/dog.jpeg")
im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")
