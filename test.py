import pandas as pd
import pandas_datareader.data as web

import requests
import json
endPoint = 'https://api.coin.z.com/public'
path = '/v1/ticker?symbol=BTC'
response = requests.get(endPoint + path)
print('現在のビットコインの価格は', response.json()['data'][0]['last'],'円です')

# JPXの東証上場一覧のページへのアクセス
# !wget 'https://www.jpx.co.jp/markets/statistics-equities/misc/tvdivq0000001vg2-att/data_j.xls' -O data_j.xls -a wget-log

## pandasでexcelファイルの読み込みとdf整形など
# company_df = pd.read_excel("data_j.xls")
# company_df.columns = ['date', 'code', 'name', 'lst', 'sectorCode', 'sectorName', 'flr1', 'flr2', 'flr3', 'flr4']
# drop_col = ['flr1', 'flr2', 'flr3', 'flr4']
# company_df = company_df.drop(drop_col, axis=1)  # 不要な列の削除
#
# j = 0
