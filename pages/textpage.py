import tkinter as tk


class textPage:
    def __init__(self, canvas):
        self.canvas = canvas
        self.elements = []

        # Stack
        self.undo_stack = [""]
        self.redo_stack = []

        self.text_area = tk.Text(
            self.canvas.master,
            width=56,
            height=14,
            font=("Arial", 12)
        )

        self.text_window = self.canvas.create_window(
            600, 320,
            window=self.text_area
        )
        self.elements.append(self.text_window)

        self.undo_btn = tk.Button(
            self.canvas.master,
            text="Undo",
            command=self.undo
        )

        self.undo_window = self.canvas.create_window(
            500, 480,
            window=self.undo_btn
        )
        self.elements.append(self.undo_window)

        self.redo_btn = tk.Button(
            self.canvas.master,
            text="Redo",
            command=self.redo
        )

        self.redo_window = self.canvas.create_window(
            700, 480,
            window=self.redo_btn
        )
        self.elements.append(self.redo_window)

        # Simpan setiap perubahan karakter
        self.text_area.bind("<KeyRelease>", self.save_state)

    def save_state(self, event=None):
        current_text = self.text_area.get("1.0", "end-1c")

        if current_text != self.undo_stack[-1]:
            self.undo_stack.append(current_text)
            self.redo_stack.clear()

    def undo(self):
        if len(self.undo_stack) > 1:
            current = self.undo_stack.pop()
            self.redo_stack.append(current)

            previous = self.undo_stack[-1]

            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", previous)

    def redo(self):
        if self.redo_stack:
            text = self.redo_stack.pop()

            self.undo_stack.append(text)

            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", text)

    def show(self):
        for el in self.elements:
            self.canvas.itemconfigure(el, state="normal")

    def hide(self):
        for el in self.elements:
            self.canvas.itemconfigure(el, state="hidden")
