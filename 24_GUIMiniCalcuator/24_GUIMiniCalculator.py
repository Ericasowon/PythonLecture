# Goal
# Create number buttons & operator buttons
# Display input in the result field (Entry widget)
# Show calculation result when "=" button is clicked


import tkinter as tk

# Button click handler
def click(button_text):
    if button_text == "=":  # Evaluate expression
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":  # Clear entry
        entry.delete(0, tk.END)
    else:  # Insert numbers or operators
        entry.insert(tk.END, button_text)

# Main window
root = tk.Tk()
root.title("🧮 Mini Calculator")

# Input field
entry = tk.Entry(root, width=20, font=("Arial", 18),
                 borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Calculator buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

# Place buttons in grid
row, col = 1, 0
for b in buttons:
    button = tk.Button(root, text=b, width=5, height=2,
                       font=("Arial", 14), command=lambda x=b: click(x))
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the app
root.mainloop()
