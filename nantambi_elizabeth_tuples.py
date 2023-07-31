#tuples are used to store items in a single variable
phone=("samsung", "iphone", "tecno")
print(phone) 

#Length of  a tuple
lenght=len(phone)
print(lenght) 


#data types in tuples
numbers=(1,2,3,4,5,6,7,8,9,10,11)
print(type(numbers))
print(type(phone))

#Accessing items in a tuple
print(numbers[1] )
print(numbers[5] )
print(numbers[4] )
print(numbers[6] )
 
#Adding items to a tuple
y=list(numbers)
y.append("21")
numbers=tuple(y) 
print(numbers)
y.insert(0,"56")
numbers=tuple(y)
print(numbers)

#concatenating tuples
phone_new=("Galaxy S9", )
phone += phone_new
print(phone)

#for loops
for i in phone:
    print(i)