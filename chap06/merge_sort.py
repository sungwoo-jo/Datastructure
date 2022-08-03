def merge_sort(array):
    def _merge_sort(arr, left, right):
        if left < right: # 최대로 분할할 수 있을 때까지 배열을 분할함
            center = (left + right) // 2 # 절반으로 나눈 인덱스 값

            _merge_sort(arr, left, center) # 배열 앞부분 병합 정렬
            _merge_sort(arr, center + 1, right) # 배열 뒷부분 병합 정렬

            p = j = 0 # buff의 포인터 p와 j에 0을 넣음
            i = k = left # arr의 포인터 i와 새로운 배열의 포인터 k에 left값을 넣음

            while i <= center: # 작업용 배열(buff)에 배열(arr)의 앞부분 복사
                buff[p] = arr[i]
                p += 1 # buff의 포인터 p 한 칸 이동
                i += 1 # arr의 포인터 i 한 칸 이동

            while i <= right and j < p: # arr의 포인터인 i는 center + 1부터 right까지(n - 1), buff의 포인터인 j는 p(배열의 앞부분 포인터)까지
                if buff[j] <= arr[i]: # 작업용 배열의 값(arr의 앞부분)이 arr의 뒷부분보다 작으면
                    arr[k] = buff[j] # arr의 첫번째 방부터 작은 값인 buff[j](배열의 앞부분)을 복사
                    j += 1 # buff의 포인터(j)를 한 칸 이동
                else: # 작업용 배열의 값(arr의 앞부분)이 arr의 뒷부분보다 크면
                    arr[k] = arr[i] # 작은 값인 arr의 뒷부분(arr[i])의 값을 복사
                    i += 1 # arr의 포인터(i)를 한 칸 이동
                k += 1 # 위 if 또는 else 과정을 마친 후 새로운 배열의 포인터도 한 칸 이동시켜줌

            while j < p: # 작업용 배열의 전체길이(p)보다 현재 포인터인 j가 작다면 == 작업용 배열에 원소가 남아있을 때
                arr[k] = buff[j] # 새로운 배열의 포인터 위치에 남은 buff의 원소를 복사
                k += 1 # 새로운 배열의 포인터 한 칸 이동
                j += 1 # buff의 포인터 한 칸 이동

    n = len(array)
    buff = [None] * n
    _merge_sort(array, 0, n - 1) # 배열, left값, right값 매개 변수로 전달
    del buff # 작업용 배열 소멸

if __name__ == "__main__":
    print("병합 정렬을 수행합니다.")
    num = int(input("원소 수를 입력하세요.: "))
    array = [None] * num

    for i in range(num):
        array[i] = int(input(f"array[{i}]: "))

    merge_sort(array)

    print("오름차순으로 정렬했습니다.")

    for i in range(num):
        print(f"array[{i}] = {array[i]}")