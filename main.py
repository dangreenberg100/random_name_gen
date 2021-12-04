import random #to choose random name

entries = int(input('How many names would you like to enter?: ')) # takes an input in for the name

name = [str(input('Enter the name of each person/s: ')) for i in range(0, entries)] #stores peoples name

def randomchooser(list):
	'''Chooses random name'''
	x = random.choice(list)#chooses name
	print(f'The random name selected was {x}!')#returns to user

randomchooser(name)