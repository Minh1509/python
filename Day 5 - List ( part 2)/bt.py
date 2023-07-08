friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]

new_list_1 = friends [0:4 :1]
new_list_2 = friends[-4 ::]
print(new_list_1, "\n", new_list_2) 

new_list= friends[::-1]
print(new_list)
new_list_3 = friends[0:len(friends):1]
print("\n", new_list_3)

new_list_4= friends.copy();
print("\n", new_list_4)

new_list_5 = friends[2 : len(friends)-1:1]
print(new_list_5)
