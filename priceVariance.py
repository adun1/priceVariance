#!/usr/bin/python3
def calcPriceVar(item):
	return item['actualQ'] * (item['actualrate'] - item['standardrate'])
    
def calcQuantityVar(item):
	return item['standardrate'] * (item['actualQ'] - item['standardQ'])

def calcTotalVar(item):
	return item['actualQ']*item['actualrate'] - item['standardQ']*item['standardrate']
#5    
numKayaks = 35
items = {
'powder': {'actualrate': 3980 / 1990, 'standardrate': 1.50, 'actualQ': 1990.0, 'standardQ': 54*numKayaks},
'finishingKit': {'actualrate': 5810/numKayaks, 'standardrate': 174, 'actualQ': numKayaks, 'standardQ': numKayaks}, 
'type1worker': {'actualrate': 2020/101, 'standardrate': 20, 'actualQ': 101, 'standardQ': 3*numKayaks},
'type2worker': {'actualrate': 2518.50/146, 'standardrate': 17, 'actualQ': 146, 'standardQ': 4*numKayaks}
}

#6 - double check encoding
items2 = {
'materials': {'actualrate': 122.00, 'standardrate': 124.00, 'actualQ': 1176, 'standardQ': 1140},
'labour': {'actualrate': 16.00, 'standardrate': 13.00, 'actualQ': 4120, 'standardQ': 4340}
}

takiItems = {
'powder': {'actualrate': 2023.2 / 1190, 'standardrate': 1.50, 'actualQ': 1190.0 / 1, 'standardQ': 52*20},
'finishingkit': {'actualrate': 3220/20, 'standardrate': 168, 'actualQ': 20, 'standardQ': 20},
'type1work': {'actualrate': 784/56, 'standardrate': 14, 'actualQ': 56, 'standardQ': 3*20},
'type2work': {'actualrate': 978.75/87, 'standardrate': 11, 'actualQ': 87, 'standardQ': 4*20}

}

taki2 = {
'materials': {'actualrate': 128.00, 'standardrate': 130.00, 'actualQ': 1236, 'standardQ': 1200},
'labour': {'actualrate': 16.9, 'standardrate': 13.9, 'actualQ': 4360.0, 'standardQ': 4610.0}
}

for item in items:
	print("#", item, "#", sep="")
	print('quantity', calcQuantityVar(items[item]))
	print('price', calcPriceVar(items[item]))
	print()

for item in items2:
	print("###q6###")
	print("#", item, "#", sep="")
	print('totalVar', calcTotalVar(items2[item]))
	print('price', calcPriceVar(items2[item]))
	print('quantity', calcQuantityVar(items2[item]))
	print()
	
print("##Taki##")
for item in takiItems:
	print(item)
	print('price', calcPriceVar(takiItems[item]))
	print('quantity', calcQuantityVar(takiItems[item]))
	print()

for item in taki2:
	print(item)
	print('total', calcTotalVar(taki2[item]))
	print('price', calcPriceVar(taki2[item]))
	print('quantity', calcQuantityVar(taki2[item]))
