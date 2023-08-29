# integers

from ast import Expression


a = 1233450958483989793920893290749783940509509304989387489767862675678678940909039403899589759875980985095093095039049283872864762784
print(f"{a}")

b = a+11
type(10)
type(b)
print(f"{a = } {b = }")

print(f"{a, 'is of type' }", type(a))
print(f"{a, 'is integer?'}", isinstance(a, int))


# integers arthmetic
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9

print(f"{a + b}") # (c- d) (e*f) (g/h)
print(a <= b)


# operation
x = 17
y = 3
 
print(x/y) # // %

a =0O10 
print(f"Value: {a} \n Type: {type(a)}")

b = 0X10
print(F"Value: {b} \n type: {type(b)}")

C = 0B001
print(f"value: {c} \n type: {type(c)}")

# floating point numbers
# 7.94
# type(7.94)
# .56
# 56.
# 2.6e-5

a = 0.98498787878378
print(a,"is of type", type(a))
print(a,"is of float?", isinstance(a, float))


# Operation floats
print(int(1.3)) # (1.7) (-1.3) (-1.7)

# round(float_number [, ndigits=])
float_numb1 = 10.60 # 10.40, 10.343, 10.34555
round_result = round(float_numb1 , 2 ) 
print(f"{round_result} Value:")


num = -12.8
num1 = -1.5
result_num1 = round(num)
print(f"Values rounding is: {result_num1}")
print("The absolute value is:", abs(num), "and the sign is:", num /abs(num) )

# COMPLEX NUMBERS
print(3.0 + 9j)
print(type(3.0+9j))


a = complex(3.1,9)
b = complex(1,2)

 
print("a =   ", a) 
# Real part = (a.real)
# Imaginary Part = (a.imag)
# Complex Conjugate = (a.conjugate())

# ("a/b= ", a/b) ("a*b= ", a*b)
print("a*a= ", a*a) 



#  Booleans
true= True # 123
false= False
# FALSE
print(type(true))

my_book = 5 > 8
print('My book', my_book,'\n')
# False

print(bool(Expression))
print(Expression)

# x == y
# x != y
# x >y
# x < y
# x >= y
# x <= y


print(3==4) # (3!=4) x > y ect 
print(bool(3==4))


# strings
print("welcome to home (\'* character.") # ! (') (").(\'*)
print('ABC')
print('a\
    b\
        c') # a b c
print('foo\\bar') # (\n) (r'\')  (\\) (R'\\' )
# a\ \b \f \n \n{} \r \t \uxxxx \uxxxxx \v \ooo \xhh
print("a\t\t\tb") # a   b
print("\u0061\u007c\u006e")
print("\141", "\x61")
print('\u23124 \N{rightwards arrow}')



# Triple Quotes

print(""" this string has a single (') and a double (") quotes.""")
string1 = """
This is the first line of text.
across several lines""" 

print(string1.format())

# Accessing values in strings
strings2= "wpjmkmkdmn mnkmkem  enkmnfkk nkejkkmmk."



# print("{0} {1}".format(name, age), end="\n"*2)

print(string1[3:10]) # ( [3:15:1]) ([2:15:2]) ([-2])
print("love "in string1) # not in 

# stringing is immutable.
# using id()
id_before_string1  = id(string1)
print(id_before_string1)
# string1[8] = 't'


strings = string1[0:8]+'t'+string1[9:]
print(string1)

id_before_string1 = id(string1)
print(id_before_string1)

string3 = string1 + " " + strings2[0] + " " + strings2[11:]
print(string3)

# capitalize()
"fungcs towwe".capitalize()

# lower and upper()
"fundh dkf".lower()
"kdjubhd hdw".upper()

# split()
"sjnjf jnjdnu".capitalize().split()
" i want to take you to said hey".split("u")

csv_string = "Dog,  Cat, Spam, Defenestrate, 1, 3.1415 \n\t"

# strip()
csv_string.strip()

# lstrip()
csv_string.lstrip()

clean_list  = [x.strip() for x in csv_string.split(",")]

# join()
print(",".join(clean_list))
print(",".join(clean_list))
print("\t".join(clean_list))

# replace()
alt_csv = csv_string.strip().replace(',', '')
print(alt_csv)

# index()
s = "My search bay"
s.index("y")
s.count("y")

# find()
s.find("y", 2)
s[s.find("fusnd "):]

len(s)

number = "123897"
print(number.isnumeric())

letters = "MyABcE"
print(letters.isnumeric())

movie = "2001: A Sammy Odissey"
book = "A Thousand Splendid Sharks"
poem = "sammy lived in a pretty how town"

print(movie.islower())
print(movie.isupper())
print(movie.startswith("20"))
print(movie.endswith("sSEY"))

print(book.istitle())
print(book.isupper())

print(poem.istitle())
print(poem.islower())

value0 = "Saturday"
value1 = "Groovy"

f" {value0} {value1} ..."
print('On {}, I feel {}'.format(value0, value1))
print(f'On {value0}, I fell {value1}')
print(f'On {0}, I fell {1}'.format(value0, value1))
print(f'On {0}, I fell {0}'.format(value0, value1))
print(f'On {value0},  I fell  {value0}')

print('{}'.format(value0*3))
print(f'{value0*0}')
print(f'{value0*-1}')
print(f'{value0!r}')


'{desire} to {place}'.format(desire="Fly me", place='the Look')
'{desire} to {place} or else I wont vistit {place}.'.format(\
    desire='Fly me', place='the Look')

a = {"desire": "I want to take you", "place": "ffks tiew"}
'{desire} to {place}'.format(**a)

a = 3.12456
f"{a:03.2f}" == "{:03.2f}".format(a)
"{0:03.2f}".format(a, 42)
"{1:03.2f}".format(a,42)

c = 2334
"int: {0:d} hex: {0:x} oct: {0:o} bin {0:b}".format(c)
f"int: {c:d} hex: {c:x} oct: {c:o} bin: {c:b}"


# convert to Integer
v1 = int(2.7)
v2 = int(-3.9)
v3 = int("2")
v4 = int("11", 16)
v5 = int(false)
print(v1,v2,v3,v4,v5)

# convert Float
v6 = float(2)
v7 = float("2.7")
v8 = float(false)
vA = float(True)
print(v6,v7,v8,vA)


# convert to string
vB = str(4.5)
vC = str(True)
print(vB, vC, type(vC))

# convert to boolean
vD = bool(0) # False
vE = bool(3)
vF = bool("htsThs")
vG = bool(list())
print(vD, vE, vF, vG)

init1 = 4
float1 = init1 + 2.1
str1 = "My int: "+ str(init1)

int2 = 4 + True 
print("float1 = {} \n str1 = {} \n".format(float1, str1, int2))


age = 21
sign = "You must be {}-years-old to enter this bar".format(age)
print(sign)

x = float(input("Give me a number: "))
print(x)

s = "hey there! what should this string be?"
print(f"the fist occurence of the letter a = {len(s)}")

print(f"the first occurence of the letter a = {s.index('a')}")

print(f"a occurs {s.count(r'a')} times")
