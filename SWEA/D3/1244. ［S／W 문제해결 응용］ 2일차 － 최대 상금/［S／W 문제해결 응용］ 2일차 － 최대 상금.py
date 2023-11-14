t = int(input())


def dfs(cnt):
    global ans
    # 바꿀 수 있는 기회가 없다면
    if cnt == 0:
        ans = max(int(''.join(nums)), ans)
        return
    # 교환
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            # 백트래킹을 위해 합친다.
            tmp_key = ''.join(nums)
            if visited.get((tmp_key, cnt - 1), 1):
                # 딕셔너리안에 없다면 아직 사용 안한 것 -> 0으로 체크
                visited[(tmp_key, cnt - 1)] = 0
                # dfs 실행
                dfs(cnt - 1)
            # 다시 바꾼 값을 원상복귀
            nums[i], nums[j] = nums[j], nums[i]


for tc in range(1, t + 1):
    # 숫자판 정보, 교환횟수
    temp, cnt = input().split()
    # 리스트 화, 정수형 화
    nums = list(temp)
    cnt = int(cnt)
    # 정답
    ans = -1
    # 백트래킹용
    visited = {}
    dfs(cnt)

    print(f'#{tc} {ans}')
