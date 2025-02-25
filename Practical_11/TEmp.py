def func(a,b=100,c=3.14):
    return a+b+c

print(func(10))
print(func(20,50))
print(func(30,60,6.28))

def print_it(*args):
    print()
    for var in args:
        print(f"{var}",end=" ")

print_it(10)
print_it(10,3.14)
print_it(10,3.14,'Sicilian')
print_it(10,3.14,'Sicillian','Punekar')

