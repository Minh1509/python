# list co the chua số và ki tự hoặc chuỗi
numbers1 = [1,2, 3, 'a', "em" ]
print(numbers1)
numbers = [1, 2,2, 3, 3, 5]  # giong mang
# chi so :  0  1  2  3
#chi so am: -4 -3 -2 -1
print(type(numbers))  # list
print(numbers)  # [1, 2, 3, 5]
print(numbers[0])  # 1
print(numbers[-1]) # 5

numbers.append(100) # them gia tri 100 vao cuoi list
print(numbers)

numbers.remove(1) # xóa phần tử đầu tiên có giá trị 1 . Chỉ 1 phần tử đầu tiên gặp bị xóa
print(numbers)

last_value = numbers.pop()  # xóa 1 giá trị cuối cùng của list và gán giá trị đó cho last_value
print(numbers)

del numbers[3] # xoa di 1 gia tri bang 3
print(numbers)
numbers.extend([2.5, 1000, 100, 123]) # them vao cuối list ban đầu và trở thành một list mới
print(numbers)

cnt = numbers.count(1)  # trả về số lượng mà giá trị đó xuất hiện

# numbers.clear() # xóa 
cnt1 = len(numbers) # chieu dai cua list *: khong the viet numbers.len()

#insert : chen gia tri vao 1 vi tri bat ki
numbers.insert(0, 1000)  #vị trí chèn là 0 và giá trị là 1000

#index : tra ve chi so cua gia trị mình chuyền vào hàm index
index_of_2 = numbers.index(2) 

#reverse : dao nguoc list
numbers.reverse() # ko viet dc reverse(numbers)  
print(numbers)

#sort : sap xep tang , giam và list chỉ chứa 1 kiểu dữ liệu
numbers.sort() # sap xep theo gia tri tang dan
print(numbers)
numbers.sort(reverse = True) # sap xep theo gia tri giam dan
print(numbers)

# max , min: gia tri lon nhat , nho nhat trong list và list chỉ có 1 kiểu dữ liệu
max_value = max(numbers)
min_value = min(numbers)
print(max_value, min_value)
# neu nhu mot ngay 
min_value = max(numbers)
