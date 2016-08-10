# -*- coding: utf-8 -*-

import pickle 

symbols = pickle.load( open( "config.cfg", "rb" ) ) 

def symb_change(num,symb):
	symbols[str(num)]=symb
	pickle.dump(symbols, open("config.cfg","wb"))
	print(symbols)
	print(symbols[str(num)])

user_number = raw_input("Enter the number of the which you wish to change: ")
user_symbol = raw_input("Enter the symbol you want to be binded: ") 

symb_change(user_number,user_symbol)


