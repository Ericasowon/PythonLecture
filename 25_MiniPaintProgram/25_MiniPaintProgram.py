# Goal
# Draw lines using mouse click & drag
# Add an eraser (clear) function
# Add a color selection feature (start with a single default color)

import tkinter as tk

def paint(event):
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    canvas.create_oval(x1, y1, x2, y2, fill="black", outline="black")

def clear_canvas():
    canvas.delete("all")

root = tk.Tk()
root.title("🎨 Mini Paint Program")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Draw by dragging the mouse
canvas.bind("<B1-Motion>", paint)

# Clear button
btn_clear = tk.Button(root, text="🧹 Clear", command=clear_canvas)
btn_clear.pack()

root.mainloop()
