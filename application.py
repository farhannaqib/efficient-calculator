from tkinter import *
from calculator import solveeq


LIGHT_GRAY = "#f5f5f5"
BLACK = "#28282B"
WHITE = "#ffffff"

class Calculator:
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculator")

        self.eq = ""
        self.number = ""

        self.topframe, self.bottomframe = self.create_frames()
        self.equationLabel, self.numberLabel = self.create_top_labels()
        
        self.numberpad = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 1)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        
        self.bottomframe.rowconfigure(1, weight=1)
        for x in range(1,5):
            self.bottomframe.rowconfigure(x, weight=1)
            self.bottomframe.columnconfigure(x, weight=1)
        
        self.create_numbers()
        self.create_operators()
        self.create_other_buttons()
    
    def create_frames(self):
        topframe = Frame(self.window, bg=LIGHT_GRAY)
        topframe.pack(expand=True,fill="both")
        bottomframe = Frame(self.window, bg=LIGHT_GRAY)
        bottomframe.pack(expand=True,fill="both")

        return topframe, bottomframe
    
    def create_top_labels(self):
        equation = Label(self.topframe, text=self.eq, anchor=E, bg=LIGHT_GRAY, fg=BLACK, padx=12, font=("Arial", 16))
        equation.pack(expand=True,fill="both")

        number = Label(self.topframe, text=self.number, anchor=E, bg=LIGHT_GRAY, fg=BLACK, padx=24, font=("Arial", 25, "bold"))
        number.pack(expand=True,fill="both")
        return equation, number
    
    def create_numbers(self):
        for n, i in self.numberpad.items():
            button = Button(self.bottomframe, text=str(n), bg=WHITE, fg=BLACK, font = ("Arial", 20), borderwidth=0, command=lambda x=n: self.add_to_equation(x))
            if (n!=0): button.grid(row=i[0], column=i[1], sticky=NSEW)
            else: button.grid(row=i[0], column=i[1], columnspan= 2, sticky=NSEW)

    def create_operators(self):
        i=0
        for op, sym in self.operations.items():
            button = Button(self.bottomframe, text=str(sym), bg=WHITE, fg=BLACK, font = ("Arial", 20), borderwidth=0, command=lambda x=op: self.add_to_equation(x))
            button.grid(row=i, column=4, sticky=NSEW)
            i+=1
    
    def create_other_buttons(self):
        clearbutton = Button(self.bottomframe, text=str("C"), bg=WHITE, fg=BLACK, font = ("Arial", 20), borderwidth=0, command=lambda: self.clear())
        clearbutton.grid(row=0, column=1, columnspan=3 ,sticky=NSEW)
        equalsbutton = Button(self.bottomframe, text=str("="), bg=WHITE, fg=BLACK, font = ("Arial", 20), borderwidth=0, command=lambda: self.solve())
        equalsbutton.grid(row=4, column=3, columnspan=2 ,sticky=NSEW)
    
    def update(self):
        self.equationLabel.config(text=self.eq)
        self.numberLabel.config(text=self.number)

    def add_to_equation(self, value):
        self.eq += str(value)
        self.update()
    
    def solve(self):
        for op in self.operations.keys():
            x = self.eq.find(op)
            if x!=-1:
                self.number = solveeq(int(self.eq[:x]), op , int(self.eq[x+1:]))
                break
        if x == -1:
            self.number = self.eq
        self.eq = ""
        self.update()

    def clear(self):
        self.eq = ""
        self.number = ""
        self.update()
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()