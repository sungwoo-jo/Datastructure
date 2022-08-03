from __future__ import annotations

class Node: # 연결 리스트용 노드 클래스
    def __init__(self, data, next): # 초기화
        self.data = data # 데이터
        self.next = next # 뒤쪽 포인터

class LinkedList: # 연결 리스트 클래스
    def __init__(self): # 초기화
        self.no = 0 # 노드의 개수
        self.head = None # 머리 노드
        self.current = None # 주목 포인터

    def __len__(self):
        return self.no # 연결 리스트의 노드 개수를 반환

    def search(self, data): # data와 값이 같은 노드를 검색
        cnt = 0 # 검색에 성공했을 때 노드의 순번(몇번째 원소를 스캔중인지)
        ptr = self.head # 머리 노드부터 검색을 시작
        while ptr is not None: # ptr이 None이 아닌 경우(꼬리 노드가 아닌 경우)에 반복. None이면 스캔할 노드가 존재하지 않음
            if ptr.data == data: # data와 값이 같은 노드 검색에 성공한 경우
                self.current = ptr # 주목 포인터에 현재 ptr 저장
                return cnt # 검색에 성공한 노드의 번호를 반환
            cnt += 1 # 원소의 순번 증가
            ptr = ptr.next # 다음 노드를 스캔함
        return -1 # 검색에 실패한 경우 -1 반환

    def __contains__(self, data): # 연결 리스트에 data가 포함되어 있는 지 확인
        return self.search(data) >= 0 # 리스트에 data와 값이 같은 노드가 포함되어 있는지 판단

    def add_first(self, data): # 맨 앞에 노드를 삽입
        ptr = self.head # 삽입하기 전의 머리 노드를 저장

        # 삽입할 노드를 생성해서 데이터에는 data를 넣고, 뒤쪽 포인터는 ptr(삽입하기 전 머리노드)이 됨. head는 삽입한 노드를 참조.
        self.head = self.current = Node(data, ptr)
        self.no += 1 # 노드의 개수 1 증가

    def add_last(self, data): # 맨 뒤에 노드를 삽입
        if self.head is None: # 리스트가 비어 있으면
            self.add_first(data) # 맨 앞에 노드를 삽입
        else: # 리스트가 비어있지 않으면
            ptr = self.head # 삽입하기 전의 머리 노드를 저장
            while ptr.next is not None: # ptr의 다음 노드가 None이 아닐 때, 즉 ptr.next가 꼬리 노드가 아닐때
                ptr = ptr.next # ptr이 참조하는 곳을 그 뒤쪽 포인터로 계속해서 업데이트 함 -> while문이 종료될 때 ptr은 결국 꼬리노드를 참조하게 됨
            # 노드를 삽입하는데 data, None으로 생성해서 주목 포인터 current에 담고, 현재 꼬리노드의 뒤쪽 포인터 ptr.next가 참조하는 곳이 새로 삽입한 노드가 되도록 업데이트함
            ptr.next = self.current = Node(data, None)
            self.no += 1 # 노드의 개수 1 증가

    def remove_first(self): # 맨 앞의 노드를 삭제
        if self.head is not None: # 리스트가 비어 있지 않을 때
            # 이후 노드에 대한 참조인 head.next를 머리 노드에 대한 참조인 head에 대입하여 head가 참조하는 곳과 주목 포인터 current가 참조하는 곳도 업데이트
            self.head = self.current = self.head.next
        self.no -= 1

    def remove_last(self): # 맨 뒤의 노드를 삭제
        if self.head is not None: # 리스트가 비어 있지 않을 때
            if self.head.next is None: # 노드가 1개 뿐일 때
                self.remove_first() # self.remove_first 함수 호출하여 머리 노드를 삭제
            else: # 노드가 2개 이상 존재할 때
                ptr = self.head # 스캔 중인 노드
                pre = self.head # 스캔 중인 노드의 앞쪽 노드

                while ptr.next is not None: # 스캔 중인 노드의 다음 포인터가 비어 있지 않을 때, while문이 종료될 때 ptr은 결국 꼬리노드를 참조하게 됨
                    pre = ptr # 맨 끝에서 2번째 노드가 담김(맨 끝 바로 이전 노드)
                    ptr = ptr.next # 맨 끝 노드가 담김
                pre.next = None # 맨 끝에서 2번째 노드의 next에 None을 대입함으로써 맨 끝 노드를 삭제시킴
                self.current = pre # 주목 포인터가 맨 뒤에서 바로 앞 노드를 가리키도록 업데이트
                self.no -= 1 # 노드의 개수 1 감소

    def remove(self, p): # 노드 p를 삭제
        if self.head is not None:
            if p is self.head: # p가 머리 노드이면
                self.remove_first() # 머리 노드를 삭제
            else: # p가 머리 노드가 아니면
                ptr = self.head # head부터 스캔을 시작
                while ptr.next is not p: # ptr.next가 p와 같아질 때까지 반복 -> 이 반복이 종료되는 조건은 ptr.next가 p가 될 때이다.
                    ptr = ptr.next # ptr.next가 p와 같지 않을 때는 계속 다음 노드로 이동함
                    if ptr is None: # ptr이 리스트에 존재하지 않을 때
                        return # 함수를 종료한다.
                ptr.next = p.next # ptr.next가 p와 같아졌다면 ptr.next(삭제되는 노드의 바로 앞 노드의 next)에 p.next(삭제되는 노드의 next 값)를 담아준다.
                self.current = ptr # 주목하는 노드를 p(뒷쪽 노드)에서 ptr(앞쪽 노드)로 업데이트시킴
                self.no -= 1 # 노드의 개수 1 감소

    def remove_current_node(self): # 주목 노드를 삭제
        self.remove(self.current)

    def clear(self): # 전체 노드를 삭제
        while self.head is not None: # 전체가 비어 있을 때(head가 None이 될 때)까지
            self.remove_first() # 머리 노드를 계속해서 삭제
        self.current = None # 전체 노드가 삭제되어 주목 노드가 None으로 업데이트
        self.no = 0 # 전체 노드가 삭제되어 노드의 개수가 0으로 업데이트

    def next(self): # 주목 노드를 한 칸 뒤로 이동
        if self.current is None or self.current.next is None: # 리스트가 비어있거나 주목 노드의 뒤쪽 노드가 존재하지 않으면
            return False # False 반환
        self.current = self.current.next # False를 반환하여 종료되는 경우가 아니라면 다음 주목 노드에 현재 주목 노드를 담아줌
        return True # True 반환

    def print_current_node(self): # 주목 노드를 출력
        if self.current is None:
            print("주목 노드가 존재하지 않습니다.")
        else:
            print(self.current.data)

    def print(self): # 모든 노드를 출력
        ptr = self.head # head의 위치를 ptr에 담아 처음부터 시작

        while ptr is not None: # ptr이 마지막 위치에 다다를 때 까지
            print(ptr.data) # 현재 ptr 위치의 데이터를 출력
            ptr = ptr.next # 다음 위치로 이동

    def __iter__(self): # 이터레이터를 반환
        return LinkedListIterator(self.head)

class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data
