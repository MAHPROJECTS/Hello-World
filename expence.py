from tkinter import Tk, Frame, Button


class TkinterFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.initUI()  # Initialize the UI components

    def initUI(self):
        # Clear all widgets before adding new UI elements
        for widget in self.master.winfo_children():
            if not isinstance(widget, Button):  # Keep the existing buttons intact
                widget.destroy()  # Destroys the widgets before it

        Button(self.master, text="Refill Database", command=lambda: print("12312")).pack(pady=10)


def main():
    root = Tk()  # Use Tk class here
    root.geometry("250x150+300+300")
    app = TkinterFrame(root)
    app.pack()  # Pack the Frame into the main window
    root.mainloop()

if __name__ == '__main__':
    main()
