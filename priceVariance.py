#!/usr/bin/python3
def calcPriceVar(item):
	return item['actualQ'] * (item['actualrate'] - item['standardrate'])
    
def calcQuantityVar(item):
	return item['standardrate'] * (item['actualQ'] - item['standardQ'])

#5    
numKayaks = 35
items = {
'powder': {'actualrate': 3980 / 1990, 'standardrate': 1.50, 'actualQ': 1990.0 / numKayaks, 'standardQ': 54},
'finishingKit': {'actualrate': 5810/numKayaks, 'standardrate': 174, 'actualQ': 1, 'standardQ': 1}, 
'type1worker': {'actualrate': 2020/101, 'standardrate': 20, 'actualQ': 101/numKayaks, 'standardQ': 3},
'type2worker': {'actualrate': 2518.50/146, 'standardrate': 17, 'actualQ': 146/numKayaks, 'standardQ': 4}
}

#6 - double check encoding
items2 = {
'materials': {'actualrate': 122.00, 'standardrate': 124.00, 'actualQ': 1176, 'standardQ': 1140},
'labour': {'actualrate': 16.00, 'standardrate': 13.00, 'actualQ': 4120, 'standardQ': 4340}
}

for item in items:
	print("#", item, "#", sep="")
	print('price', calcPriceVar(items[item]))
	print('quantity', calcQuantityVar(items[item]))
	print()

for item in items2:
	print("###q6###")
	print("#", item, "#", sep="")
	print('price', calcPriceVar(items2[item]))
	print('quantity', calcQuantityVar(items2[item]))
	print()
