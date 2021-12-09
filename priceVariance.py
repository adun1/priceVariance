#!/usr/bin/python3

def calcPriceVar(item):
	return item['actualQ'] * (item['actualrate'] - item['standardrate'])
    
def calcQuantityVar(item):
	return item['standardrate'] * (item['actualQ'] - item['standardQ'])
    
numKayaks = 35
items = {
'powder': {'actualrate': 3980 / 1990, 'standardrate': 1.50, 'actualQ': 1990.0 / numKayaks, 'standardQ': 54}, 
'type1worker': {'actualrate': 2020/101, 'standardrate': 20, 'actualQ': 101/numKayaks, 'standardQ': 3}
}
for item in items:
	print("#", item, "#", sep="")
	print('price', calcPriceVar(items[item]))
	print('quantity', calcQuantityVar(items[item]))

