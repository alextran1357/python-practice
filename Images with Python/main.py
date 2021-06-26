from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.convert('L')
filtered_img.save("grey.png", 'png')

box = (100,100,400,400)
region = filtered_img
filtered_img.resize((300,300)).show()

