import tkinter as tk
import asyncio

class Main(tk.Frame):
    
    _buttons = (
        "C", "DEL", "*", "=", "/",
        "1", "2", "3", "-", "+",
        "4", "5", "6", "x^3", "x^n",
        "7", "8", "9", ",", "j", "(",
         "0", ")", "x^2"
    )
    
    def __init__(self, root):
        super(Main, self).__init__(root)
        archive: dict = {int : str}
        count: int = 0
        
        self.archive = archive
        self.count = count 
        self.make()
        
    def make(self) -> None:
        self.equation = "0"
        self.lable = tk.Label(text=self.equation, font=("Calibri", 21),
                              bg="mint cream", foreground="black")
        self.lable.place(x = 10, y = 40)
        
        x: int = 10
        y: int = 80
        
        for button in self._buttons:
            compute = lambda par = button: self.logic(par)
            tk.Button(text = button, bg = "light blue",
                      font = ("Calibri", 15), command=compute).place(x = x, y = y,
                                                                   width = 45,
                                                                   height = 30)
        else:
            x += 48
            if x > 210:
                x = 10
                y += 31
    
    def logic(self, button: str) -> None:
        full_eq: str = ""
        
        if button == "C":
            self.equation = ""
        elif button == "DEL":
            self.equation = self.equation[0:-1]
        elif button == "x^2":
            self.equation = f"({self.equation})**2"
            full_eq = self.equation
            self.equation = str(eval(self.equation))
            Main.archive(self,full_eq)
        elif button == "x^3":
            self.equation += f"({self.equation})**3"
            full_eq = self.equation
            self.equation = str(eval(self.equation))
            Main.archive(self,full_eq)
        elif button == "=":
            full_eq = self.equation
            self.equation = str(eval(self.equation))
            Main.archive(self,full_eq) 
        else:
            if self.equation == "0":
                    self.equation = ""
            self.equation += button
        self.update()
            
    def update(self) -> None:
        
        if self.equation == "":
            self.equation = "0"
        self.lable.configure(text = self.equation)
    
    def archive(self, full_eq) -> None:
        self.count += 1
        full_eq = f"{full_eq} = {self.equation}"
        self.archive[self.count] = full_eq


if __name__ == "__main__":
    root = tk.Tk()
    root["bg"] = "mint cream"
    root.title("Калькулятор")
    root.geometry("480x240+200+200")
    application = Main(root)
    application.pack()
    root.mainloop()