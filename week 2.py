# week 2
#functions
def greet():
    print('Hi, How are you?')
    
greet()

def greet(user):
    print(f'Hi {user}, you ran great.')
    
greet('Usharbudha')

def fav_book(user,book):
    print(f"{user} likes to read {book}")
    
fav_book('Usharbudha','Fiction')

def add(a,d):
    c=a+d
    return c

sol=add(1,2)
sol

add(1)

def div(a,b=1):
    return a/b

div(2)
div(10,3)

def greet(*users):
    for user in users:
        print(f"Hi {user}")
        
greet('Usharbudha','Dev')

def summation(*numbers):
    summation=0
    for number in numbers:
        summation = summation+number
    return summation
    

def summation(*numbers):
    summation=0
    check=0
    for number in numbers:
        summation = summation+number
        check+=1
        print(check)
        return summation
    
summation(7,4,5,6,7,8,9)


def greet(**users):
    print(users)

greet(name='Usharbudha Dev', age=23)


def greet(**users):
    for keys,values in users.items():
        print(f"His {keys} is (values)")
        
greet(name='Usharbudha Dev', age=23)


def factorial(n):
    if n==0:
        return 1
    else:
        recursive=factorial(n-1)
        result=n*recursive
        return result

factorial(6)

def fibo(n):
    if n==0:
        return 1
    if n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

for i in range(0,10):
    print(fibo(i))
        
fibo(8)

x=4
def example():
    print(x)
    z=5
    print(z)

example()

print(z)  #will give an error, because its defind inside a function

x=6
def example2():
    print(x)
    print(x+5)
    x+=6   #you cannot cange the value
    print(x)

example2()


import summation1 as s
s.summation(2,3,4,5,6,7)

def simple_gen():
    yield 'Oh'
    yield 'Hello'
    yield 'There'
    
for i in simple_gen():
    print(i)

correct_combo=(3,4,5)
count=0
for i in range(0,9):
    for o in range(0,9):
        for p in range(0,9):
            count=count+1
            if(i,o,p)==correct_combo:
                print('Correct combination found')
                print(i,o,p)
print(count)

#MORE EFFICENT WAY
def combo_gen():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                yield(i,j,k)
    
for (i,j,k) in combo_gen():
    print(i,j,k)
    if (i,j,k)==correct_combo:
        print('Found Combo: {}'.format((i,j,k)))
        break


names=['Usharbudha Dev','Usharbudha Dev','Usharbudha Dev']
grades=[50,60,70]
a=list(zip(names,grades))
print(a)

for names,grades in zip(names,grades):
    print(f'{names} scored {grades}')

x=[1,2,3,4]
y=[5,6,7,8]
z=['q','w','e','r']

[print(x,y,z) for x,y,z in zip(x,y,z)]
print(x)


#EXCEPTION HANDLING
x=int(input("ENTER A NUMBER="))
try:
    x=int(input("ENTER A NUMBER="))
except ValueError:
    print("Oops! That's not valid. Enter Again")


from collections import OrderedDict
my_dict={'a':1,'b':2}
print(my_dict)
Ordered_dict=OrderedDict(my_dict)
print(Ordered_dict)

from collections import defaultdict
ice_cream=defaultdict(lambda:"CHOCOLATE")
ice_cream['SRAH']='VANILLA'
print(ice_cream['SRAH'])
print(ice_cream['Abdul'])

r=lambda x,y:x**y
r(4,3)


from collections import Counter
my_count=Counter(['a','b','c','a','c'])
my_count

my_count.update(["a","c"])
my_count

my_count.subtract('c')
my_count['a']=1
my_count
my_count.clear()
my_count

from collections import namedtuple
user=namedtuple('user','name age gender')
a=user(name='Usharbudha Dev',age=23,gender='M')
print(a)

















