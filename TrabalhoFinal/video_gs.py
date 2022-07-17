from PIL import Image
from pathlib import Path
import os

file_directory = Path("fundo_branco/")

for current_file in file_directory.iterdir():
    if current_file.is_file():
        with open(current_file, 'r') as data_file:
            image = Image.open("fundo_branco/" + os.path.basename(current_file))
            # Gray
            image = image.convert('L')
            image.save("fundo_branco_gs/" + os.path.basename(current_file))

file_directory = Path("fundo_vermelho/")

for current_file in file_directory.iterdir():
    if current_file.is_file():
        with open(current_file, 'r') as data_file:
            image = Image.open("fundo_vermelho/" + os.path.basename(current_file))
            # Gray
            image = image.convert('L')
            image.save("fundo_vermelho_gs/" + os.path.basename(current_file))