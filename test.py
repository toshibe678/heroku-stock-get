import pandas as pd
import pandas_datareader.data as web

# JPXの東証上場一覧のページへのアクセス
!wget 'https://www.jpx.co.jp/markets/statistics-equities/misc/tvdivq0000001vg2-att/data_j.xls' -O data_j.xls -a wget-log

## pandasでexcelファイルの読み込みとdf整形など
company_df = pd.read_excel("data_j.xls")
company_df.columns = ['date', 'code', 'name', 'lst', 'sectorCode', 'sectorName', 'flr1', 'flr2', 'flr3', 'flr4']
drop_col = ['flr1', 'flr2', 'flr3', 'flr4']
company_df = company_df.drop(drop_col, axis=1)  # 不要な列の削除

