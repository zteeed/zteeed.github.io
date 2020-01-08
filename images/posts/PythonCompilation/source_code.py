from PIL import Image
import random
import os
import sys


def get_current_path():
    """ Get current folder path, works for dev and PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath('.')
        return base_path


def get_ressource_path(filename):
    """ Get current ressource path, works for dev and PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.abspath('.'))
    return os.path.join(base_path, filename)


def main():
    cars = os.listdir(get_ressource_path('images'))
    selected_car = random.choice(cars)
    path = get_ressource_path(f'images\\{selected_car}')
    img = Image.open(path)
    img.save(f'random_{selected_car}.png')


if __name__ == '__main__':
    main()
