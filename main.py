from tkinter import *
from tkinter import ttk

class mainApp(Tk):
    __temperaturaAnt = ""
    
    def __init__(self):
        Tk.__init__(self)
        self.title("Termómetro")
        self.geometry("210x150")
        self.configure(bg="#ECECEC")
        self.resizable(0,0)
        
        self.temperatura = StringVar(value="")
        self.temperatura.trace("w", self.validateTemperature)
        self.tipoUnidad = StringVar(value="C")
        
        self.createLayout()
        
    def createLayout(self):
        self.entrada = ttk.Entry(self, textvariable=self.temperatura).place(x=10, y=10)
        
        self.lblUnidad = ttk.Label(self, text="Grados").place(x=10, y=45)
        self.rbF = ttk.Radiobutton(self, text="Fahrenheit", variable=self.tipoUnidad, value="F", command=self.selected).place(x=20,y=70)
        self.rbC = ttk.Radiobutton(self, text="Celsius", variable=self.tipoUnidad, value="C", command=self.selected).place(x=20, y=95)
        
    def start(self):
        self.mainloop()
        
    def validateTemperature(self, *args):
        nuevoValor = self.temperatura.get()
        try:
            float(nuevoValor)
            self.__temperaturaAnt = nuevoValor
        except ValueError:
            if nuevoValor == "" or nuevoValor == "-":
                self.__temperaturaAnt = nuevoValor
            else: self.temperatura.set(self.__temperaturaAnt)
            
    def selected(self):
        try:
            grados = float(self.temperatura.get())
            if self.tipoUnidad.get() == 'F': self.temperatura.set(grados * 9/5 + 32)
            elif self.tipoUnidad.get() == 'C': self.temperatura.set((grados - 32) * 5/9)
        except ValueError as e: print(e, "introduce un número primero")
        
        
if __name__ == '__main__':
    app = mainApp()
    app.start()