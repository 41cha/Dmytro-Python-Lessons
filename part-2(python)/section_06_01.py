def new_year_greeting():
    print('hello world \nhave a nice day \ngood christmas')

new_year_greeting()

print('-------------------------------------------------------------------')




def print_user_details(name, age, city):
    print(f"Ім'я: {name}, Вік: {age}, Місто: {city}")

print_user_details('Vova', '18', 'Vinitsya')

print('-------------------------------------------------------------------')




def describe_pet(pet_name, animal_type='dog'):
    print(f'animal type is {animal_type}\npet name is {pet_name}')

describe_pet('bobik')

print('-------------------------------------------------------------------')




def calculate_discount(price, discount=0.1):
    return price * discount
new_price = calculate_discount(1000)

print(new_price)

print('-------------------------------------------------------------------')



def convert_temperature(temperature=25):
    return temperature * 9/5 + 32, temperature + 273.15

new_temp = convert_temperature()
print(new_temp)

print('-------------------------------------------------------------------')



import statistics

def calculate_statistics(numbers=[1, 2, 3, 2, 5, 6]):
    return statistics.mean(numbers), statistics.median(numbers), statistics.stdev(numbers)

mean, median, stdev = calculate_statistics()
print(mean)
print(median)
print(stdev)
    
print('-------------------------------------------------------------------')



def create_profile(name, age, email, nickname):
    print(f'my name is {name}, i`m {age} years old, my email is {email}, my nickname is {nickname}')

create_profile('vova', '18', 'dfsgdfg', '41cha')

print('-------------------------------------------------------------------')



def max_number(*args):
    currmax = 0
    for i in args:
        for x in args:
            if i < x:
                currmax = x
            else:
                continue
    print(currmax)

max_number(1, 2, 23, 3, 4)

print('-------------------------------------------------------------------')



def about_me(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


about_me(name="Іван", age=30, hobby="футбол")

print('-------------------------------------------------------------------')
print('-------------------------------------------------------------------')
print('-------------------------------------------------------------------')

#корисно
def gen_func():
    for x in range(5):
        yield x**2
generator = gen_func()

for value in gen_func():
    print(value)

print('-------------------------------------------------------------------')
print('-------------------------------------------------------------------')
print('-------------------------------------------------------------------')

def lambda_func(n, callback):
    lambda_square = lambda x: x ** 2
    square = lambda_square(n)
    callback(square)

def print_result(square):
    print(f"Result is {square}")

lambda_func(3, print_result)

print('-------------------------------------------------------------------')



def apply_operation(n, callback):
    result = n + n
    callback(result)

def print_apply_operation(result):
    print(f'result is {result}')

apply_operation(5, print_apply_operation)

print('-------------------------------------------------------------------')



def fibonachi(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonachi(n - 1) + fibonachi(n - 2)
    
print(fibonachi(12))

print('-------------------------------------------------------------------')



def debug_info(func):
    def wrapper(*args):
        func_args = args
        result = func(*args)
        print(f'{func.__name__}, args: {func_args}, result: {result}')
        return result
    return wrapper


@debug_info
def fibonachi(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibonachi(n - 1) + fibonachi(n - 2)

print(fibonachi(13))

print('-------------------------------------------------------------------')

import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.5f} seconds to run.")
        return result
    return wrapper

@timer_decorator
def about_me(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

about_me(name="Іван", age=30, hobby="футбол")

print('-------------------------------------------------------------------')

def ms_or_s_decorator(in_sec=True):
    def timer_decorator(func):
        if in_sec == True:
            def wrapper_in_sec(*args, **kwargs):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                print(f"{func.__name__} took {end_time - start_time:.5f} seconds to run.")
                return result
            return wrapper_in_sec
        else:
            def wrapper_in_ms(*args, **kwargs):
                start_time = time.time() * 100
                result = func(*args, **kwargs)
                end_time = time.time() * 100
                print(f"{func.__name__} took {end_time - start_time:.5f} miliseconds to run.")
                return result
            return wrapper_in_ms
    return timer_decorator

@ms_or_s_decorator(False)
def say_hello():
    print("Hello!")

say_hello()

print('-------------------------------------------------------------------')

# 3 Написати декоратор кешування відповіді по параметрам для довільної функції перевірити скільки буде виконуватись по часу з ним і без нього