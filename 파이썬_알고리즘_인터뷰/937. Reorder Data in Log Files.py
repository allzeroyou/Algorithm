from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        num_list = []  # 숫자로그
        word_list = []  # 문자로그
        for i in logs:
            word = i.split()
            if word[1].isdigit():  # 숫자-True
                num_list.append(i)

            else:
                word_list.append(i)

        word_list.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return word_list + num_list


s = Solution()
print(s.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
