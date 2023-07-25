# intersection  : tìm phần chung của set , list , dic, tuple . Có thể lấy giao 2 kiểu dữ liệu khác nhau
# tìm phần chung bằng " & " : phải cùng set , cùng list , cùng dic , cùng tuple

# vd
import json
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
lis = [1, 2, 3, 5]
tup = (1, 2, 3, 4)
set3 = set1.intersection(set2)
set4 = set1.intersection(lis)
set5 = set1.intersection(tup)
print(set3, "\n", set4, "\n", set5)

print(set1 & set2)


# difference  : rất đặc biệt : gioongs toan tu - ( tru) . chỉ áp dụng 2 kiểu dữ liệu giống nhau
# ví dụ :
set1 = {1, 2, 3, 4}
set2 = {3, 4, 10, -10}

set3 = set1.difference(set2)  # set1 - set2
set4 = set2.difference(set1)  # set2 - set1

print(set3, "\n", set4)

# hợp 2 kiểu dữ liệu : union . Có thể hợp 2 kiểu dữ liệu khác nhau
set1 = {1, 2, 3}
lst = {3, 4, 5}
set2 = {5, 6, 7}
set3 = set1.union(lst)
set4 = set1.union(set2)
set5 = set1.union(set2).union(lst)  # hợp nhiều cái với nhau
print(set3, "\n", set4)

print(set5)

# symmetric_difference : lấy các phần tử khác nhau của 2 tập hợp . có thể khác nhau
set3 = set1.symmetric_difference(set2)
set4 = set1.symmetric_difference(lst)
print(set3, "\n", set4)


# Dictionary
student = {
    "name": "Bob",
    "age": 20,
    "grades": [45, 57, 60, 99]
}
print(json.dumps(student, indent=4))  # indent :  khoang cach bang 4
value = student["name"]
print(value)  # "pop"

value1 = student.get("id", "Sv001")  # co the truyen them key ( name , age, ...) nhưng không thêm key đó vào dict
print(value1)  # Sv001
student["id1"] = "Sv002"  # them thi sinh 002
student["name"] = "Minh" # update gia tri
print(student) 

student.update(id = "Sv001") # thêm key = "id ", value = "Sv001"
