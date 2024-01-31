while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except EOFError:
        break
# 사용자로부터 입력을 끝까지 받아서 EOFError 라고 불리우는 오류를 발생시키는데 이때 EOF란 파일의 끝(end of file) 을 의미하며(파일의 끝은 ctrl-d 에 의해 표현됩니다),
# 갑자기 파일의 끝이 올 것을 예상하지 못했기 때문에 위와 같은 오류가 발생
# 예외는 try..except 문을 통해 처리할 수 있습니다. 이것은 try 블록 안에 평소와 같이 명령을 입력하고 예외 상황에 해당하는 오류 핸들러를 except 블록에 입력해 주면 된다.

