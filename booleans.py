a = 100
b = 40

if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")    

print(bool("My Cars"))
print(bool(26))

#The bool() function allows you to evaluate any value, and give you True or False in return

x = "My Garage"
y = 54
print(bool(x))
print(bool(y))

#Almost any value is evaluated to True if it has some sort of content
#Any string is True, except empty strings.
#Any number is True, except 0
#Any list, tuple, set, and dictionary are True, except empty ones

print(bool(0))
print(bool(""))

#One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False
class mylass():
    def __len__(self):
        return 0
    
myobj = mylass()
print(bool(myobj))    


#You can execute code based on the Boolean answer of a function
def myFunction():
    return True

if myFunction():
    print("Yes")
else:
    print("No")