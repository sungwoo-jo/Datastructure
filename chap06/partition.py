def partition(arr):
    n = len(arr) # 배열의 길이 n
    pl = 0 # 왼쪽 포인터 pl
    pr = n - 1 # 오른쪽 포인터 pr
    pivot = arr[n // 2] # 배열의 중앙 값 pivot

    while pl <= pr: # pl이 pr과 같거나 작을 동안 수행(두 개의 그룹으로 나눔)
        while arr[pl] < pivot: pl += 1 # pl이 피벗보다 작다면 1칸 이동
        while arr[pr] > pivot: pr -= 1 # pr이 피벗보다 크다면 1칸 이동
        if pl <= pr: # 서로 교차한 상태가 아니라면
            arr[pl], arr[pr] = arr[pr], arr[pl] # a[pl]과 a[pr]의 값을 스왑
            pl += 1 # pl 1칸 이동
            pr += 1 # pr 1칸 이동

    print(f"피벗은 {pivot}입니다.")

    print("피벗 이하인 그룹입니다.")
    print(*arr[0 : pl]) # arr[0] ~ a[pl - 1]

    if pl > pr + 1:
        print("피벗과 일치하는 그룹입니다.")
        print(*arr[pr + 1 : pl]) # arr[pr + 1] ~ arr[pl - 1]

    print("피벗 이상인 그룹입니다.")
    print(*arr[pr : n]) # arr[pr] ~ arr[n - 1]

if __name__ == "__main__":
    print("배열을 나눕니다.")
    num = int(input("원소 수를 입력하세요.: "))
    array = [None] * num

    for i in range(num):
        array[i] = int(input(f"x[{i}] = "))

    partition(array)