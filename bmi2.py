namae = input('あなたの名前を入力してください:')
shintyo = input('あなたの身長は何センチですか?:')
shintyo = float(shintyo)
weight = input('あなたの体重は何キログラムですか?:')
weight = float(weight)

bmi = 10000.0*weight/(shintyo**2)
bmi = round(bmi,1)

print(namae, 'さんのBNIは', bmi, 'で', end='')

if bmi < 18.5:
   print('やせ気味です。')
elif bmi < 25.0:
   print('ふつうです。')
elif bmi < 30:
   print('太り気味です。')
else:
   print('太りすぎです。')
