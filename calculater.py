def print_finel(fun):

    def inner(*args, **kwargs):
        var = fun(*args, **kwargs)
        return f"The total calculation sum is = {var}"
    return inner

def calculater(a, operation, b):
    try:
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        else:
            return a / b
    except Exception as e:
        return "Incorrect Input"


dct = {"+":"add", "-":"Minus", "*":"Multiply", "/":"Divider"}
@print_finel
def user_input():
    operation = input("Enter the operation = ")
    a = int(input(f"Enter the value to {dct.get(operation)} = "))
    b = int(input(f"Enter the value to {dct.get(operation)} = "))
    result = calculater(a,operation, b)
    run_cal = True
    while run_cal:
        print(f"The result {result}")
        operation = input("Enter the operation = ")
        b = input(f"Enter the value {dct.get(operation)} or Exit = ")
        if b == "exit":
            print(result)
            break
        else:
            result = calculater(result, dct.get(operation), int(b))
    return result

print(user_input())
