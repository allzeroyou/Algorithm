N = int(input())

array = [0]*10000000

for _ in range(N):
    i = int(input())




    # append 한번 하는데 O(N)임-> 연산을 N번하니까 -> O(N^2)
    # del 한번 하는데 O(N)임 -> 연산을 N번하니까 -> O(N^2)
    # 조회는 O(1) -> N번하니까 O(N)

# 배열 vs 연결리스트
# 배열은 파이썬에서 list 자료구조로 사용가능하되, array라고 부르는게 나음
# 연결리스트라는 자료구조가 있기 때문!
# 배열과 정반대임