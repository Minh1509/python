print(1 + 2)  # 3
print(1 - 2)  # -1
print(3 * 2)  # 6
print(3 ** 2)  # 9
print(3 / 2)  # 1.5
print(3 // 2)  # 1 ( int ) laay phan nguyen
print(3 % 2)  # 1     3 chia 2 du 1

print(3 > 2)  # True
print(3 < 2)  # False
print(3 == 2)  # False
print(3 != 2)  # True
print(3.0 == 3)  # True

print(True and True)  # True
print(True and False)  # False
print(1 and 2)


# and or not

# list: []
# set : set()
# dict (dictionary) : {}
# tuple : ()

# += , -= , *= , /= , //=, **= , %=

# ép kiểu
age = 30
tuoi = str(age)
print("Tuoi cua toi la :" + tuoi)
print("Tuoi: " + str(age))

# f-strings  or format() : chuyển luôn về chuỗi
print(f"Tuoi: {age}")

print("Tuoi : {}" .format(age))  # format(age) thay the vao dau ngoac nhon

# các hàm của chuôi
s = "heLLO worLD"
s1 = s.upper()  # HELLO : chuyển thành in hoa hết
s2 = s.capitalize()  # Hello : chữ đầu in hoa còn lại là chuyển thành in thường
s3 = s.title()  # Hello World : In hoa chữ cái đầu của từng từ . Phần còn lại chuyển thành in thường
# tách chuỗi : giống stringstream
s4 = s.split()  # ['hello' , 'world']
s5 = s.lower()  # hello world : viết thường tất cả chuỗi