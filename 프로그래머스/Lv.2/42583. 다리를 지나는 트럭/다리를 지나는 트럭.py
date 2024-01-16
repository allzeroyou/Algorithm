def solution(bridge_length, weight, truck_weights):
    # 다리 건너는 트럭
    ing_truck = []
    # 트럭 수
    answer = 0
    # 다리 지나는 중인 트럭 무게
    total = 0

    while truck_weights:  # 트럭 모두가 지날때까지
        answer += 1  # 과정 하나가 지날때 +1

        # 무게 보다 가볍고, 다리 위 트럭 개수가 최대 트럭수보다 작을때
        if (total + truck_weights[0] <= weight) and len(ing_truck) <= bridge_length:
            ing_truck.append(truck_weights.pop(0))
            total += ing_truck[-1]

        else:
            ing_truck.append(0)

        if answer >= bridge_length:  # 다리에 올라갈 수 있는 트럭수보다 크다면
            total -= ing_truck.pop(0)

    return answer + bridge_length
