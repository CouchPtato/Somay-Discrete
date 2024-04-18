import numpy as np

def  evaluate_polynomial(degree):
    coeffpolynomial = np.array([])

    for i in range(degree + 1):
        coeff = float(input(f'Enter coefficient x^{i}: '))
        coeffpolynomial = np.append(coeffpolynomial, coeff)

    print('\nCoefficients: ', coeffpolynomial)

    x = float(input('Enter the value of the variable for which the value of the polynomial is to be found:'))

    value = 0
    for i in range(degree+1):
        value += coeffpolynomial[i]*(x**i)

    print(f'Value of polynomial with coefficients{coeffpolynomial} at {x} is :', value)

def main():
    degree = int(input("Enter the highest degree of your polynomial: "))

    print()
    evaluate_polynomial(degree)
    
if __name__ == "__main__":
    main()