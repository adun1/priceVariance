#!/usr/bin/python3

def calcPriceVar(item):
    return item['standardQ'] * (item['actualrate'] - item['standardrate'])
    
def calcQuantityVar():
    return
    
type1worker = {actualrate: 2020/101, standardrate: 20, actualQ: 101/35, standardQ: 3}
print(calcPriceVar(type1worker))