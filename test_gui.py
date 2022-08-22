from tkinter import *
from PIL import Image
from tkinter import filedialog

window = Tk()
window.title("Silver")


def dir_button_clicked():
    dir_name = filedialog.askdirectory(initialdir='C:\\Users\\Blade\\Desktop')
    print(dir_name)
    return dir_name


get_dir_button = Button(text="Get Dir", command=dir_button_clicked)
get_dir_button.pack()

window.mainloop()
