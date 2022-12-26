# a simpel calculator made

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def mulitply(n1, n2):
  return n1 * n2

def devide(n1, n2):
  return n1 / n2

print(devide(10, 5))

operations = {
  "+": add,
  "-": subtract,
  "*": mulitply,
  "/": devide
}
def calculator():
    
    num1 = float(input('select first number: '))
    for key, value in operations.items():
        print(key)

    while True:
        operations_symbol = input('pick a operation symbol from the above: ')
        num2 = float(input('select second number: '))


        answear = operations[operations_symbol]
        answear1 = answear(num1, num2)

        print(f'{num1} {operations_symbol} {num2} = {answear1}')

        continue_stop = input("type 'n' to start new calculation or type 'y' to continue: ").lower()
        if continue_stop == 'n':
            calculator()
        else:
            num1 = answear1
            continue

calculator()