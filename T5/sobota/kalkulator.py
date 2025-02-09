import math

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def dodawanie(self):
        return self.a + self.b

    def odejmowanie(self):
        return self.a - self.b
    
    def mnozenie(self):
        return  self.a * self.b
    
    def dzielenie(self):
        print(self.a / self.b)
    
    def pierwiastek(self):
        print(math.sqrt(self.a))

    def potega(self):
        return math.pow(self.a, self.b)
    

kalkulator_1 = Kalkulator(10,2)
print(kalkulator_1.dodawanie())
print(kalkulator_1.odejmowanie())
print(kalkulator_1.mnozenie())
print(kalkulator_1.dzielenie())
print(kalkulator_1.potega())
print(kalkulator_1.pierwiastek())
