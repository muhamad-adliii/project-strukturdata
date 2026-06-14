import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class ImagePage:
    def __init__(self, canvas):
        self.canvas = canvas
        self.elements = []

        self.undo_stack = []
        self.redo_stack = []
        self.current_image_path = None
        self.photo = None

        self.title_id = self.canvas.create_text(
            600, 180,
            text="IMAGE UNDO REDO PAGE",
            font=("Arial", 16, "bold"),
            fill="white"
        )
        self.elements.append(self.title_id)

        self.image_frame = tk.Frame(
            self.canvas.master,
            bg="#dfe6e9",
            width=500,
            height=250
        )
        self.image_frame.pack_propagate(False)

        self.image_label = tk.Label(
            self.image_frame,
            text="IMAGE AREA",
            bg="#dfe6e9",
            font=("Arial", 14)
        )
        self.image_label.pack(expand=True, fill="both")

        self.image_window = self.canvas.create_window(
            600, 320,
            window=self.image_frame,
            width=500,
            height=250
        )
        self.elements.append(self.image_window)

        self.add_btn = tk.Button(
            self.canvas.master,
            text="Add Image",
            width=15,
            command=self.add_image
        )
        self.add_window = self.canvas.create_window(
            450, 480,
            window=self.add_btn
        )
        self.elements.append(self.add_window)

        self.undo_btn = tk.Button(
            self.canvas.master,
            text="Undo",
            width=15,
            command=self.undo
        )
        self.undo_window = self.canvas.create_window(
            600, 480,
            window=self.undo_btn
        )
        self.elements.append(self.undo_window)
        self.redo_btn = tk.Button(
            self.canvas.master,
            text="Redo",
            width=15,
            command=self.redo
        )
        self.redo_window = self.canvas.create_window(
            750, 480,
            window=self.redo_btn
        )
        self.elements.append(self.redo_window)

        self.hide()

    def add_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")]
        )
        if file_path:
            self.undo_stack.append(self.current_image_path)
            self.redo_stack.clear()
            self.current_image_path = file_path
            self.display_image(self.current_image_path)

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.current_image_path)
            self.current_image_path = self.undo_stack.pop()
            self.display_image(self.current_image_path)

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.current_image_path)
            self.current_image_path = self.redo_stack.pop()
            self.display_image(self.current_image_path)

    def display_image(self, path):
        if path:
            try:
                img = Image.open(path)
                img = img.resize((500, 250), Image.Resampling.LANCZOS)
                self.photo = ImageTk.PhotoImage(img)
                self.image_label.config(image=self.photo, text="")
            except Exception as e:
                print(f"Error loading image: {e}")
        else:
            self.image_label.config(image="", text="IMAGE AREA")
            self.photo = None

    def show(self):
        for el in self.elements:
            self.canvas.itemconfigure(el, state="normal")

    def hide(self):
        for el in self.elements:
            self.canvas.itemconfigure(el, state="hidden")
