set1={"red","green","blue","yellow"}
print(set1)



#Length of a set
length_set=len(set1)
print(length_set)


#Accessing Elements in a set
for s in set1:
    print(s) 


#checking for presence of an element in a set
print("red" in set1)


#data type
print(type(set1))

#Adding to a set
set1.add("Purple")
print(set1) 


#Adding two sets together
set2={"Clive","Elisha","Petra"}
print(set1.union(set2))