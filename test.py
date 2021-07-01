import pandas as pd
import pandas_datareader.data as web
import time
import os

import requests
import pprint

# JPXの東証上場一覧のページへのアクセス

response = requests.get("https://www.jpx.co.jp/markets/statistics-equities/misc/tvdivq0000001vg2-att/data_j.xls")
fileName = 'data_j.xls'
saveFilePath = os.path.join('.', fileName)
with open(saveFilePath, 'wb') as saveFile:
    saveFile.write(response.content)

## pandasでexcelファイルの読み込みとdf整形など
company_df = pd.read_excel("data_j.xls")
company_df.columns = ['date', 'code', 'name', 'lst', 'sectorCode', 'sectorName', 'flr1', 'flr2', 'flr3', 'flr4']
drop_col = ['flr1', 'flr2', 'flr3', 'flr4']
company_df = company_df.drop(drop_col, axis=1)  # 不要な列の削除

# 保存用ディレクトリの準備
os.mkdir('/tmp/stock')

j = 0
count = 0
tmp_code = 0
for index, item in company_df.iterrows():
    if j <= index / (len(company_df) / 20) < j + 1:
        if count == 0:
            print('from:'+str(item['code'])+' start!')
            count = 1
        ### 中身を文字型に変換して'.JP'を付与
        code = str(item['code']) + '.JP'
        stock_df = web.DataReader(code, "stooq")
        # 早すぎると規制されるっぽいのでsleep
        time.sleep(1)

        # 1日の制限超えた応答きたらエラー
        if stock_df.empty:
            print(stock_df)
            print('error:' + str(item['code']) + ' daily over!?')
        else:
            stock_df['Code'] = item['code']

            # 後処理のために明示的にカラムを並び替える
            stock_df.reindex(columns=['Code', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume'])

            # csv保存：[stock_code].csv
            filename = "/tmp/stock/" + str(item['code']) + ".csv"
            stock_df.to_csv(filename, encoding="utf-8")
            tmp_code = item['code']

print('to:'+str(tmp_code)+' end!')
print('All_finish!')
