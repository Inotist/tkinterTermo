from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("1024x768")
        self.title("Mi ventana")
        self.configure(bg = "blue")
        
    def start(self):
        self.mainloop()


if __name__ == '__main__':
    app = mainApp()
    app.start()