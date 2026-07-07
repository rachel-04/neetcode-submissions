import math

class AreaCalc:
   def calculate(self, length: float, width: float = None)-> float:
    if width == None:
        result = math.pi* length**2
        finalresult = round(result,2)
        return finalresult
    elif length == None:
        result = math.pi* width**2
        finalresult = round(result,2)
        return finalresult
    else:
        result = length * width
        return result

    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
