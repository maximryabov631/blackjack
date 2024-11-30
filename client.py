import tkinter as tk
import subprocess

def run_blackjack_with_solana():
    subprocess.Popen(["python", "blackjack_using_solana.py"])

def run_blackjack_without_solana():
    subprocess.Popen(["python", "play_blackjack_without_solana.py"])

# main window that shopws up
root = tk.Tk()
root.title("Blackjack Client")

# Create buttons
btn_with_solana = tk.Button(root, text="Play Blackjack Using Solana", command=run_blackjack_with_solana, width=30, height=2)
btn_with_solana.pack(pady=10)

btn_without_solana = tk.Button(root, text="Play Blackjack Without Solana", command=run_blackjack_without_solana, width=30, height=2)
btn_without_solana.pack(pady=10)

root.mainloop()
