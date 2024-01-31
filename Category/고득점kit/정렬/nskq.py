def solution(numbers):
    MAX = 1001
    nums = list(map(str,range(0,MAX))) # 숫자로 하면 너무 크기 때문에 문자열로!

    for i in range(MAX):
        for j in range(MAX):
            vi,vj = nums[i],nums[j]
            if vj+vi < vi+vj:  # 문자열 더하기(e.g. 01 < 10)
                nums[i],nums[j] = vj,vi

    dic = {}

    for number in numbers:
        number = str(number)
        if number not in dic:
            dic[number] = 0
        dic[number] += 1

    ret = ""
    for num in nums:
        if num in dic:
            ret += num * dic[num]
    if all(k=='0' for k in dic.keys()):
        return '0'
    return ret
print(solution([10,100,111]))