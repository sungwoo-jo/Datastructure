from typing import MutableSequence

def heap_sort(arr):
    def down_heap(arr, left, right):
        temp = arr[left] # 루트 값

        parent = left
        while parent < (right + 1) // 2: # 부모 노드가 자식

if __name__ == "__main__":
    print("힙 정렬을 수행합니다.")
    num = int(input("원소 수를 입력하세요.: "))
    array = [None] * num

    for i in range(num):
        array[i] = int(input(f"array[{i}]: "))

    heap_sort(array)

    print("오름차순으로 정렬했습니다.")
    for i in range(num):
        print(f"array[{i}] = {array[i]}")