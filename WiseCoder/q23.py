def print_arithmetic_operation(n1, n2):
    add = n1 + n2
    minus = n1 - n2
    mul = n1 * n2
    de = n1 / n2
    print(f"{add} {minus} {mul} {de} 가 반환되었습니다.")


n1 = int(input("첫 번째 정수를 입력하시오: "))
n2 = int(input("두 번째 정수를 입력하시오: "))
print_arithmetic_operation(n1, n2)