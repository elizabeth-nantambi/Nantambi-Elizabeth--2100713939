

age = 20
if age < 18:
    print("You're underage")
elif age >= 18 or age <= 65:
    print("You're adult")
else:
    print("You're a senior citizen") 


#loops
#fruits = ["Mango","Orange","Cherry"]
#for i in fruits:
 #   print(i) 

#break and continue 

numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
for i in numbers: 
    if i == 10:
        break
    print(i) 

#continue
numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
for i in numbers: 
    if i == 10:
        continue
        print(i) 
#exception handling
try: 
    number=int(input("Enter a number= "))

    print(n)
except:
    print("Error")
finally:
    print("This code will always be executed") 




# Exercise
# mental health
print("\n\n")
# Prompt students on a scale of 1:10 to rate their mental health
health_status = {
    1: 'Excellent',
    2: 'Very good',
    3: 'Good',
    4: 'Above average',
    5: 'Average',
    6: 'Below average',
    7: 'Fair',
    8: 'poor',
    9: 'very poor',
    10: 'Critical',
}

try:
    response = int(input("On a scale of 1:10, rate your mental health: "))
    if response in health_status.keys():
        print("Your health is "+health_status[response])
    else:
        print("Out of range")

except ValueError:
    print("Only integers are allowed")
except Exception:
    print("Error occurances ")
finally:
    print("thanks for your response")




    