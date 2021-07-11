pip3 install -r requirements.txt

herokuで実行
heroku run --app floating-stream-17786 python test.py 0
heroku run --app floating-stream-17786 python test.py 19

環境変数の一覧
heroku config --app floating-stream-17786

環境変数を追加／変更する
heroku config:set 環境変数名=セットしたい値 --app floating-stream-17786

環境変数を削除する
heroku config:unset 環境変数名 --app floating-stream-17786

stock token
heroku config:set git_token=xxxxxxxxxxxxxxxx --app floating-stream-17786


