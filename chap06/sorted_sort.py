print("sorted( ) 함수를 사용하여 정렬합니다.")
num = int(input("원소 수를 입력하세요.: "))
array = [None] * num

for i in range(num):
    array[i] = int(input(f"array[{i}]: "))

# 배열 array를 오름차순 정렬
array = sorted(array)
print("오름차순으로 정렬했습니다.")
for i in range(num):
    print(f"array[{i}] = {array[i]}")

# 배열 array를 내림차순 정렬
array = sorted(array, reverse = True)
print("내림차순으로 정렬했습니다.")
for i in range(num):
    print(f"array[{i}] = {array[i]}")