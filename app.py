import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create open button
        self.open_button = tk.Button(self)
        self.open_button["text"] = "Open"
        self.open_button["command"] = self.open_image
        self.open_button.pack(side="top")

        # Create original image label
        self.original_image_label = tk.Label(self)
        self.original_image_label.pack(side="top")

        # Create processed image label
        self.processed_image_label = tk.Label(self)
        self.processed_image_label.pack(side="top")

    def open_image(self):
        image_path = filedialog.askopenfilename()
        self.original_image = cv2.imread(image_path)
        self.show_original_image()
        self.process_image()

    def show_original_image(self):
        image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        self.original_image_label.configure(image=image)
        self.original_image_label.image = image

    def process_image(self):
        kernel = np.array([[0, -1, 0],
                           [-1, 5,-1],
                           [0, -1, 0]])
        processed_image = cv2.filter2D(self.original_image, -1, kernel)
        processed_image = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
        processed_image = Image.fromarray(processed_image)
        processed_image = ImageTk.PhotoImage(processed_image)
        self.processed_image_label.configure(image=processed_image)
        self.processed_image_label.image = processed_image

root = tk.Tk()
app = Application(master=root)
app.mainloop()
