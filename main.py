#関数

a = 15
b = 4
 
#  print(a)
#  print(b)
 
c = a + b
d = a - b
e = a * b
f = a / b

print(c,d,e,f)


g = a % b
print(g)
print(f"{a}を{b}で割った余りは{g}です")

int_var = 15
string_var = "15"
float_var = 15.0
# print(int_var + string_var) エラーが出ます

#課題
# 数字の100と150を変数として定義して
# これらを四則演算した結果をprintで表示させてください。
# printする際は、わかりやすいように上で説明したf文字列を使って説明文を記述してください。

#上記で既にabcdを使用している為numとしてわかりやすくする事が必要である
num1 = 100
num2 = 150

num3 = num1 + num2
num4 = num1 - num2
num5 = num1 * num2
num6 = num1 / num2
print(f"{num1}と{num2}を足した値は{num3}です")
print(f"{num1}から{num2}を引いた値は{num4}です")
print(f"{num1}と{num2}を掛けた値は{num5}です")
print(f"{num1}から{num2}を割った値は{num6}です")


#下記のようにする


print(f"{num1}と{num2}を足した値は{num1 + num2}です")
print(f"{num1}から{num2}を引いた値は{num1 - num2}です")
print(f"{num1}と{num2}を掛けた値は{num1 * num2}です")
print(f"{num1}から{num2}を割った値は{num1 / num2}です")