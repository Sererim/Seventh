
class Calculator():
    
    def __init__(self) -> None:
        equation: str = ""
        save: dict = {int : str}
        answer: int = 0
        count = 0
        
        self.count = count
        self.equation = equation
        self.save = save
        self.answer = answer
        
    
    def message(self, foo: int) -> None:
        match foo:
            case 0:
                print(" Simple command line calculator.\n",
                      "Complex numbers must be entered like this:\n",
                      "[x + yj]\n Or program will return an error.\n",
                      "To use already entered eqaution press enter",
                      " and the number of the equation.\n"
                      " To terminate program at any time enter Y or y")
            case 1:
                print("Error syntax error!")
    
    def archive(self) -> bool:
        foo: str = ""
        
        for i in range(len(self.save)):
            foo = self.save.get(i)
            print(f"{i} : {foo}")
    
    def calculate(self) -> None:
        self.message(0)
        foo: int = 0
                
        while True:
            self.equation = input("Enter an equation.\n")
            
            if self.equation in ['Y', 'y']:
                break
            elif self.equation == "":
                print("To use already entered eqaution press enter",
                      " and the number of the equation.")
                foo = int(input())
                print(self.save.get(foo))
                self.equation = self.save.get(foo)
                for i in range(len(self.equation)):
                    if self.equation[i] == "=":
                        self.equation = self.equation[0 : i - 1]
                        break
                self.equation = f"({self.equation})" + input(f"({self.equation})")
            try:
                    
                
                self.answer = eval(self.equation)
                self.count += 1
                self.save[self.count] = f"{self.equation} = {self.answer}"
                Calculator.archive(self)
            except SyntaxError:
                Calculator.message(self, 1)
                pass
        return True
                

def main() -> int:
    calc = Calculator()
    calc.calculate()
    
    return 0


if __name__ == "__main__":
    main()
