import tkinter as tk
import random
import string

class RandomPasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")

        self.password = tk.Label(root, text="Generated Password:")
        self.password.pack()

        self.password_var = tk.StringVar()
        self.password_enter = tk.Entry(root, textvariable=self.password_var)
        self.password_enter.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

    def generate_password(self):
        password_length = 12  # You can adjust the desired password length
        characters = string.ascii_letters + string.digits + string.punctuation
        generated_code = ''.join(random.choice(characters) for _ in range(password_length))
        self.password_var.set(generated_code)

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomPasswordGenerator(root)
    root.mainloop()
