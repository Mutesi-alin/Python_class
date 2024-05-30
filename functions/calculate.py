def add(x,y):
    result=x+y
    return result

def substract(a,b):
    result=a-b
    return result


def multiply(a,b):
    result=a*b
    return result

def remainder(a,b):
    result= a/b
    return result

def power(a,b):
    result=a**b
    return result
# adding alot of numbers;
def sum(*numbers):
    total= 0
    for  number in numbers:
        total += number
    return total

def multiply_many(*numbers):
    total=1
    for number in numbers:
        return 
    

    #keyword one asteriok before the paramenter it returns a dictionary using two aster

def create_sentence(**words):
    sentence="" 
    for word in words.values():
        sentence += word
        sentence += " "
        return sentence


def sum_and_greet(*args,**kwargs):
    total= 0
    for  x in args:
        total += x
    f= kwargs["first_name"]
    l= kwargs["last_name"]
    greeting= f" hello {f},{l}, the sum of your number is {total}"
    return greeting