#Ex1
#1
names_of_people = ["Liz","olivia","elica","Hope","Elijah"]
print(names_of_people[1]) 
#2
names_of_people[0]='Tinah'
print(names_of_people)
#3
names_of_people.append('Marianne') 
print(names_of_people)  
#4
names_of_people.insert(3,'Bathel') 
print(names_of_people)
#5
names_of_people.remove("Hope")
print(names_of_people) 
#6
print(names_of_people[-1])

#7
countries = ['United States','Uganda','Belarus','Kuwait','Kenya','Kiribati','Tanzania']
print(countries[2:5])
#8
print(countries.copy()) 
#9
for country in countries:
    print(country) 
#10
#Ascending
animals=['pig', 'cow', 'sheep','goat']
print(sorted(animals)) 

#descending
print(sorted(animals,reverse=True)) 
#11
for name in animals:
    if 'a' in name: 
        print(name) 
#12
fname=['Nantambi']
lname=['Elizabeth']
print(fname+lname)
print('\n================================================================')
#exercise2
print( 'Exercise 2')

x=('samsung','iphone','tecno','redmi')
#1
print(x[0]) 
#2
print(x[-2]) 
#4
y=list(x)
y.append('huawei')
x=tuple(y)
print(x)

#3
z=list(x)
z[1]='itel'
x=tuple(z)
print(x) 
#5
for i in x:
    print(i)  
#6
t=list(x) 
t.pop(0)
x=tuple(t)
print(x)
 
#7
cities = tuple(["Kampala", "Entebbe", "Gulu", "Jinja", "Mbarara"])
print(cities)  
#8
#unpacking
city1, city2, city3, city4, city5 = cities

# Printing the unpacked values
print(city1)
print(city2)
print(city3)
print(city4)
print(city5)
 
#9
print(cities[1:4])

#10
first_name = ('Nantambi',)
last_name = ('Elizabeth',)
con= first_name+last_name
print(con) 


#11
colors=('blue', 'green', 'black')
print(colors*3) 

#12
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

print(thistuple.count(8)) 

print('\n================================================================')
print( 'Exercise 3')

#Ex3
#1
fav_bev = set(["coffee", "juice"])
print(fav_bev)
#2
fav_bev.add("soda")
fav_bev.add("tea")
print(fav_bev)

#3
mySet = {"oven", "kettle", "microwave", "refrigerator"}

print("microwave" in mySet)
#4
mySet.remove("kettle")
print(mySet)
#5
for item in mySet:
    print(item)
#6
mySet = {1, 2, 3, 4}
myList = [5, 6]
mySet.update(myList)
print(mySet)
#7
my_name={'Nantambi Elizabeth'}
my_age={20} 
print(my_name.union(my_age))

print('\n================================================================')

print( 'Exercise 4')


#Ex4
#1
num=100
name='Liz'
print(name + str(num)) 
#2
txt = " Hello, Uganda! "
output = txt.strip()  
#print(output)
print(output.replace(" ", "")) 
#3
upper = txt.upper()
print(upper)
#4
rep = txt.replace('U', 'V')
print(rep)
#5
y = "I am proudly Ugandan"
print(y[1:4])
#6
c="All 'Data Scientists' are cool!"
print(c)
print('\n================================================================')

print( 'Exercise 5')
#ex5
Shoes = {
'brand' : 'Nick',
'color' : 'black',
'size' : 40
} 
#1
print(Shoes["size"])
#2
Shoes["brand"]="Adidas"
print(Shoes["brand"])
#3
Shoes["type"] = "sneakers"
print(Shoes) 
#4
print(Shoes.keys()) 

#5
print(Shoes.values()) 

#6
if "size" in Shoes:
    print("exists")
print("size" in Shoes) 
#7
for i in Shoes:
    print(i)

#8
del Shoes["color"]
print(Shoes) 

#9
print(Shoes.clear())
print(Shoes) 

#10
Details = {
    'name': 'Liz',
    'address': 'Uganda',
    'email': 'lizn@gmail.com',
    'contact': '077625681',
    'occupation': 'Softnumare developer'
    
}

copy_of= Details.copy()
print(copy_of) 

#11
Details2 = {
    'Liz':{
    'name': 'Liz',
    'address': 'Uganda',
    'email': 'lizn@gmail.com',
    'contact': '077625681',
    'occupation': 'Softnumare developer'
    
} 
    'Olivia':{
        'name': 'Olivia',
        'address': 'Uganda',
        'email': 'olivian@gmail.com',
        'contact': '077625782',
        'occupation': ' networker'
    } 
}