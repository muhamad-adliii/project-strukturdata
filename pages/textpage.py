import tkinter as tk 

class textPage:
    def __init__(self, canvas):
        self.canvas = canvas
        self.elements = []

        self.title_id = self.canvas.create_text(
            600, 180, 
            font=("Poppins", 14, "bold"),
            fill="black"
        )
        self.elements.append(self.title_id)

        self.frame_img = tk.PhotoImage(file="./images/bingkai.png")
        
        self.frame_id = self.canvas.create_image(
            600, 320, 
            image=self.frame_img
        )
        self.elements.append(self.frame_id)

        self.text_area = tk.Text(
            self.canvas.master, 
            width=56,
            height=14,
            font=("Poppins", 12),
            relief="flat",
            bd=0,
            highlightthickness=0,
            fg="white",
            bg="#030b30",
            insertbackground="white"
        )
        self.text_window = self.canvas.create_window(
            600, 320, 
            window=self.text_area
        )
        self.elements.append(self.text_window)

        self.undo_btn = tk.Button(
            self.canvas.master, 
            text="Undo",
            width=15
        )
        self.undo_window = self.canvas.create_window(
            500, 480, 
            window=self.undo_btn
        )
        self.elements.append(self.undo_window)

        self.redo_btn = tk.Button(
            self.canvas.master,
            text="Redo",
            width=15
        )
        self.redo_window = self.canvas.create_window(
            700, 480, 
            window=self.redo_btn
        )
        self.elements.append(self.redo_window)

        self.hide()

    def show(self):
        for el in self.elements:
            self.canvas.itemconfigure(el, state="normal")

    def hide(self):
        for el in self.elements:
            self.canvas.itemconfigure(el, state="hidden")