import sys
import os
from PIL import Image

# Grab first and second argument
poke_path = sys.argv[1]
new_path = sys.argv[2]

# Check is new/ exists, if not create
if not os.path.exists(new_path):
    os.mkdir(new_path)

# Loop through Pokedex, convert images to PNG
for filename in os.listdir(poke_path):
    img = Image.open(os.path.join(poke_path, filename))
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{new_path}{clean_name}.png', 'png')
