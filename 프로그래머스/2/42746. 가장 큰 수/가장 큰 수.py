def solution(numbers):
    answer = ''

    def three_number(num):
        str_num = str(num)
        three = (str_num * 4)[:4]
        return three

    numbers.sort(key=lambda x: three_number(x), reverse=True)

    answer = ''.join(map(str, numbers))
    return str(int(answer))