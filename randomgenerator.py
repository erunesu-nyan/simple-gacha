import random
import json

def gen_name():
	with open('names.json') as f:
	  listofnames = json.load(f)
	return gen(listofnames)

def gen_rarity():
	listofweightedrarity = ['SSR']*1 + ['SR']*9 + ['R']*40 + ['N']*50
	return gen(listofweightedrarity)

def gen_name():
	with open('races.json') as f:
	  listofraces = json.load(f)
	return gen(listofraces)

def gen(listofsomething):
	result = random.choice(listofsomething)
	return result
	
