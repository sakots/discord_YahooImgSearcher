# discord_YahooImgSearcher

![いめーじ](top.png)

## これは何ですか

入力された文字列に反応してyahooで画像検索して1件返すだけのDiscordBot。

## 使い方

1. Python3の新しいやつを動かせるようにしてください。
2. 必要そうなライブラリをインストールします。

   ```python
   
   pip install python-dotenv discord.py bs4 

   ```

   あとなんか足りなかったら動かしたときに「足りねえぞ！」ってエラーが出るので適宜インストールで。

3. Discordにbotの登録をします。[Discord Developer Portal](https://discord.com/developers/applications)からどうぞ。
4. 設定を終えたら、`sample.env`を`.env`にリネームして、ACCESS_TOKENのところにBotのアクセストークンをいれてください。
5. Python3でyahoo_search.pyを動かして、botがオンラインになったらOK。
6. 「!i ○○」で、○○を画像検索して貼り付けてくれます。

## 履歴のようなもの

### [2021/07/11]

- 公開
