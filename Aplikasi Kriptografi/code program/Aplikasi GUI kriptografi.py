import tkinter as tk
from tkinter import ttk

# Fungsi untuk mengenkripsi dan mendekripsi dengan Shift Cipher


def shift_cipher(text, key, mode):
    if key.isnumeric() and int(key) >= 0 and int(key) < 26:
        key = chr(int(key) + 97)
    elif key.isnumeric() and int(key) >= 26:
        key = str(int(key) % 26)
        key = chr(int(key) + 97)
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord(key) - \
                ord('a') if key.islower() else ord(key) - ord('A')
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 +
                              65) if mode == "Encrypt" else chr((ord(char) - shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 +
                              97) if mode == "Encrypt" else chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result

# Fungsi untuk mengenkripsi dan mendekripsi dengan Vigenere Cipher


def vigenere_cipher(text, key, mode):
    result = ""
    key_idx = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_idx % len(key)]) - ord('a') if key[key_idx %
                                                                   len(key)].islower() else ord(key[key_idx % len(key)]) - ord('A')
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 +
                              65) if mode == "Encrypt" else chr((ord(char) - shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 +
                              97) if mode == "Encrypt" else chr((ord(char) - shift - 97) % 26 + 97)
            key_idx += 1
        else:
            result += char
    return result

# Fungsi untuk mengenkripsi dan mendekripsi dengan Substitution Cipher


def substitution_cipher(text, key, mode):
    if mode == "Encrypt":
        return text.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", key.lower()))
    else:
        return text.translate(str.maketrans(key.lower(), "abcdefghijklmnopqrstuvwxyz"))

# Fungsi untuk mengenkripsi dan mendekripsi dengan Transposition Cipher


def transposition_cipher(text, key, mode):
    if mode == "Encrypt":
        num_cols = len(key)
        num_rows = -(-len(text) // num_cols)  # Round up division
        null_char = chr(0)
        plaintext_matrix = [list(
            text[i*num_cols:(i+1)*num_cols].ljust(num_cols, null_char)) for i in range(num_rows)]
        key_order = sorted(range(num_cols), key=lambda k: key[k])
        result = ""
        for col in key_order:
            result += "".join([plaintext_matrix[row][col]
                              for row in range(num_rows)])
        return result.replace(null_char, "")
    else:
        num_cols = len(key)
        num_rows = -(-len(text) // num_cols)  # Round up division
        null_char = chr(0)
        ciphertext_matrix = [list(
            text[i*num_rows:(i+1)*num_rows].ljust(num_rows, null_char)) for i in range(num_cols)]
        key_order = sorted(range(num_cols), key=lambda k: key[k])
        result = ""
        for row in range(num_rows):
            result += "".join([ciphertext_matrix[col][row]
                              for col in key_order])
        return result.replace(null_char, "")

# Fungsi untuk mengeksekusi enkripsi atau dekripsi saat tombol "Encrypt" atau "Decrypt" ditekan


def execute_cipher():
    text = input_text.get("1.0", "end-1c")
    key = key_entry.get()
    mode = mode_var.get()
    cipher_type = cipher_var.get()
    if cipher_type == "Shift Cipher":
        result = shift_cipher(text, key, mode)
    elif cipher_type == "Vigenere Cipher":
        result = vigenere_cipher(text, key, mode)
    elif cipher_type == "Substitution Cipher":
        result = substitution_cipher(text, key, mode)
    elif cipher_type == "Transposition Cipher":
        result = transposition_cipher(text, key, mode)
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", result)


# Membuat tampilan GUI
root = tk.Tk()
root.title("Cryptography")

# Membuat pilihan tipe cipher
cipher_var = tk.StringVar()
cipher_var.set("Shift Cipher")
cipher_label = ttk.Label(root, text="Cipher Type:")
cipher_label.grid(row=0, column=0, sticky="W")
shift_cipher_radio = ttk.Radiobutton(
    root, text="Shift Cipher", variable=cipher_var, value="Shift Cipher")
shift_cipher_radio.grid(row=1, column=0, sticky="W")
vigenere_cipher_radio = ttk.Radiobutton(
    root, text="Vigenere Cipher", variable=cipher_var, value="Vigenere Cipher")
vigenere_cipher_radio.grid(row=2, column=0, sticky="W")
substitution_cipher_radio = ttk.Radiobutton(
    root, text="Substitution Cipher", variable=cipher_var, value="Substitution Cipher")
substitution_cipher_radio.grid(row=3, column=0, sticky="W")
transposition_cipher_radio = ttk.Radiobutton(
    root, text="Transposition Cipher", variable=cipher_var, value="Transposition Cipher")
transposition_cipher_radio.grid(row=4, column=0, sticky="W")

# Membuat input teks dan output teks
input_label = ttk.Label(root, text="Input Text:")
input_label.grid(row=0, column=1, sticky="W")
input_text = tk.Text(root, height=10)
input_text.grid(row=1, column=1, rowspan=3)
output_label = ttk.Label(root, text="Output Text:")
output_label.grid(row=0, column=2, sticky="W")
output_text = tk.Text(root, height=10)
output_text.grid(row=1, column=2, rowspan=3)

# Membuat label dan entry untuk kunci
key_label = ttk.Label(root, text="Key:")
key_label.grid(row=4, column=1, sticky="W")
key_entry = ttk.Entry(root)
key_entry.grid(row=4, column=2)

# Membuat pilihan enkripsi atau dekripsi
mode_var = tk.StringVar()
mode_var.set("Encrypt")
mode_label = ttk.Label(root, text="Mode:")
mode_label.grid(row=5, column=0, sticky="W")
encrypt_radio = ttk.Radiobutton(
    root, text="Encrypt", variable=mode_var, value="Encrypt")
encrypt_radio.grid(row=6, column=0, sticky="W")
decrypt_radio = ttk.Radiobutton(
    root, text="Decrypt", variable=mode_var, value="Decrypt")
decrypt_radio.grid(row=7, column=0, sticky="W")

# Membuat tombol "Encrypt" dan "Decrypt"
execute_button = ttk.Button(
    root, text="Encrypt/Decrypt", command=execute_cipher)
execute_button.grid(row=8, column=1, columnspan=2)

root.mainloop()
