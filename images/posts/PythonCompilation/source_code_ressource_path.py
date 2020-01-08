import os 
import sys
from time import sleep


def main():
    ressource_path = getattr(sys, '_MEIPASS', os.path.abspath('.'))
    print(ressource_path)
    current_path = os.path.abspath('.')
    print(current_path)
    sleep(5)  # Force to keep console open


if __name__ == '__main__':
    main()
