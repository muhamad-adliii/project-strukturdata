import tkinter as tk
from PIL import Image, ImageTk
from pages.textpage import textPage
from pages.imagepage import ImagePage

root = tk.Tk()
root.title("Program Stack Undo Redo")
root.geometry("1200x700")
root.resizable(False, False)

canvas = tk.Canvas(
    root,
    width=1200,
    height=700,
    highlightthickness=0
)
canvas.pack(fill="both", expand=True)

image = Image.open("./images/bg.png")
image = image.resize((1200, 700))
photo = ImageTk.PhotoImage(image)

canvas.create_image(
    0,
    0,
    image=photo,
    anchor="nw"
)


canvas.create_text(
    600,
    30,
    text="STACK UNDO REDO PROJECT",
    fill="white",
    font=("Poppins", 16, "bold")
)


def show_text_page():
    image_page.hide()
    text_page.show()


def show_image_page():
    text_page.hide()
    image_page.show()


btn_text = tk.Button(
    root,
    text="Text Undo Redo",
    width=20,
    height=2,
    command=show_text_page
)


canvas.create_window(
    500,
    100,
    window=btn_text
)

btn_image = tk.Button(
    root,
    text="Image Undo Redo",
    width=20,
    height=2,
    command=show_image_page
)
canvas.create_window(
    700,
    100,
    window=btn_image
)

text_page = textPage(canvas)
image_page = ImagePage(canvas)

show_text_page()

root.mainloop()
