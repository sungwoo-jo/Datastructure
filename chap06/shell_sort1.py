from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    n = len(a) # 배열의 전체 길이 저장
    h = n // 2 # 배열을 2로 나눈 몫 저장
    while h > 0: # h가 0보다 클 동안 진행



if __name__ == "__main__":
    print("----------셸 정렬을 수행합니다.----------")
    num = int(input("원소 수를 입력하세요.: "))
    x = [None] * num

    for i in range(num):
        x[i] = input(f"x[{i}]: ")

    shell_sort(x)

    print("----------셸 정렬이 완료되었습니다.----------")

    for i in range(num):
        print(f"x[{i}] = {x[i]}")


# 예시 원소 수: 8
# 예시 원소: 8, 1, 4, 2, 7, 6, 3, 5

# n = 8
# h = 4
# for i in range(h, n): i: [4], 5, 6, 7
# j = 0
# tmp = 4
