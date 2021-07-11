pip3 install -r requirements.txt

herokuで実行
heroku run --app floating-stream-17786 python stock.py 1
heroku run --app floating-stream-17786 python stock.py 19

環境変数の一覧
heroku config --app floating-stream-17786

環境変数を追加／変更する
heroku config:set 環境変数名=セットしたい値 --app floating-stream-17786

環境変数を削除する
heroku config:unset 環境変数名 --app floating-stream-17786

stock token
heroku config:set git_token=xxxxxxxxxxxxxxxx --app floating-stream-17786

crontab -e
2 16 * * 1-5 /usr/local/bin/heroku run --app floating-stream-17786 python stock.py 0
2 17 * * 1-5 /usr/local/bin/heroku run --app floating-stream-17786 python stock.py 1
2 18 * * 1-5 /usr/local/bin/heroku run --app floating-stream-17786 python stock.py 2
2 19 * * 1-5 /usr/local/bin/heroku run --app floating-stream-17786 python stock.py 3
2 20 * * 1-5 /usr/local/bin/heroku run --app floating-stream-17786 python stock.py 4
2 21 * * 1-5 /usr/local/bin/heroku run --app floating-stream-17786 python stock.py 5
2 22 * * 1-5 /usr/local/bin/heroku run --app floating-stream-17786 python stock.py 6
2 23 * * 1-5 /usr/local/bin/heroku run --app floating-stream-17786 python stock.py 7
2 0 * * 1-5 /usr/local/bin/heroku run --app floating-stream-17786 python stock.py 8
2 1 * * 1-5 /usr/local/bin/heroku run --app floating-stream-17786 python stock.py 9
2 2 * * 1-5 /usr/local/bin/heroku run --app floating-stream-17786 python stock.py 10
2 3 * * 1-5 /usr/local/bin/heroku run --app floating-stream-17786 python stock.py 11
2 4 * * 1-5 /usr/local/bin/heroku run --app floating-stream-17786 python stock.py 12
2 5 * * 1-5 /usr/local/bin/heroku run --app floating-stream-17786 python stock.py 13
2 6 * * 1-5 /usr/local/bin/heroku run --app floating-stream-17786 python stock.py 14
2 7 * * 1-5 /usr/local/bin/heroku run --app floating-stream-17786 python stock.py 15
