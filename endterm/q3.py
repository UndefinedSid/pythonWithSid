class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def __mul__(self, other):
        real_part = (self.real * other.real) - (self.imaginary * other.imaginary)
        imaginary_part = (self.real * other.imaginary) + (self.imaginary * other.real)
        return ComplexNumber(real_part, imaginary_part)

    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real} - {-self.imaginary}i"
        return f"{self.real} + {self.imaginary}i"


real1 = int(input("Enter real part of first complex number: "))
imaginary1 = int(input("Enter imaginary part of first complex number: "))
real2 = int(input("Enter real part of second complex number: "))
imaginary2 = int(input("Enter imaginary part of second complex number: "))

number1 = ComplexNumber(real1, imaginary1)
number2 = ComplexNumber(real2, imaginary2)

print("First complex number:", number1)
print("Second complex number:", number2)
print("Addition:", number1 + number2)
print("Multiplication:", number1 * number2)
