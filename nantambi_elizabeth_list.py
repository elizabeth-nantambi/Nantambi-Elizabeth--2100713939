Afternoon = ["Liz","olivia","elica","Hope","Elijah"]
#Accessing items in a list
print (Afternoon)
print (Afternoon[4])
print (Afternoon[0])
print (Afternoon[-2])

#Accessing a range if items
print(Afternoon[1:3])
print(Afternoon[0:4])


print(type(Afternoon))
length=len(Afternoon)
print(length) 

#Adding tos list
Afternoon.append("peter")
print (Afternoon)

#inserting into a list
Afternoon.insert(2,"Chris")
print (Afternoon)
Afternoon.insert(4,"Chris")
print (Afternoon)