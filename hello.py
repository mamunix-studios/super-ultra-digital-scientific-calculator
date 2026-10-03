import os
import tkinter as tk
from tkinter import messagebox
import math

history = []
memory_value = 0.0
is_dark_mode = True

def percentage(x, y):
    return (x * y) / 100
def square_root(x):
    if x < 0: return "Error"
    return math.sqrt(x)
def factorial_func(x):
    try:
        if x < 0 or not x.is_integer():
            return "Error"
        return math.factorial(int(x))
    except:
        return "Error"

def button_click(char):
    global memory_value
    current = display_entry.get()

    if char == "🌓 Mode":
        toggle_theme()
        return

    elif char == "C":
        display_entry.delete(0, tk.END)

    elif char == "⌫":
        display_entry.delete(len(current)-1, tk.END)

    elif char == "M+":
        try: memory_value += float(current)
        except: pass

    elif char == "M-":
        try: memory_value -= float(current)
        except: pass

    elif char == "MR":
        display_entry.insert(tk.END, str(memory_value))

    elif char == "MC":
        memory_value = 0.0

    elif char == "=":
        if not current.strip():
            return
        try:
            expr = current.replace("^", "**").replace("x", "*")
            if "%" in expr:
                parts = expr.split("%")
                if len(parts) == 2:
                    num2 = float(parts[0])
                    num1 = float(parts[1])
                    result = percentage(num1, num2)
                    calculation = f"{num2} % of {num1} = {result}"
                    display_entry.delete(0, tk.END)
                    display_entry.insert(0, str(result))
                    history.append(calculation)
                else:
                    display_entry.delete(0, tk.END)
                    display_entry.insert(0, "Error")
            else:
                result = eval(expr)
                calculation = f"{current} = {result}"
                display_entry.delete(0, tk.END)
                display_entry.insert(0, str(result))
                history.append(calculation)
        except Exception:
            display_entry.delete(0, tk.END)
            display_entry.insert(0, "Error")

    elif char == "n!":
        try:
            res = factorial_func(float(current))
            display_entry.delete(0, tk.END)
            display_entry.insert(0, str(res))
            history.append(f"{current} = {res}")
        except:
            display_entry.delete(0, tk.END)
            display_entry.insert(0, "Error")

    elif char == "sin⁻¹":
        try:
            res = math.degrees(math.asin(float(current)))
            display_entry.delete(0, tk.END)
            display_entry.insert(0, str(round(res, 4)))
            history.append(f"sin⁻¹({current}) = {round(res, 4)}")
        except:
            display_entry.delete(0, tk.END)
            display_entry.insert(0, "Error")

    elif char == 'cos⁻¹':
        try:
            res = math.degrees(math.acos(float(current)))
            display_entry.delete(0, tk.END)
            display_entry.insert(0, str(round(res, 4)))
            history.append(f"cos⁻¹({current}) = {round(res, 4)}")
        except:
            display_entry.delete(0, tk.END)
            display_entry.insert(0, "Error")

    elif char == 'tan⁻¹':
        try:
            res = math.degrees(math.atan(float(current)))
            display_entry.delete(0, tk.END)
            display_entry.insert(0, str(round(res, 4)))
            history.append(f"tan⁻¹({current}) = {round(res, 4)}")
        except:
            display_entry.delete(0, tk.END)
            display_entry.insert(0, "Error")

    elif char == "✓":
        try:
            res = square_root(float(current))
            display_entry.delete(0, tk.END)
            display_entry.insert(0, str(res))
            history.append(f"√({current}) = {res}")
        except:
            display_entry.delete(0, tk.END)
            display_entry.insert(0, "Error")

    elif char == "sin":
        try:
            res = math.sin(math.radians(float(current)))
            display_entry.delete(0, tk.END)
            display_entry.insert(0, str(round(res, 4)))
            history.append(f"sin({current}) = {round(res, 4)}")
        except:
            display_entry.delete(0, tk.END)
            display_entry.insert(0, "Error")

    elif char == 'cos':
        try:
            res = math.cos(math.radians(float(current)))
            display_entry.delete(0, tk.END)
            display_entry.insert(0, str(round(res, 4)))
            history.append(f"cos({current}) = {round(res, 4)}")
        except:
            display_entry.delete(0, tk.END)
            display_entry.insert(0, "Error") 

    elif char == 'tan':
        try:
            res = math.tan(math.radians(float(current)))
            display_entry.delete(0, tk.END)
            display_entry.insert(0, str(round(res, 4)))
            history.append(f"tan({current}) = {round(res, 4)}")
        except:
            display_entry.delete(0, tk.END)
            display_entry.insert(0, "Error") 
    elif char == 'log':
        try:
            res = math.log10(math.radians(float(current)))
            display_entry.delete(0, tk.END)
            display_entry.insert(0, str(round(res, 4)))
            history.append(f"log({current}) = {round(res, 4)}")
        except:
            display_entry.delete(0, tk.END)
            display_entry.insert(0, "Error") 

    elif char == 'ln':
        try:
            res = math.log(math.radians(float(current)))
            display_entry.delete(0, tk.END)
            display_entry.insert(0, str(round(res, 4)))
            history.append(f"In({current}) = {round(res, 4)}")
        except:
            display_entry.delete(0, tk.END)
            display_entry.insert(0, "Error") 

    elif char == "π":
        res = str(round(math.pi, 4))
        display_entry.insert(tk.END, res)
        history.append(f"π = {res}")

    elif char == "e":
        res = str(round(math.e, 4))
        display_entry.insert(tk.END, res)
        history.append(f"e = {res}")

    else: 
        display_entry.insert(tk.END, char)

def keyboard_press(event):
    key = event.char
    if key == '\r': 
        button_click('=') 
    elif key == '\x1b': 
        button_click('C')  
    elif key == '\x08': 
        button_click('⌫') 
    elif key in ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '%', '^', '+']: 
        button_click(key) 
    elif key.lower() == 'x': 
        button_click('x')

def toggle_theme():
    global is_dark_mode
    if is_dark_mode:
        root.configure(bg="#f4f5f7")                 
        top_utility_frame.configure(bg="#f4f5f7")
        frame.configure(bg="#f4f5f7")
        bottom_frame.configure(bg="#f4f5f7")
        display_entry.configure(bg="#ffffff", fg="#1e1f26", highlightbackground="#cbd5e1")
        is_dark_mode = False
    else:
        root.configure(bg="#1e1f26")
        top_utility_frame.configure(bg="#1e1f26")
        frame.configure(bg="#1e1f26")
        bottom_frame.configure(bg="#1e1f26")
        display_entry.configure(bg="#16171d", fg="#e2e8f0", highlightbackground="#3a3b45")
        is_dark_mode = True

def copy_result():
    root.clipboard_clear()
    root.clipboard_append(display_entry.get())
    messagebox.showinfo("Success", "Result copied to clipboard successfully!") 

def show_shortcuts(): 
    msg = "Keyboard Shortcuts:\n\n" \
          "• Enter / Return => Calculate (=)\n" \
          "• Escape (Esc) => Clear All (C)\n" \
          "• Backspace => Delete Last Digit (⌫)\n" \
          "• Key 'X' or '*' => Multiplication" 
    messagebox.showinfo("Shortcut Guide", msg) 

def show_about(): 
    messagebox.showinfo("About Application", "Universal Scientific Calculator\n" 
                        "Version: 1.0 (Ultra Digital)\n\n" \
                        "Powered by: MAMUNIX Studios\n" \
                        "Developed with pride by Md Mamun-UR Rashid.\n" \
                        "All rights reserved © 2026.") 

def show_history():
        if not history:
            messagebox.showinfo("History", "History not Available")
        else:
            messagebox.showinfo("Calculation History", "\n".join(history))

def delete_history(): 
        if not history:
            messagebox.showinfo("History",  "History not Available for Deletion")
        else:
            history.clear()
            messagebox.showinfo("History", "History Cleared Successfully.") 

root = tk.Tk()
icon_path = os.path.join("assets", "mamunix_app.ico")
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)
root.title("Super Ultra Digital Scientific Calculator")
root.geometry("480x700")
root.resizable(False, False)
root.configure(bg="#1e1f26")

display_entry = tk.Entry(root, bg="#0C1547", fg="#e2e8f0", font=("Arial", 22, "bold"), justify="right", bd=5,
                          relief=tk.FLAT, highlightbackground="#0c114d", highlightcolor="#0077b6")

display_entry.pack(padx=15, pady=(20, 15), fill=tk.BOTH, ipady=5)

top_utility_frame = tk.Frame(root, bg="#1e1f26")
top_utility_frame.pack(pady=5, fill=tk.X, padx=15) 

btn_copy = tk.Button(top_utility_frame, text="📋 Copy Result", font=("Arial", 9, "bold"), bg="#2a4365", 
                     fg="white", bd=2, width=14, command=copy_result)
btn_copy.pack(side="left", padx=4, pady=2, ipady=4, expand=True, fill=tk.X)

btn_shortcut = tk.Button(top_utility_frame, text="⌨️ Shortcuts", font=("Arial", 9, "bold"), bg="#8c4d16", 
                         fg="white", bd=2, width=14, command=show_shortcuts)

btn_shortcut.pack(side="left", padx=4, pady=2, ipady=4, expand=True, fill=tk.X)

btn_about = tk.Button(top_utility_frame, text="ℹ️ About", font=("Arial", 9, "bold"), bg="#5a3782",
                       fg="white", bd=2, width=14, command=show_about)
btn_about.pack(side="left", padx=4, pady=2, ipady=4, expand=True, fill=tk.X)

frame = tk.Frame(root, bg="#1e1f26")
frame.pack(ipady=5)

buttons = [
    ['MC', 'MR', 'M+', 'M-', '🌓 Mode'],
    ['sin⁻¹', 'cos⁻¹', 'tan⁻¹', 'n!', '^'],
    ['sin', 'cos', 'tan', 'log', 'ln'], 
    ['7', '8', '9', '/', 'C'], 
    ['4', '5', '6', 'x', '✓'], 
    ['1', '2', '3', '-', '='], 
    ['0', '.', '%', '+', '⌫'],
    ['π', 'e', '', '', '']
]

for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        btn_txt = buttons[i][j]
        if btn_txt == '':
            continue

        if btn_txt == "=": 
            btn_bg = "#23cab9"  
        elif btn_txt == "🌓 Mode": 
             btn_bg = "#00adb5"  
        elif btn_txt in ['MC', 'MR', 'M+', 'M-']: 
            btn_bg = "#5c677d"  
        elif btn_txt in ['/', 'x', '-', '+', '^', '✓', '%', 'sin⁻¹', 'cos⁻¹', 'tan⁻¹', 'n!']: 
            btn_bg = "#3d3f58"  
        elif btn_txt in ['sin', 'cos', 'tan', 'log', 'ln', 'π', 'e']: 
            btn_bg = "#0077b6" 
        elif btn_txt in ['⌫', 'C']: 
            btn_bg = "#e63946"  
        else: 
            btn_bg = "#2a2b36" 

        btn = tk.Button(frame, text=btn_txt, font=("Arial", 11, "bold"), width=7, height=2, bg=btn_bg, fg="white",
                         bd=2, relief=tk.RAISED)
        btn.configure(command=lambda text=btn_txt: button_click(text))
        btn.grid(row=i, column=j, padx=4, pady=4)

bottom_frame = tk.Frame(root, bg="#292a35")
bottom_frame.pack(pady=10, fill=tk.X, padx=15)

btn_history = tk.Button(bottom_frame, text="View History", font=("Arial", 9, "bold"), bg="#14532d", fg="white",
                         bd=2, width=17, command=show_history) 

btn_history.pack(side="left", padx=20, pady=4, ipady=4, expand=True, fill=tk.X) 

btn_delete = tk.Button(bottom_frame, text="Delete History", font=("Arial", 9, "bold"), bg="#7f1d1d", fg="white", 
                       bd=2, width=17, command=delete_history) 
btn_delete.pack(side="right", padx=20, pady=4, ipady=4, expand=True, fill=tk.X) 

root.bind('<Key>', keyboard_press)
root.mainloop()