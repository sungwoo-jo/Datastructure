def merge_sorted_list(a, b, c):
    pa, pb, pc = 0, 0, 0 # 각 배열의 커서
    na, nb, nc = len(a), len(b), len(c) # 각 배열의 길이

    while pa < na and pb < nb: # 배열의 길이보다 작을동안만 수행
        if a[pa] <= b[pb]: # a[pa]의 값이 b[pb]의 값보다 이하라면
            c[pc] = a[pa] # c 배열에 작은 값(a[pa])을 복사
            pa += 1 # pa를 한 칸 이동
        else: # 반대로 a[pa]의 값이 b[pb]의 값보다 크다면: a[pa] > a[pb]
            c[pc] = b[pb] # c 배열에 작은 값(b[pb])을 복사
            pb += 1 # pb를 한 칸 이동
        pc += 1 # if와 else문을 거친 다음에는 pc도 한칸 이동시켜줌

    # 한 배열이라도 복사가 완료되었다면, 나머지 배열도 남은 값을 복사함
    while pa < na: # a배열의 원소가 남아있을 때
        c[pc] = a[pa] # c배열에 a배열 남은 원소를 복사
        pa += 1 # pa 한 칸 이동
        pc += 1 # pc 한 칸 이동

    while pb < nb: # b배열의 원소가 남아있을 때
        c[pc] = b[pb] # c배열에 b배열 남은 원소를 복사
        pb += 1 # pb 한 칸 이동
        pc += 1 # pc 한 칸 이동

if __name__ == "__main__":
    a = [1, 2, 4, 5, 7]
    b = [3, 6, 8, 9]
    c = [None] * (len(a) + len(b))
    print("정렬을 마친 두 배열의 병합을 수행합니다.")

    merge_sorted_list(a, b, c)

    print("배열 a와 b를 병합하여 배열 c에 저장합니다.")
    print(f"배열 a: {a}")
    print(f"배열 b: {b}")
    print(f"배열 c: {c}")