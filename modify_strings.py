a = "Let's Ride"
print(a.upper())

b = "Collect Moments Not Things"
print(b.lower())

c = " Travel is my therapy " #removes white space from the beginning or the end
print(c.strip())

d = "Good Ride"
print(d.replace("G", "F"))

e = "Long roads, deep thoughts" #The split() method returns a list where the text between the specified separator becomes the list items.
print(e.split(","))  

#The split() method splits the string into substrings if it finds instances of the separator

x = "Good Roads and"
y = "Beautiful Destiantion"
z = x + " " + y
print(z)