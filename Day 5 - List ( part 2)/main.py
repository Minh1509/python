# list in list
# copy list
# list slicing => newlist

# 1
friends = [['pop', 23], ['mike', 25], ['nam'], 26]
print(type(friends))

# 2
lst1 = [1, 3, 2]
lst2 = lst1
# is
print(lst1 is lst2)  # true
print(lst1 == lst2)  # true
print("\n")
lst2 = lst1.copy()
print(lst1 is lst2) # false
print(lst1 == lst2) # true

#3 
a = [1 , 3, 2, 4 , 5]
new_lst1 = a[0:2:1] # bat dau -> ket thuc  -> buoc nhay
print(new_lst1)

new_lst2 = a[0:4 :2]
print(new_lst2)

