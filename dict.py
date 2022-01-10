test_dict = {
    "名前": "りんご",
    "価格": 100,
    "個数": 3
}

print(test_dict["名前"])
print(test_dict["価格"])
print(test_dict["個数"])

item = {
    "名前": "りんご",
    "価格": 100,
    "個数": 3
}


item2 = {
    "名前": "みかん",
    "価格": 150,
    "個数": 2
}


item3 = {
    "名前": "きゅうい",
    "価格": 200,
    "個数": 1
}
item_list = [item,item2,item3]

print(item_list)

#課題
#あらかじめ辞書で商品を定義しておき、その中から
# 指定した商品の価格を取得する関数を作成してください

def find_item_price(name):
    item_list = []
    item_list.append({
        "名前": "りんご",
        "価格": 100,
        "個数": 3
    })
    item_list.append({
         "名前": "みかん",
        "価格": 150,
        "個数": 2
    })
    item_list.append({
        "名前": "きゅうい",
        "価格": 200,
        "個数": 1
    })
    
    for item in item_list:
        if item["名前"] == name:
            return item["価格"]
    return None

print(find_item_price("みかん"))
print(find_item_price("きゅうい"))
print(find_item_price("きゅうい2"))