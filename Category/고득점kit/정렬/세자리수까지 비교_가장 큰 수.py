def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)  # 세 자리까지 비교

    answer = str(int(''.join(numbers)))  # 앞에 0을 제거하기 위해 int로 변환 후 다시 str로 변환

    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0, 0, 0]))
print(solution([10, 100, 111]))
print(solution([99,0,90]))

if "666">"101010": # 첫번째 문자를 가지고 비교
    print("666이 더 큼")
if "50" > "5": # 첫번째 문자가 같으면 2번째 자릿수로 비교
    print("50이 더 큼")
if "333">"303030": # 2번째 자리로 크기 비교
    print("333이 더 큼")