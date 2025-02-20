<<<<<<< HEAD
=======


import tkinter as tk

class ButtonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Button App")
        
        # Create three buttons
        self.button1 = tk.Button(self.root, text="Button 1", command=self.button1_action)
        self.button1.pack(pady=10)
        
        self.button2 = tk.Button(self.root, text="Button 2", command=self.button2_action)
        self.button2.pack(pady=10)
        
        self.button3 = tk.Button(self.root, text="Button 3", command=self.button3_action)
        self.button3.pack(pady=10)
        
    def button1_action(self):
        print("Hello World From Saleem")
        
    def button2_action(self):
<<<<<<< HEAD
        print("hello from h")

        print("Hello World From Humaira")

        
    def button3_action(self):
<<<<<<< HEAD
<<<<<<< HEAD
        print("ello from mahd")
=======
        print("Hello World From MahPooda")
>>>>>>> 356ad6c4ad8d6236de9158aa08aa897c5bc03be2
=======
        print("Hello World From MahLooda")
>>>>>>> dc3278ea8bfcdd599c51720ee209c9584231da65

# Create the main window
root = tk.Tk()

# Create an instance of the ButtonApp class
app = ButtonApp(root)

# Start the Tkinter event loop
root.mainloop()
