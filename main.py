import tkinter as tk
from tkinter import ttk, messagebox

# ─── Main Application Window ───────────────────────────────────────────────────

# Create the root window (the main application window)
root = tk.Tk()
root.title("My Tkinter App")          # Set window title
root.geometry("400x350")              # Set window size (width x height)
root.resizable(True, True)            # Allow resizing in both directions

# ─── Styling ───────────────────────────────────────────────────────────────────

# Configure a simple color scheme
BG_COLOR = "#f0f4f8"
BTN_COLOR = "#4a90d9"
root.configure(bg=BG_COLOR)

# ─── Header Label ──────────────────────────────────────────────────────────────

# A label is a widget that displays static text or images
header = tk.Label(
    root,
    text="Welcome to My App",          # Text to display
    font=("Helvetica", 16, "bold"),    # Font family, size, style
    bg=BG_COLOR,                       # Background color (match window)
    fg="#2c3e50"                       # Foreground (text) color
)
header.pack(pady=15)                   # Pack places widget; pady adds vertical spacing

# ─── Entry Widget (Text Input) ─────────────────────────────────────────────────

# Frame to group the label + entry horizontally
input_frame = tk.Frame(root, bg=BG_COLOR)
input_frame.pack(pady=5)

# Label next to the input field
name_label = tk.Label(input_frame, text="Your Name:", bg=BG_COLOR, font=("Helvetica", 11))
name_label.pack(side=tk.LEFT, padx=5)  # side=LEFT places widgets left-to-right

# Entry widget for single-line text input
name_entry = tk.Entry(input_frame, width=22, font=("Helvetica", 11))
name_entry.pack(side=tk.LEFT, padx=5)
name_entry.insert(0, "e.g. Muhammad")  # Pre-fill placeholder text

# ─── Dropdown (OptionMenu) ─────────────────────────────────────────────────────

dropdown_frame = tk.Frame(root, bg=BG_COLOR)
dropdown_frame.pack(pady=5)

dropdown_label = tk.Label(dropdown_frame, text="Select Role:", bg=BG_COLOR, font=("Helvetica", 11))
dropdown_label.pack(side=tk.LEFT, padx=5)

# StringVar holds the currently selected dropdown value
selected_role = tk.StringVar(value="Student")

# OptionMenu creates a dropdown from a list of choices
role_menu = ttk.Combobox(
    dropdown_frame,
    textvariable=selected_role,
    values=["Student", "Engineer", "Researcher", "Other"],
    state="readonly",                  # Prevent typing custom values
    width=18
)
role_menu.pack(side=tk.LEFT, padx=5)

# ─── Checkbutton ───────────────────────────────────────────────────────────────

# IntVar stores the checkbox state: 1 = checked, 0 = unchecked
notify_var = tk.IntVar(value=0)

checkbox = tk.Checkbutton(
    root,
    text="Subscribe to notifications",
    variable=notify_var,               # Link to IntVar
    bg=BG_COLOR,
    font=("Helvetica", 10)
)
checkbox.pack(pady=8)

# ─── Output Label ──────────────────────────────────────────────────────────────

# This label will be updated dynamically when the button is clicked
output_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 11, "italic"),
    bg=BG_COLOR,
    fg="#27ae60",
    wraplength=360                     # Wrap text if it exceeds this pixel width
)
output_label.pack(pady=5)

# ─── Button Callback Function ──────────────────────────────────────────────────

def on_submit():
    """Called when the Submit button is clicked."""
    name = name_entry.get().strip()    # Get text from entry, remove whitespace
    role = selected_role.get()
    notify = "Yes" if notify_var.get() == 1 else "No"

    # Basic validation — show a warning dialog if name is empty
    if not name or name == "e.g. Muhammad":
        messagebox.showwarning("Input Error", "Please enter your name!")
        return

    # Update the output label with the collected info
    output_label.config(
        text=f"Hello, {name}! Role: {role} | Notifications: {notify}"
    )

def on_clear():
    """Clears all inputs back to defaults."""
    name_entry.delete(0, tk.END)       # Delete from index 0 to end
    name_entry.insert(0, "e.g. Muhammad")
    selected_role.set("Student")
    notify_var.set(0)
    output_label.config(text="")

# ─── Buttons ───────────────────────────────────────────────────────────────────

btn_frame = tk.Frame(root, bg=BG_COLOR)
btn_frame.pack(pady=12)

# Submit button — triggers on_submit() when clicked
submit_btn = tk.Button(
    btn_frame,
    text="Submit",
    command=on_submit,                 # Function to call on click
    bg=BTN_COLOR,
    fg="white",
    font=("Helvetica", 11, "bold"),
    padx=12, pady=4,
    relief=tk.FLAT,                    # Flat style (no 3-D border)
    cursor="hand2"                     # Show pointer cursor on hover
)
submit_btn.pack(side=tk.LEFT, padx=8)

# Clear button — resets all fields
clear_btn = tk.Button(
    btn_frame,
    text="Clear",
    command=on_clear,
    bg="#e74c3c",
    fg="white",
    font=("Helvetica", 11, "bold"),
    padx=12, pady=4,
    relief=tk.FLAT,
    cursor="hand2"
)
clear_btn.pack(side=tk.LEFT, padx=8)

# ─── Status Bar ────────────────────────────────────────────────────────────────

# A label anchored to the bottom acts as a simple status bar
status_bar = tk.Label(
    root,
    text="Ready",
    bd=1,                              # Border width
    relief=tk.SUNKEN,                  # Sunken border style
    anchor=tk.W,                       # Align text to the West (left)
    font=("Helvetica", 9),
    bg="#dce3ea"
)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)  # fill=X stretches across full width

# ─── Start the Event Loop ──────────────────────────────────────────────────────

# mainloop() keeps the window open and listens for events (clicks, key presses, etc.)
# Nothing after this line runs until the window is closed
root.mainloop()