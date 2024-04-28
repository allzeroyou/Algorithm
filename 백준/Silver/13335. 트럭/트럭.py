# n: 다리 건너는 트럭수, w: 다리 길이, l: 다리의 최대하중
n, w, l = map(int, input().split())
# 트럭의 무게
trucks = list(map(int, input().split()))

bridge = [0] * w  # 다리
weight, time = 0, 0  # 현재 다리 위 무게, 시간

while True:
    out = bridge.pop(0)  # 방금 다리를 건넌 트럭은 다리에서 제거해야한다.
    weight -= out  # 방금 다리 다리를 건넌 트럭의 무게를 weight에서 빼야 다음 트럭이 건너옴

    if trucks:  # 넘어 올 트럭이 남아있을 때
        if weight + trucks[0] <= l:  # 다리 하중을 견딜 수 있으면
            bridge.append(trucks[0])  # 다리를 건너려는 트럭
            weight += trucks[0]  # weight에 현재 다리를 건너려는 트럭 무게 추가
            trucks.pop(0)

        else:  # 다리 하중을 견딜 수 없으면
            bridge.append(0)  # 0을 추가하여 다리위에 있는 트럭을 먼저 보낸다.
    time += 1  # 시간 +1

    if not bridge:  # 다리위에 트럭이 다 지나가면 반복문 종료
        break
print(time)
