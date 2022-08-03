# def bf_match(txt, pat):
#     pt = 0  # txt를 따라가는 커서
#     pp = 0  # pat를 따라가는 커서
#
#     while pt != len(txt) and pp != len(pat): # pt가 텍스트의 길이와 같지 않고, pp가 패턴의 길이와 같지 않을때
#         if txt[pt] == pat[pp]: # pt번째와 pp번째 값이 동일하다면 다음 인덱스도 같은 지 검사
#             pt += 1
#             pp += 1
#         else: # 값이 동일하지 않다면 pt - pp + 1의 인덱스 위치부터 다시 검사, pp는 0번째 인덱스부터 다시 검사
#             pt = pt - pp + 1
#             pp = 0
#
#     return pt - pp if pp == len(pat) else -1 # pp와 len(pat)와 동일하다면 pt - pp(찾은 인덱스 위치)를 반환하고, 아니라면(찾지 못했다면) -1을 반환
#
# if __name__ == "__main__":
#     s1 = input("텍스트를 입력하세요: ")
#     s2 = input("패턴을 입력하세요: ")
#
#     idx = bf_match(s1, s2)
#
#     if idx == -1:
#         print("텍스트 안에 패턴이 존재하지 않습니다.")
#     else:
#         print(f"{(idx + 1)}번째 문자가 일치합니다.")

# 각 문자열을 따라가는 커서를 선언
# 문자열[커서]가 0이 아닐때 동안 반복
# 만약 문자열[커서] == 문자열[커서]라면, +1
# 아니라면 pt = pt - pp + 1부터 진행
# 결과 반환은 만약 pp가 pat의 끝까지 비교했다면(전부 다 일치해서 pp의 길이와 같아진 상태) pt - pp를 반환
def bf_match(txt, pat):
    pt = 0
    pp = 0

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp + 1
            pp = 0

    return pt - pp if pp == len(pat) else -1

if __name__ == "__main__":
    print("문자열 검색을 실행합니다.")

    s1 = input("텍스트를 입력하세요.: ")
    s2 = input("패턴을 입력하세요.: ")

    idx = bf_match(s1, s2)

    if idx == -1:
        print("텍스트 안에 패턴이 존재하지 않습니다.")
    else:
        print(f"텍스트 안에 패턴이 {idx + 1}번째 존재합니다.")