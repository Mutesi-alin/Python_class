
    


def print_numbers(n):
    numners= range(n)
    for number in numbers:
        print(number)

def print_even_numbers(n):
    numbers= range(n)
    for number in numbers:
        if number %2==0:
            print(number)

def odd_or_even(n):
        numbers=range(n)
        for number in numbers:
            if  number %2==0:
                 print(f"{number} is even") 
            else: print(f"{number} is odd")

def  check_divisibility(n) :
     numbers= range(n)
     for number in numbers:
          if number%3==0:
               print(f"{number}is divisible by 3")  
          elif number%5==0:
               print(f"{number}is divisible by 5")  
          elif number %7==0:
               print(f"{number} is divisible by seven") 
          else: print(f"{number} is not divisible 3,5,7")   

def count_down(n):
     x=0
     while n>x:
          print(n)
          n-=1
def count_down(n):
     x=0
     while n>x:
          print(n)
          if n==5:
             break  
          n-=1

def divisible_by_seven(n):
    x=1
    while x<=n:
        x+=1
        if x%7!=0:
            continue

print(f"{x}is divisible by 7")


                   


 