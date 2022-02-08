import time

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

# 単純にリストの内容を1つずつ出力する
for i in data:
    print(i)

# リストの内容を1つ出力するたびに1秒スリープする
for i in data:
    print(i)
    time.sleep(1)
