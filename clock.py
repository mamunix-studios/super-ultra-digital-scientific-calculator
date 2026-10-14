import sys
import tkinter as tk
from tkinter import ttk
import time
import os

class Mamunix_Smart_clock:
    def __init__(self, root):
        self.root = root
        self.root.title("MAMUNIX Premium Digital Smart Clock")
        if hasattr(sys, '_MEIPASS'):
            self.root.iconbitmap(os.path.join(sys._MEIPASS, 'assets', 'mamunix_app.ico'))
        else:
            self.root.iconbitmap(os.path.join(os.path.abspath("."), 'assets', 'mamunix_app.ico'))
            self.root.geometry("500x350")
            self.root.resizable(False, False)

            self.main_frame = tk.Frame(self.root, bg="#0B0C10", padx=20, pady=20)
            self.main_frame.pack(fill=tk.BOTH, expand=True)
            self.brand_label = tk.Label(self.main_frame, text="MAMUNIX STUDIOS", font=("Helvetica", 14, "bold"),
                                         bg="#0B0C10", fg="#C5A059")
            self.brand_label.pack(anchor="w", pady=(0, 10))
            self.greeting_label = tk.Label(self.main_frame, text="Initializing System...", font=("Segoe UI", 14, "italic"),
                                           bg="#0B0C10", fg="#45A29E")
            self.greeting_label.pack(anchor="w", pady=(0, 15))
            self.display_frame = tk.Frame(self.main_frame, bg="#1F2833",   highlightbackground="#66FCF1", 
                                          highlightthickness=1, bd=0)
            self.display_frame.pack(fill=tk.X, pady=10, ipady=15)

            self.time_label = tk.Label(self.display_frame, text="00:00:00 AM", font=("Consolas", 42, "bold"), bg="#1F2833",
                                       fg="#FF3333")
            self.time_label.pack()
        self.date_label = tk.Label(self.main_frame, text="Loading Date...", font=("Segoe UI", 11, "bold"),
              bg="#0B0C10", fg="#45A29E")
        self.date_label.pack(anchor="e", pady=(15, 0))

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%I:%M:%S %p")
        current_date = time.strftime("%A, %B %d, %Y")
        hour = int(time.strftime("%H"))
        
        if hour < 12:
            greeting = "Good Morning! ☀️"
        elif 12 <= hour < 16:
            greeting = "Good Afternoon! 🌤️"
        elif 16 <= hour < 20:
            greeting = "Good Evening! 🌆"
        else:
            greeting = "Good Night! 🌙"
            
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        self.greeting_label.config(text=greeting)
        
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    app = Mamunix_Smart_clock(root)
    root.mainloop()