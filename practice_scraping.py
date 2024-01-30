"""
クローリング➡複数ウェブサイトのリンクをなぞってウェブページを巡回すること。
クローラー➡クローリングをするプログラムのこと。
Webスクレイピング➡ウェブサイトのHTMLから必要なデータを取得すること。
   ※クローラ(プログラム)によって必要な情報のあるWebページにアクセスし、
     スクレイパによって実際に情報を取得する。
<注意点>
無許可のクローリング・スクレイピングを拒否している場合がある。
処罰の可能性も。
"""
#----RequestとBeautiful Soupを使った基本のスクレイピング--------------------------

#---<Request>---------------------------------------------------------------------
#まずは「pip3 install requests」をコマンドプロンプトから実行、Requestをインストール。
"""
import requests

r = requests.get('https://news.yahoo.co.jp')

print(r.headers)#header情報を取得
print("---------------------------------------")
print(r.encoding)#Webページ指定のエンコード情報を取得
print(r.content)#body以下の情報を取得

"""
#-----------------------------------------------------------------------------------

#---<Beautiful Soup>----------------------------------------------------------------
#「pip3 install beautifulsoup4」をコマンドプロンプトから実行、Beautiful Soupをインストール。

"""
from bs4 import BeautifulSoup

html = "<h1>sayhello</h1>,<h1>saysay</h1>,<h2>say</h2>"

soup = BeautifulSoup(html,"html.parser")#parser:何を元に解析するか⇒HTML

print(soup.select("h1"))#取得し、soupに格納したHTMLの内<h1>タグを指定して表示。

"""

#---結果------
# [<h1>sayhello</h1>, <h1>saysay</h1>] がコマンドラインに表示される。

#<注意点>
#Beautiful SoupはURLを指定することができない。

#-----------------------------------------------------------------------------------

#-----実践編--(失敗)----------------------------------------------------------------------------
"""
import requests
from bs4 import BeautifulSoup

url = "https://news.yahoo.co.jp/"

res = requests.get(url)#Requestsのget()メソッドによって

soup = BeautifulSoup(res.content,"html.parser")

#elems = soup.select('#uamods-topics > div > div > div > ul > li')

#elems = soup.find_all("a")
#print(elems)

#正規表現を扱う機能がある、Python標準ライブラリのreモジュールをインポート。
import re

elems = soup.find_all(href=re.compile("https://news.yahoo.co.jp/pickup/"))
#print(elems[0].contents[0])#１つ目のタイトルのみ表示
#print(elems[0].attrs['href'])#１つ目のURLのみ表示



#ループ処理で全てのタイトル＆URLの一覧を取得
for elem in elems:
    if elem.text.strip():
        print(elem.text)
        print(elem.attrs['href'])
"""
        
"""---結果-----
豊田織機 ディーゼル試験でも不正   
https://news.yahoo.co.jp/pickup/6489870
豊田織機 ディーゼル試験でも不正
https://news.yahoo.co.jp/pickup/6489870
極寒のビニールハウス避難 事情は
https://news.yahoo.co.jp/pickup/6489862
中国恒大 香港市場で株式取引停止
https://news.yahoo.co.jp/pickup/6489865
京アニ被告 遺族と初めて直接面会
https://news.yahoo.co.jp/pickup/6489864
邦人拘束を正当化 訪中団は落胆
https://news.yahoo.co.jp/pickup/6489858
朝鮮人の追悼碑 群馬県が撤去開始
https://news.yahoo.co.jp/pickup/6489861
「オーサムストア」全店閉店へ
https://news.yahoo.co.jp/pickup/6489866
やす子 忙しすぎ「はい～」忘れる
https://news.yahoo.co.jp/pickup/6489867
<span class="sc-fLkZIC mmyYW" style="background-image:url(https://news-pctr.c.yimg.jp/t/news-topics/images/tpc/2024/1/29/30ab6ea16b07467b078bacc584ef4893be0fcefa604364596cb94f97e05c58d8.jpg?w=440&amp;h=440&amp;pri=l&amp;up=0)"></span>
https://news.yahoo.co.jp/pickup/6489866
"""
#-----実践編--(失敗)----------------------------------------------------------------------------


#-----実践編--(成功)----------------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup

url = "https://news.yahoo.co.jp/"

res = requests.get(url)#Requestsのget()メソッドによって

soup = BeautifulSoup(res.content,"html.parser")

elems = soup.select('#uamods-topics > div > div > div > ul > li')
#指定したい要素コード(Elements)liの上で右クリック、Copyでセクレタをコピー。

for elem in elems:
    title = elem.text#タグではなく、中身のテキスト部分。
    url = elem.find('a')['href']
    print(title)
    print(url)


"""---結果---
豊田織機に立ち入り検査 国交省
https://news.yahoo.co.jp/pickup/6489949
織機不正巡りトヨタ4工場生産停止
https://news.yahoo.co.jp/pickup/6489944
がれき撤去の同意難しく 復旧妨げ
https://news.yahoo.co.jp/pickup/6489939
琵琶湖でボート転覆 複数心肺停止
https://news.yahoo.co.jp/pickup/6489946
京アニ被告 遺族面会でアニメの話
https://news.yahoo.co.jp/pickup/6489948
塾経営者に性犯罪歴 娘守れず悲痛
https://news.yahoo.co.jp/pickup/6489937
実験用サルの価格 コロナ前の5倍
https://news.yahoo.co.jp/pickup/6489940
水原氏なしで英会話 急成長の大谷
https://news.yahoo.co.jp/pickup/6489941
"""

#-----実践編--(成功)----------------------------------------------------------------------------