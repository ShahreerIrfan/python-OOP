class Calculator:
    brand = 'Casio'
    def add(self, num1, num2):
        return num1 + num2

c1 = Calculator()
print("Enter 2 numbers: ")
numbr1 = int(input())
numbr2 = int(input())
result = c1.add(numbr1, numbr2)
print(result)

# num = int(input())
# print(num)