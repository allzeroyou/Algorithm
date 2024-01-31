# 노드 구현(값 + 링크)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

# head = Node(5)
# next_node = Node(12)
# head.next = next_node

# 단순 연결 리스트
'''
구현될 항목
- 첫 번째 노드 삽입
- 중간 노드 삽입
- 마지막 노드 삽입
- 노드 삭제
'''
class SingleLinkedList:
    def __init__(self, data):
        new_node=Node(data)
        self.head = new_node            # head 필요
        self.list_size = 1              # 길이 계산 보단 길이를 가지고 있는게 더 나아서 O(1) 추가

    def __str__(self):
        print_list = '[ '
        node = self.head
        while True:
            print_list += str(node)
            if node.next == None:
                break
            node = node.next
            print_list += ', '
        print_list += ' ]'
        return print_list

    # 첫번째 노드 삽입
    def insertFirst(self, data):
        new_node = Node(data)           # 새로운 노드 생성
        temp_node = self.head           # 기존 헤드를 잠시 보관
        self.head = new_node            # 헤드를 새로운 노드로 변경
        self.head.next = temp_node      # 새로 생성된 헤드의 링크를
                                        # 기존 헤드의 링크로 변경
        self.list_size += 1
    # 노드 선택
    def selectNode(self, num):
        if self.list_size < num:
            return                      # overflow
        node = self.head
        count = 0
        while count < num:
            node = node.next            # 간단하게 노드를 전환, 연결된 링크로 이동
            count += 1
        return node
    # 마지막 노드 삽입
    def insertLast(self, data):
        node = self.head
        while True:
            if node.next == None: # 다음 링크가 없으면
                break
            node = node.next

        new_node = Node(data)
        node.next = new_node
        self.list_size += 1

    # 중간 노드 삽입
    def insertMiddle(self, num, data):
        if self.head.next == None:
            # 헤더가 만들어진 직후에 메서드 사용하는 경우
            self.insertLast(data)
            return
        node = self.selectNode(num)
        new_node = Node(data)
        temp_next = node.next
        node.next = new_node
        new_node.next = temp_next
        self.list_size += 1

    # 노드 삭제
    def deleteNode(self, num):
        if self.list_size < 1:
            return              # underflow
        elif self.list_size < num:
            return              # overflow
        if num == 0:
            self.deleteHead()
            return
        node = self.selectNode(num -1) # 이전 노드의 링크를 다다음 노드와 연결

        node.next = node.next.next
        del_node = node.next
    # 헤드 노드 삭제
    def deleteHead(self):
        node = self.head
        self.head = node.next
        del node
    # 연결리스트 크기
    def size(self):
        return str(self.list_size)

if __name__ == '__main__':
    m_list = SingleLinkedList(1)
    m_list.insertLast(5)
    m_list.insertLast(6)
    print('LinkedList: ', m_list)
    print('LinkedList: ', m_list.size())
    print('LinkedList SelectNode(1) :',
          m_list.selectNode(1))
    m_list.insertMiddle(1, 15)
    print('LinkedList Insert Middle(1, 15) :', m_list)

    m_list.insertFirst(100)
    print('LinkedList Insert First(100) : ', m_list)
    print('LinkedList SelectNode(0) :', m_list.selectNode(0))

    m_list.deleteNode(0)
    print('LinkedList Delete Node(0) : ', m_list)
    m_list.deleteNode(1)
    print('LinkedList Delete Node(1) : ', m_list)