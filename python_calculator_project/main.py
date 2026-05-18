
from tkinter import *
from tkinter import messagebox, simpledialog
import math
import sqlite3

# Database setup
conn = sqlite3.connect("history.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS history (
    expression TEXT,
    result TEXT
)
''')

conn.commit()

root = Tk()
root.title("Prince Advanced Scientific Calculator")
root.geometry("550x750")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

expression = ""
logbase = 10  # Default log base

input_text = StringVar()
preview_text = StringVar()

input_frame = Frame(root, bg="#1e1e1e")
input_frame.pack(pady=10)

# Main input field
input_field = Entry(
    input_frame,
    font=('Arial', 22),
    textvariable=input_text,
    width=25,
    bd=5,
    relief=RIDGE,
    justify=RIGHT
)
input_field.grid(row=0, column=0, sticky="ew")
input_field.focus()

# Real-time preview field
preview_frame = Frame(root, bg="#2d2d2d", bd=2, relief=SUNKEN)
preview_frame.pack(pady=5, padx=20, fill=X)

Label(preview_frame, text="Preview: ", font=("Arial", 10), bg="#2d2d2d", fg="#888888").pack(side=LEFT, padx=5)
preview_label = Label(
    preview_frame,
    textvariable=preview_text,
    font=("Arial", 12),
    bg="#2d2d2d",
    fg="#00ff00"
)
preview_label.pack(side=LEFT, padx=5)

# Log base display
logbase_frame = Frame(root, bg="#1e1e1e")
logbase_frame.pack(pady=5)

logbase_text = StringVar(value="Log Base: 10")
Label(logbase_frame, textvariable=logbase_text, font=("Arial", 10), bg="#1e1e1e", fg="#ffaa00").pack()

def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)
    update_preview()

def clear():
    global expression
    expression = ""
    input_text.set("")
    preview_text.set("")

def equal():
    global expression
    try:
        result = str(eval(expression))
        cursor.execute(
            "INSERT INTO history VALUES (?, ?)",
            (expression, result)
        )
        conn.commit()

        input_text.set(result)
        expression = result
        preview_text.set("")
    except:
        messagebox.showerror("Error", "Invalid Expression")
        expression = ""
        input_text.set("")
        preview_text.set("")

def update_preview():
    """Real-time preview of calculation"""
    try:
        if expression:
            result = eval(expression)
            preview_text.set(f"= {result}")
        else:
            preview_text.set("")
    except:
        preview_text.set("")

def square_root():
    global expression
    try:
        result = str(math.sqrt(float(expression)))
        input_text.set(result)
        expression = result
        update_preview()
    except:
        messagebox.showerror("Error", "Invalid Input")

def log10_func():
    """Calculate logarithm base 10"""
    global expression
    try:
        num = float(expression)
        if num <= 0:
            messagebox.showerror("Error", "Logarithm of non-positive number is undefined")
            return
        result = str(math.log10(num))
        input_text.set(result)
        expression = result
        update_preview()
    except:
        messagebox.showerror("Error", "Invalid Input")

def ln_func():
    """Calculate natural logarithm (base e)"""
    global expression
    try:
        num = float(expression)
        if num <= 0:
            messagebox.showerror("Error", "Logarithm of non-positive number is undefined")
            return
        result = str(math.log(num))
        input_text.set(result)
        expression = result
        update_preview()
    except:
        messagebox.showerror("Error", "Invalid Input")

def log_custom_base():
    """Calculate logarithm with custom base"""
    global expression
    try:
        num = float(expression)
        if num <= 0:
            messagebox.showerror("Error", "Logarithm of non-positive number is undefined")
            return
        
        base = simpledialog.askfloat("Log Base", f"Enter base (current: {logbase}):", minvalue=1.1)
        if base and base != 1:
            result = str(math.log(num, base))
            input_text.set(result)
            expression = result
            update_preview()
    except:
        messagebox.showerror("Error", "Invalid Input")

def set_log_base():
    """Set custom logarithm base"""
    global logbase
    try:
        base = simpledialog.askfloat("Set Log Base", "Enter logarithm base:", minvalue=1.1)
        if base and base != 1:
            logbase = base
            logbase_text.set(f"Log Base: {base}")
    except:
        messagebox.showerror("Error", "Invalid Base")

def power_func():
    """Add power operator with real-time preview"""
    global expression
    expression += "**"
    input_text.set(expression)
    update_preview()

def factorial_func():
    """Calculate factorial"""
    global expression
    try:
        num = int(float(expression))
        if num < 0:
            messagebox.showerror("Error", "Factorial of negative number is undefined")
            return
        result = str(math.factorial(num))
        input_text.set(result)
        expression = result
        update_preview()
    except:
        messagebox.showerror("Error", "Invalid Input")

def sin_func():
    """Calculate sine (in degrees)"""
    global expression
    try:
        num = float(expression)
        result = str(math.sin(math.radians(num)))
        input_text.set(result)
        expression = result
        update_preview()
    except:
        messagebox.showerror("Error", "Invalid Input")

def cos_func():
    """Calculate cosine (in degrees)"""
    global expression
    try:
        num = float(expression)
        result = str(math.cos(math.radians(num)))
        input_text.set(result)
        expression = result
        update_preview()
    except:
        messagebox.showerror("Error", "Invalid Input")

def tan_func():
    """Calculate tangent (in degrees)"""
    global expression
    try:
        num = float(expression)
        result = str(math.tan(math.radians(num)))
        input_text.set(result)
        expression = result
        update_preview()
    except:
        messagebox.showerror("Error", "Invalid Input")

def percentage():
    global expression
    try:
        result = str(float(expression) / 100)
        input_text.set(result)
        expression = result
        update_preview()
    except:
        messagebox.showerror("Error", "Invalid Input")

def show_history():
    history_window = Toplevel(root)
    history_window.title("Calculation History")
    history_window.geometry("400x450")
    history_window.configure(bg="#1e1e1e")

    # Frame with scrollbar
    frame = Frame(history_window, bg="#1e1e1e")
    frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    text = Text(
        frame,
        font=("Arial", 11),
        bg="#2d2d2d",
        fg="#00ff00",
        yscrollcommand=scrollbar.set
    )
    text.pack(fill=BOTH, expand=True)
    scrollbar.config(command=text.yview)

    cursor.execute("SELECT * FROM history")
    rows = cursor.fetchall()
    
    for row in rows:
        text.insert(END, f"{row[0]} = {row[1]}\n")
    
    text.config(state=DISABLED)

# ==================== BUTTONS SECTION ====================

    for row in rows:
        text.insert(END, f"{row[0]} = {row[1]}\n")

# ==================== BUTTONS SECTION ====================
buttons_frame = Frame(root, bg="#1e1e1e")
buttons_frame.pack(pady=5)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = Button(
            buttons_frame,
            text=text,
            width=6,
            height=2,
            font=("Arial", 14, "bold"),
            bg="#00a86b",
            fg="white",
            command=equal
        )
    else:
        btn = Button(
            buttons_frame,
            text=text,
            width=6,
            height=2,
            font=("Arial", 14),
            bg="#333333",
            fg="white",
            command=lambda t=text: press(t)
        )

    btn.grid(row=row, column=col, padx=3, pady=3)

# ==================== SCIENTIFIC FUNCTIONS ROW 1 ====================
sci_frame1 = Frame(root, bg="#1e1e1e")
sci_frame1.pack(pady=8)

Button(
    sci_frame1,
    text="C",
    width=7,
    height=2,
    font=("Arial", 11, "bold"),
    bg="#ff4444",
    fg="white",
    command=clear
).grid(row=0, column=0, padx=2)

Button(
    sci_frame1,
    text="√",
    width=7,
    height=2,
    font=("Arial", 11),
    bg="#5555aa",
    fg="white",
    command=square_root
).grid(row=0, column=1, padx=2)

Button(
    sci_frame1,
    text="x²",
    width=7,
    height=2,
    font=("Arial", 11),
    bg="#5555aa",
    fg="white",
    command=power_func
).grid(row=0, column=2, padx=2)

Button(
    sci_frame1,
    text="%",
    width=7,
    height=2,
    font=("Arial", 11),
    bg="#5555aa",
    fg="white",
    command=percentage
).grid(row=0, column=3, padx=2)

Button(
    sci_frame1,
    text="n!",
    width=7,
    height=2,
    font=("Arial", 11),
    bg="#5555aa",
    fg="white",
    command=factorial_func
).grid(row=0, column=4, padx=2)

# ==================== LOGARITHMIC FUNCTIONS ====================
log_frame = Frame(root, bg="#1e1e1e")
log_frame.pack(pady=8)

Label(log_frame, text="Logarithmic Functions:", font=("Arial", 10, "bold"), bg="#1e1e1e", fg="#ffaa00").pack(side=LEFT, padx=5)

Button(
    log_frame,
    text="log₁₀",
    width=7,
    height=2,
    font=("Arial", 10),
    bg="#ff8844",
    fg="white",
    command=log10_func
).pack(side=LEFT, padx=2)

Button(
    log_frame,
    text="ln",
    width=7,
    height=2,
    font=("Arial", 10),
    bg="#ff8844",
    fg="white",
    command=ln_func
).pack(side=LEFT, padx=2)

Button(
    log_frame,
    text="logₓ",
    width=7,
    height=2,
    font=("Arial", 10),
    bg="#ff8844",
    fg="white",
    command=log_custom_base
).pack(side=LEFT, padx=2)

Button(
    log_frame,
    text="Set Base",
    width=8,
    height=2,
    font=("Arial", 10),
    bg="#cc6633",
    fg="white",
    command=set_log_base
).pack(side=LEFT, padx=2)

# ==================== TRIGONOMETRIC FUNCTIONS ====================
trig_frame = Frame(root, bg="#1e1e1e")
trig_frame.pack(pady=8)

Label(trig_frame, text="Trigonometric (degrees):", font=("Arial", 10, "bold"), bg="#1e1e1e", fg="#00ddff").pack(side=LEFT, padx=5)

Button(
    trig_frame,
    text="sin",
    width=7,
    height=2,
    font=("Arial", 10),
    bg="#00aa88",
    fg="white",
    command=sin_func
).pack(side=LEFT, padx=2)

Button(
    trig_frame,
    text="cos",
    width=7,
    height=2,
    font=("Arial", 10),
    bg="#00aa88",
    fg="white",
    command=cos_func
).pack(side=LEFT, padx=2)

Button(
    trig_frame,
    text="tan",
    width=7,
    height=2,
    font=("Arial", 10),
    bg="#00aa88",
    fg="white",
    command=tan_func
).pack(side=LEFT, padx=2)

# ==================== HISTORY & UTILITIES ====================
extra_frame = Frame(root, bg="#1e1e1e")
extra_frame.pack(pady=10)

Button(
    extra_frame,
    text="Show History",
    width=52,
    height=2,
    font=("Arial", 11, "bold"),
    bg="#0066cc",
    fg="white",
    command=show_history
).pack(pady=5)


root.mainloop()

conn.close()
