namae = input ('あなたの名前を入力して:')
shintyo = input ('あなたの身長は何センチですか?:')
shintyo = float ( shintyo ) 
weight = input ('あなたの体重は何キログラムですか?:')
weight = float ( weight ) 
bmi = 10000* weight /( shintyo **2)
print ( namae , 'さんのBMIは', bmi, 'です。')
