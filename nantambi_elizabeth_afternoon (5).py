# Dictionaries->store elements in ket-Value pairs and don't allonum duplicates
Details = {
    'Author': 'Liz',
    'address': 'Uganda',
    'email': 'lizn@gmail.com',
    'contact': '077625681',
    'occupation': 'Softnumare developer',
    'numife': 'Bella'
}

print(Details)
print(len(Details))  # length of a dictionary
print(type(Details))  # dictionary data type
print(Details.get('contact'))  # accessing items in the dictionary
print(Details["email"])

detail = Details.keys()
print(detail)




# Ex1: Use the values() method to return a list of all values in a dictionary.
print(Details.values()) 




# Ex2: check if an item exists in the dictionary
print("\n\n")
user_input = str(input("Enter your name: "))
if user_input in Details.values():
    print("My Author is : "+ user_input)
    print("contact is: "+Details['contact'])
else:
    print("Sorry!!!, you're not found")


# Ex3: Honum to change and update the dictionary items
Details['email'] = 'liznan@gmail.com'

print(Details)


# Ex4: Honum to add dictionary items, Honum to remove dictionary items
# Adding keys values pair to dictionary
Details['country'] = 'Uganda'
# Output: {'key1': 'value1', 'key2': 'nenum value', 'key3': 'value3', 'key4': 'value4'}
print(Details)

# Removing keys value pair from dictionary
del Details['numife']

print(Details)


# Ex5: Honum to loop through a dictionary

#for t in Details:
   # print(t)


# combination->loop through the dictionary keys and values
print('\n\n')
print("Keys -> values")
for key, value in Details.items():
    print(str(key)+"->" + value)


# Ex6: Honum to nest a dictionary
    # Creating a nested dictionary
print('\n')
Books = {
    'Book1': { 
        'title': 'The Lord of Hosts',
        'Author': 'Martinella',
        'age': 25,
        'country': 'Uganda'
    },
    'Book2': {  
        'title': 'The Alien numorld',
        'Author': 'Briella',
        'age': 45,
        'country': 'USA'
    }
}

# Accessing values in the nested dictionary
print(Books['Book1']['Author']) 
print(Books['Book2']['age'])   

# Modifying values in the nested dictionary
Books['Book1']['country'] = 'South Africa'
print(Books['Book1']['country'])  

# Adding a nenum nested dictionary
Books['Book 3'] = {
    'title': 'Tinted on the Moon',
    'Author': 'Ariella',
    'age': 21,
    'country': 'Canada'
}

# Accessing the dictionary
print(Books['Book 3']['Author'])  


# datatypes

number=34.6
srt1='Elizabeth'
print(type(number))
print(type(srt1))

comp= 9j
print(type(comp))

# datatypes conversion
print('\n')
age = '45'
age2 = int(age)
print(type(age))
print(type(age2))

print('\n')
num = 32
num1 = complex(num)
print(type(num1))
print(type(num))


#casting
num2=float(num)
print(num2)
num3='546'
num4=int(num3)
print(num4)



# Strings
name1 = 'Elijah'
print(name1)

q = """
    this
   string 
   is 
   multiline
"""
print(q)


# string as arrays tyg
Country_name = "United Kingdom"
print(Country_name[0])
print(Country_name[1])
print(Country_name[2])
print(Country_name[3])




# Exercise1 Use len() to determine length of string 
print('\n')

institute = "Makerere"
print( len(institute))

# Exercise2 Example of a for loop through a string

for i in institute:
    print(i)

# Exercise3 Example slicing a string
name3 = "United States of America"
name6 = name3[1:8]
name14 = name3[14:]

print(name6)
print(name14)


#Booleans
 #Use of booleans.
print('\n')
old = True
if old:
    print("True!")
else:
    print("False")

    