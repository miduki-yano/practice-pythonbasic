#pythonファイルの拡張子は.py
#----python3で変数名に使えない予約語----------------------------
['False', 'None', 'True', 'and', 'as', 'assert', 'break',
  'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
  'finally', 'for', 'from', 'global', 'if', 'import', 'in', 
  'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
  'return', 'try', 'while', 'with', 'yield']
#--------------------------------------------------------------

#--------------------------------------------------------------

#文字列なら"または'で囲む。数値はなし。
lang = "小文字" #変数に文字列を代入(pythonには型宣言がない)
#変数に格納した値は、プログラムが終了するまで保持する
Lang = "大文字" #pythonは小文字と大文字を区別できる

print(lang)
print(Lang)

print(10+5)
print('10+5')

#--------------------------------------------------------------

#--------------------------------------------------------------

hello_world = "Hello,World"
#変数名に2語使う場合は＿で区切るのが推奨される。

x = 5
print(x)#5が出力される

x = "Python"#型宣言がないため、代入可能。
print(x)#Pythonが出力される

#--------------------------------------------------------------

#-----結合---------------------------------------------------------

a = "hello "
b = "world"
print(a + b)#「hello world」と出力される。

#--------------------------------------------------------------

#------反復--------------------------------------------------------

a = "Diego"
print(a * 3)#「DiegoDiegoDiego」と出力される。

#--------------------------------------------------------------

#------型変換(キャスト)--------------------------------------------------------
#文字列型と数値型を連結した場合、エラーとなる。

name = "Diego"
age = 26

#print("I'm " + name + " and " + age + " years old.")
#「TypeError: can only concatenate str (not "int") to str」のエラーになる。

print("I'm " + name + " and " + str(age) + " years old.")
#数値型⇒文字列型にキャスト

banana = "200"
orange = 390

print(int(banana) + orange)
#文字列型⇒数値型にキャスト

#--------------------------------------------------------------

#-----リスト型---------------------------------------------------------
#構文：配列名 = ["x","y","z"]

li = []

li.append("python")#リストの末尾に要素を追加
print(li)#['python']と表示される。


li.append("php")
print(li)
#['python', 'php']と表示される。
#インデックス番号は[0],[1]

print(li[1])#インデックス番号を指定して表示。

#--------------------------------------------------------------

#-----辞書型---------------------------------------------------------
#keyとValueのセットを保持する。
#構文：辞書名 = {"キー1" : "値1","キー2" : "値2",.....}

profile = {"name":"tani","email":"mokomoko@gmoil.com"}#{}で囲う。
print(profile["name"])#キー文字列を指定して表示。

profile["gender"] = "man"
#新しく要素を追加
#辞書名["キー"] = "値"

print(profile)
#{'name': 'tani', 'email': 'mokomoko@gmoil.com', 'gender': 'man'}が表示される。

#--------------------------------------------------------------

#----インデントと条件式----------------------------------------------------------
#インデント(字下げ)はプログラムの動作に影響する。
#「if 条件式:」のように書く。
#条件式の後に:とインデントが必要。無いとエラーになる。

score = 80
if score > 78:#コロン
    print("合格")
    #前の文に:があれば、先頭に半角スペース４つ(それかタブ1)が必要。
else:#コロン
    print("不合格")
    #前の文に:があれば、先頭に半角スペース４つ(それかタブ1)が必要。

#合格が表示される。

#--------------------------------------------------------------

#----for文のループ処理----------------------------------------------------------
#構文：for ループ内変数 in リスト名:(インデント)実行する処理
       
for i in ["apple","banana","melon"]:
    print(i)
#リストの要素を全て取り出し、処理終了。
    

#range(x): 0からx-1までの連番のリストを返す
#range(x,y): xからy-1までの連番のリストを返す    
    
for i in range(10):#range()メソッド
    print(i)
#0~9までの数字を表示。
    

data = [2,4,3,6]
sum = 0  #初期化

for d in data:
    sum += d
    #sum = sum + d
else:
    print(sum)
    # 2+4+3+6=15 なので、15が表示される。

#--------------------------------------------------------------

#----辞書型のループ処理----------------------------------------------------------

data = {"tani":21,"kazu":22,"python":100}

for key, value in data.items():#items()メソッドは辞書のキーと値のセットを返す。
    print("key: {} value:{}".format(key, value))
    #{}は置き換えフィールド
    #format()メソッドで引数として渡されたkeyとvalueで、左から順に穴埋めする。
    
    #--結果---
    #key: tani value:21
    #key: kazu value:22
    #key: python value:100
  
#--------------------------------------------------------------
    
#-----while文---------------------------------------------------------

n = 0
while n < 10:#nが10未満の間はｎを表示して、＋１する。
    print(n)
    n += 1

    #0~9が表示される。

#n += 1を書かないと、無限ループとなる。※Ctrl + cで終了できる。
    
#もし、故意に無限ループする場合
#while True:
    #print("無限ループ")    

#--------------------------------------------------------------
    
#--------------------------------------------------------------