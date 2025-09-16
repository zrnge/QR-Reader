import tkinter as tk
from tkinter import filedialog, messagebox
import cv2

def read_qr(image_path):
    detector = cv2.QRCodeDetector()
    img = cv2.imread(image_path)
    if img is None:
        return None
    data, points, _ = detector.detectAndDecode(img)
    return data if data else None

def open_file():
    file_path = filedialog.askopenfilename(
        title="Select QR Code Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    if not file_path:
        return
    result = read_qr(file_path)
    if result:
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, result)
    else:
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, "⚠️ No QR code detected.")

def copy_to_clipboard():
    result = text_box.get("1.0", tk.END).strip()
    if result:
        root.clipboard_clear()
        root.clipboard_append(result)
        root.update()
        messagebox.showinfo("Copied", "✅ QR data copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "⚠️ No data to copy.")

# --- GUI setup ---
root = tk.Tk()
root.title("📷 QR Code Reader")
root.geometry("500x300")
root.configure(bg="#2E3440")  # dark theme background

# Styles
label_style = {"font": ("Arial", 13, "bold"), "bg": "#2E3440", "fg": "#D8DEE9"}
button_style = {"font": ("Arial", 11, "bold"), "bg": "#4C566A", "fg": "white", "activebackground": "#5E81AC", "activeforeground": "white"}

# Title
label = tk.Label(root, text="Select an image to read a QR code:", **label_style)
label.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root, bg="#2E3440")
btn_frame.pack(pady=5)

open_btn = tk.Button(btn_frame, text="📂 Open Image", command=open_file, **button_style, width=15)
open_btn.grid(row=0, column=0, padx=10)

copy_btn = tk.Button(btn_frame, text="📋 Copy Result", command=copy_to_clipboard, **button_style, width=15)
copy_btn.grid(row=0, column=1, padx=10)

# Result box
text_box = tk.Text(root, height=6, width=55, font=("Consolas", 11), bg="#3B4252", fg="#ECEFF4", insertbackground="white")
text_box.pack(pady=15)

root.mainloop()
