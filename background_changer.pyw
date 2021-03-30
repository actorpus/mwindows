from tkinter import Tk
from tkinter import Button
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from os import environ
from os import system


def browseFiles():
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\" + environ.get("USERNAME") + "\\Pictures",
                                          title="Select a Image",
                                          filetypes=(("Image Files", "*.jpg*"), ("All Files", "*.*")))

    if filename:
        image: Image.Image = Image.open(filename)
        image = image.resize((1920, 1080))
        image.save("C:\\Users\\" + environ.get("USERNAME") + "\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\TranscodedWallpaper", format="jpeg")


def reboot():
    if messagebox.askokcancel("Reboot", "Warning, rebooting will cause loss of all unsaved work!"):
        system("shutdown -f")


window = Tk()
window.title('Background Changer')
window.geometry("143x50")
window.resizable(0, 0)
window.attributes('-toolwindow', True)


Button(window, text="Change Background", command=browseFiles, width=19).pack(side="top")
Button(window, text="Apply Changes", command=reboot, width=19).pack(side="bottom")


window.mainloop()
