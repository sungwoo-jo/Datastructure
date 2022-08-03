from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    for i in range()

if __name__ == "__main__":
    print("삽입 정렬 수행합니다.")
    num = int(input("원소의 개수를 입력하세요.: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x{[i]} = "))

    insertion_sort(num)

    print("오름차순으로 정렬했습니다.")

    for i in range(num):
        print(f"x[{i}]: {x[i]}")