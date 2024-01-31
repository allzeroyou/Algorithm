import bookstore
b = bookstore.Book()
print(b)  # 책 객체를 새로 만들었어요~
# Book()을 통해 Book 객체를 만들자마자 초기화 메서드 실행.
# setData와 printData 메서드들은 다음과 같이 사용 가능

b.setData('누가 내 치즈를 먹었을까', '300원', '미키')
print(b.printData())