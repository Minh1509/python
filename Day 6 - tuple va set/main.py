#tuple 
tup1 = 1, 2, 3 #tuple 
tup2 = (1, 2, 3) # tuple
tup3= 1,  # tuple
tup4 = (4, )

# đánh dấu giống trong list
print(tup1[0], tup1[-1]) # 1, 3
#tup1[0] = 100 # sẽ bị lỗi do tuple không thể thay đổi giá trị

# cách thêm giá trị vào tuple
tup1 += 4,
print(tup1) # 1, 2, 3, 4

tup1 += (5, 6, 7)
print(tup1) # 1, 2, 3, 4, 5, 6 ,7



# set : chứa các phân tử khác nhau và các phần tử được sắp xếp theo thứ tự tăng dần ( các phần tử âm sẽ được sắp xếp phía sau các số duong ) . set có thể lưu số nguyên , chuỗi , ký tự .
set1 = set() # set trống
set1.add(2) # theem 1 gia tri vao set
set1.add(2)
set1.add(2)
set1.add(2)
print(set1) # {2} 

set1.update ([1, 2, 3, 5, 4])
print(set1) 


set1.remove(1) # xoa 1
print(set1) 

set2 = set1.copy()
print(set2 is set1) # false
print(set2 == set1) # true : noi dung giong nhau

set2.clear () # xóa mọi phần tử

# ktao 1 set cho truóc
set = {-7, 4, 1, 3, -10, -5, -23 }
print(set)
k=  set.pop()
print(k) # 1 : lấy phần tửu đầu tiên

