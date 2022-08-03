def bm_match(txt, pat):
    skip_table = [None] * 256 # 건너뛰기 표

    # 건너뛰기 표 만들기
    for pt in range(256):
        skip_table[pt] = len(pat) # 패턴에 포함되지 않거나 패턴의 맨 끝 문자의 이동량인 4로 가장 먼저 skip_table을 초기화
    for pt in range(len(pat)):
        skip_table[ord(pat[pt])] = len(pat) - pt - 1 # 그 외 문자들은 패턴에 포함되고 맨 끝 문자가 아닌 경우이므로 패턴길이 - pt - 1로 초기화

    # 검색하기
    while pt < len(txt): # pt가 txt 길이보다 작을동안 (검색이 끝나지 않는 조건)
        pp = len(pat) - 1 # 가장 끝부터 비교하기 때문에 pp는 '패턴의 길이 - 1' 부터 시작
        while txt[pt] == pat[pp]: # 문자가 일치하는 경우
            if pp == 0: # pp가 첫 문자를 가리키고 있다면
                return pt # 반복을 끝내고 반환
            pt -= 1 # 앞 문자도 비교
            pp -= 1 # 앞 문자도 비교
        pt += skip_table[ord(txt[pt])] if skip_table[ord(txt[pt])] > len(pat) - pp \
            else len(pat) - pp

    return -1

if __name__ == "__main__":
    s1 = input("텍스트를 입력하세요.: ")
    s2 = input("패턴을 입력하세요.: ")

    idx = bm_match(s1, s2)

    if idx == -1:
        print("텍스트 안에 패턴이 존재하지 않습니다.")
    else:
        print(f"{idx + 1}번째 문자에서 일치합니다.")