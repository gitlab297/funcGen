def create_operation(operation):
    if operation == "div":
        def div(x, y):
            return x / y
        return div
    elif operation == "mul":
        def mul(x, y):
            return x * y
        return mul
my_func_add = create_operation("mul")
print('Задача 1: Фабрика функций')
print(my_func_add(10,5))



print('Задача 2: Лямбда')
exp = lambda x, y: x ** y
print(exp(10, 2))

def exp_def(x, y):
    return x ** y
print(exp_def(10, 2))



class Rect:
    def __init__(self, a):
       self.a = a
    def __call__(self, b):
       return self.a * b

s = Rect(10)
s2 = s(4)
print('Задача 3: Вызываемые объекты')
print(s2)
