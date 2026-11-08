import tkinter as tk
import random
import os
import sys
from PIL import ImageTk, Image

def resource_path(relative_path):
    """ Находит файлы, зашитые внутрь скомпилированного EXE """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Указываем путь к нашему локальному PNG файлу
IMG_NAME = resource_path("Scribbles.png")

if os.path.exists(IMG_NAME):
    # Открываем изображение из папки скрипта
    img_data = Image.open(IMG_NAME).convert("RGB")
else:
    # Красная заглушка на случай критической ошибки
    img_data = Image.new('RGB', (200, 200), color='red')

root = tk.Tk()
root.withdraw()
photos = []

def create_paper():
    window = tk.Toplevel(root)
    window.title("БУМАЖКИ!")
    window.attributes("-topmost", True)
    window.overrideredirect(True)
    
    size = random.randint(180, 280)
    scr_width = window.winfo_screenwidth()
    scr_height = window.winfo_screenheight()
    x = random.randint(0, scr_width - size)
    y = random.randint(0, scr_height - size)
    window.geometry(f"{size}x{size}+{x}+{y}")
    
    resized_img = img_data.resize((size, size))
    photo = ImageTk.PhotoImage(resized_img)
    photos.append(photo)
    
    label = tk.Label(window, image=photo, bd=0)
    label.pack(fill="both", expand=True)
    
    def on_click(event):
        create_paper()
        create_paper()
        window.destroy()
        
    label.bind("<Button-1>", on_click)

for _ in range(5):
    create_paper()

root.mainloop()
