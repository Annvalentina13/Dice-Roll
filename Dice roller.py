import tkinter as tk
import random

def roll_dice():
    dice_value = random.randint(1, 6)
    result_label.config(text=f"You rolled: {dice_value}")

# GUI setup
root = tk.Tk()
root.title("Dice Rolling Simulator")
root.geometry("300x200")
root.config(bg="lightblue")

title_label = tk.Label(root, text="🎲 Dice Rolling Simulator 🎲", font=("Helvetica", 16), bg="lightblue")
title_label.pack(pady=20)

roll_button = tk.Button(root, text="Roll the Dice", font=("Helvetica", 14), command=roll_dice)
roll_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 16), bg="lightblue")
result_label.pack(pady=20)

root.mainloop()
