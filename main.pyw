import tkinter as tk
import ttkbootstrap as ttk
import numpy as np
from sympy import Matrix 

A = Matrix([[2, 3], [1, 4]])
I = A.inv()

def encrypt_msg(msg):
    msg_matrix = np.zeros((2, len(msg)))

    for i, char in enumerate(msg):
        msg_matrix[0, i] = ord(char)
        msg_matrix[1, i] = ord(char)

    encrypted_matrix = A * msg_matrix
    encrypted_msg = ''.join(chr(int(c)) for c in encrypted_matrix)

    result_label_var.set(f"Encrypted Message: {encrypted_msg[:len(encrypted_msg) // 2]}")
    result.set(f"{encrypted_msg[:len(encrypted_msg) // 2]}")

def decrypt_msg(encrypted_msg):
    encrypted_matrix = np.zeros((2, len(encrypted_msg)))

    for i, char in enumerate(encrypted_msg):
        encrypted_matrix[0, i] = ord(char)
        encrypted_matrix[1, i] = ord(char)

    decrypted_matrix = I * encrypted_matrix
    decrypted_msg = ''.join(chr(int(c)) for c in decrypted_matrix)

    result_label_var.set(f"Decrypted Message: {decrypted_msg[len(decrypted_msg) // 2 - len(text_var.get()):len(decrypted_msg) // 2]}")
    result.set(f"{decrypted_msg[len(decrypted_msg) // 2 - len(text_var.get()):len(decrypted_msg) // 2]}")

window = ttk.Window(themename = "journal")
window.title("Message Encryptor/Decryptor")
window.geometry("800x300")
window.resizable(False, False)

frame = ttk.Frame(window)
frame.pack(pady = 20)

label = ttk.Label(frame, text = "Enter your message")
label.grid(row = 0, column = 0, padx = 5)

text_var = tk.StringVar()
entry = ttk.Entry(frame, textvariable = text_var, width = 60)
entry.grid(row = 0, column = 1)

encrypt_button = ttk.Button(frame, text = "Encrypt", command = lambda: encrypt_msg(text_var.get()))
encrypt_button.grid(row = 1, column = 0, pady = 10)

decrypt_button = ttk.Button(frame, text = "Decrypt", command = lambda: decrypt_msg(text_var.get()))
decrypt_button.grid(row = 1, column = 1, pady = 10)

result = tk.StringVar()
result_label_var = tk.StringVar(value = "Result: ")

result_label = ttk.Label(window, textvariable = result_label_var, font = "consolas 12")
result_label.pack(pady = 20)

result_entry = ttk.Entry(window, textvariable = result, width = 80)
result_entry.pack(pady = 10)

window.mainloop()