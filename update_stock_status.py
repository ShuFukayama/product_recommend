import csv
import random
import constants as ct

# 在庫状況の選択肢
stock_options = [ct.STOCK_STATUS_AVAILABLE, ct.STOCK_STATUS_LOW, ct.STOCK_STATUS_NONE]

# CSVファイルを読み込む
input_file = "data/products.csv"
output_file = "data/products_updated.csv"

with open(input_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = list(reader)

# ヘッダー行に「stock_status」を追加
header = rows[0]
header.append("stock_status")

# 各商品行に在庫状況をランダムに割り振る
for i in range(1, len(rows)):
    # ランダムに在庫状況を選択
    stock_status = random.choice(stock_options)
    rows[i].append(stock_status)

# 更新したデータをファイルに書き込む
with open(output_file, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print(f"在庫状況を追加したCSVファイルを {output_file} に保存しました。")