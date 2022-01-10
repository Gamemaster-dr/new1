print("関数の外")

#引数

def test(num):
    for i in range(num):
        print(f"関数の中:{i}")
                
test(3)

#戻り値

def sum(a,b):
    return a + b

c = sum(1,5)
print(c)

#課題
# 1からnまでの数字を足した結果をreturnする関数を作成してください
# 1 + 2 + 3 + .... + n

def sigma(num):
    total = 0
    for i in range(1,num + 1):
        total += i
        
    return(total)

print(sigma(100))
# 動詞 + 名詞
# print_number

#検算
#(1 + num)*num/2