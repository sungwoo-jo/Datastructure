def select_value(arr, idx1, idx2, idx3):
    if arr[idx2] < arr[idx1]: arr[idx2], arr[idx1] = arr[idx1], arr[idx2]
    if arr[idx3] < arr[idx2]: arr[idx3], arr[idx2] = arr[idx2], arr[idx3]
    if arr[idx2] < arr[idx1]: arr[idx2], arr[idx1] = arr[idx1], arr[idx2]
    return idx2

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        tmp = arr[i]
        while j > 0 and arr[j - 1] > tmp:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = tmp

def qsort(arr, left, right):
    if right - left < 9: # 원소 수가 9 미만이면 단순 삽입 정렬로 전환
        insertion_sort(arr, left, right)
    else:
        pl = left # 왼쪽 포인터 pl
        pr = right # 오른쪽 포인터 pr
        middle = select_value(arr, pl, (pl + pr) // 2, pr) # 중앙값 인덱스 반환
        pivot = arr[middle]  # 피벗 pivot

        arr[middle], arr[pr - 1] = arr[pr - 1], arr[middle] # 중앙값과 pr - 1 값 교환
        pl += 1 # pl의 시작 위치 변경
        pr -= 2 # pr의 시작 위치 변경

        while pl <= pr:
            while arr[pl] < pivot: pl += 1
            while arr[pr] > pivot: pr -= 1
            if pl <= pr:
                arr[pl], arr[pr] = arr[pr], arr[pl]
                pl += 1
                pr -= 1

        if left < pr: qsort(arr, left, pr) # pr이 a[0]보다 오른쪽에 위치하면 왼쪽 그룹 나누기
        if pl < right: qsort(arr, pl, right) # pl이 a[8]보다 왼쪽에 위치하면 오른쪽 그룹 나누기

def quick_sort(arr):
    qsort(arr, 0, len(arr) - 1)

print("퀵 정렬을 수행합니다.")
num = int(input("원소 수를 입력하세요.: "))
array = [None] * num

for i in range(num):
    array[i] = int(input(f"array[{i}]: "))

quick_sort(array)

print("오름차순으로 정렬했습니다.")

for i in range(num):
    print(f"array[{i}] = {array[i]}")