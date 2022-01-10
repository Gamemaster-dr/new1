# リスト
num_list = [1,2,3,4,5,6,7,8,9,10]

print(num_list)

# forとif
# for num in num_list:
#     print(i)

# for num in range(1,100):
#     if num % 2 == 0:
#         print(f"{num}は偶数です")
#     else:
#         print(f"{num}は奇数です")
        

#いろいろなパターン　passは何もしないということ。とりあえず条件を書いておかないといけないけど空欄だとエラーになるのでその場合に使う
# andはかつ、orはもしくは

# if num > 1 and num < 10:
#     pass
# elif num < 10 or num > 100:   
#     pass
# elif num != 0:
#     pass
# else:
#     pass

#課題
# 1から100までの数字のうち、3で割り切れる数字、5で割り切れる数字
# 3と5の両方で割り切れる数字をprint文で表示させてください。
# elifにしない理由として、1行目の条件で当てはまってしまうと他の行の条件を見に行かなくなってしまう為

for i in range(1,101):
    if i % 3 == 0:
        print(f"{i}は3で割り切れる")
    if i % 5 == 0:
        print(f"{i}は5で割り切れる")   
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}は3と5の両方で割り切れる")
        