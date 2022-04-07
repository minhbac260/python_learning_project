from numpy import equal
from pathlib import Path


file_inp = str(Path(__file__).parent) + "/input_broken_keyboard.INP"

def process(text_inp):
    f_pointer = open(text_inp,"r")
    char_arr = []
    key_number = 0
    text = f_pointer.readline()
    while text != '0':
        key_number = int(text)
        text = f_pointer.readline()
        print(text)
        text = f_pointer.readline()
        
process(file_inp)
        