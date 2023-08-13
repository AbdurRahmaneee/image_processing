from PIL import Image, ImageFilter

img = Image.open('./pics/space.jpg')
# filter_img = img.filter(ImageFilter.SMOOTH)
# convert_img = img.convert('L')
# box = (100, 100, 400, 400)
# region = convert_img.crop(box)
#
# # resize = convert_img.resize(re)
# region.save('grey.png')
img.thumbnail((400, 400))
img.save('thumbnail.jpg')
print(img.size)