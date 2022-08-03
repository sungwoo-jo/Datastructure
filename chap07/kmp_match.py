def kmp_match(txt, pat):
    pt = 1 # txt를 따라가는 커서
    pp = 0 # pat를 따라가는 커서
    skip_table = [0] * (len(pat) + 1) # 건너뛰기 표(skip table)

    # 건너뛰기 표(skip table) 만들기
    skip_table[pt] = 0
    while pt != len(pat): # pt가 len(pat)와 같다면 검색이 종료된 것
        if pat[pt] == pat[pp]: # 패턴[pt]와 패턴[pp]가 같다면 계속 비교
            pt += 1
            pp += 1
            skip_table[pt] = pp # skip 테이블에 다시 시작하는 값 작성
        elif pp == 0: # 일치하는 문자열이 없다면 패턴 오른쪽으로 1칸 밀기
            pt += 1
            skip_table[pt] = pp # 0 대입
        else:
            pp = skip_table[pp]

    # 문자열 검색하기
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip_table[pp]

    return pt - pp if pp == len(pat) else -1

if __name__ == "__main__":
    print("문자열 검색을 시작합니다.")

    s1 = input("텍스트를 입력하세요.: ")
    s2 = input("패턴을 입력하세요.: ")

    idx = kmp_match(s1, s2)

    if idx == -1:
        print("텍스트 안에 패턴이 존재하지 않습니다.")
    else:
        print(f"텍스트안에 문자열이 {idx + 1}번째 위치에 있습니다.")