import allireland

def instruction():
	print("\nEnter the letter of your choice :")
	print( "(A) to display a sorted list of the counties")
	print( "(B) display the total numer of titles won ")
	print( "(C) dsipaly which county has the most titles")
	print( "(D) Display the county who wom the most to leat All Irelands")
	print( "(E) Display the couties who won X number of title")
	print( "(F) Displays the counties who won X number of All Irelands ")
	print( "(Q) to quit ")
	print( "\n\n")


def get_choice():
	options =['a','b','c','d','e','f','q']
	choice =True
	while(choice):
		try:
			option = input("Enter your option A-F or Q\n")
			option = option.lower()
			if option not in options:
				raise ValueError
			choice = False
		except ValueError:
			print('You must enter option A - F or press Q to quit:')

	return option





#option a
def get_county():
	''' Displays a  sorted list of all the counties  '''
	county = sorted(set(allireland.allireland_winners.keys()))
	return "\n".join(str(x) for x in county)


#oprtion b	
def total_titles():
	''' display the tottal numer of titles won'''
	return sum(list(allireland.allireland_winners.values()))

#option c
def most_titles():
	''' County who won the most titles '''
	max_titles = max(list(allireland.allireland_winners.values()))
	return list(allireland.allireland_winners.keys())[list(allireland.allireland_winners.values()).index(max_titles)]

#option d	
def mostToLeast():
	'''Display the county who wom the most to leat All Irelands  '''
	most_to_least = sorted([(v,k) for k,v in allireland.allireland_winners.items()])
	return "\n".join(str(x) for x in most_to_least[::-1])


	
#option e
def no_of_titles(no_of_titles_won):
	''' Display the couties who won X number of title . ie Dublin won 28  '''
	print("Workining .....")
	for k, v in allireland.allireland_winners.items():
		if v== no_of_titles_won:
			print(k)
	


#option f
def no_of_ulster_wins():
	''' Dispaly the Counyt in Ulster who won the mos All Ireland '''
	no_of_titles_in_ulster=0

	allireland_ulster_list=list(allireland.ulster)
	allireland_winners_list = list(allireland.allireland_winners)

	ulster_wins=0
	for i  in range(len(allireland_ulster_list)):
		if allireland_ulster_list[i] in allireland.allireland_winners :
			ulster_teams =allireland_ulster_list[i]
			#print(allireland_ulster_list[i])
			if allireland.allireland_winners[ulster_teams] > 0 :
				ulster_wins += allireland.allireland_winners.get(ulster_teams)
	return ulster_wins


def no_of_connacht_wins():
	''' Dispaly the Counyt in Connacht who won the mos All Ireland '''

	no_of_titles_in_connacht=0

	allireland_connacht_list=list(allireland.connacht)
	allireland_winners_list = list(allireland.allireland_winners)

	connacht_wins=0
	for i  in range(len(allireland_connacht_list)):
		if allireland_connacht_list[i] in allireland.allireland_winners :
			connacht_teams =allireland_connacht_list[i]
			#print(allireland_connacht_list[i])
			if allireland.allireland_winners[connacht_teams] > 0 :
				connacht_wins += allireland.allireland_winners.get(connacht_teams)
	return connacht_wins



def no_of_leinster_wins():
	''' Dispaly the Counyt in Leinster who won the mos All Ireland '''

	no_of_titles_in_leinster=0

	allireland_leinster_list=list(allireland.leinster)
	allireland_winners_list = list(allireland.allireland_winners)

	leinster_wins=0
	for i  in range(len(allireland_leinster_list)):
		if allireland_leinster_list[i] in allireland.allireland_winners :
			leinster_teams =allireland_leinster_list[i]
			
			if allireland.allireland_winners[leinster_teams] > 0 :
				leinster_wins += allireland.allireland_winners.get(leinster_teams)
	return leinster_wins


''' Dispaly the Counyt in Munster who won the mos All Ireland '''
def no_of_munster_wins():

	no_of_titles_in_munster=0

	allireland_munster_list=list(allireland.munster)
	allireland_winners_list = list(allireland.allireland_winners)

	munster_wins=0
	for i  in range(len(allireland_munster_list)):
		if allireland_munster_list[i] in allireland.allireland_winners :
			munster_teams =allireland_munster_list[i]
			#print(allireland_munster_list[i])
			if allireland.allireland_winners[munster_teams] > 0 :
				munster_wins += allireland.allireland_winners.get(munster_teams)
	return munster_wins

def add_title_to(x):
	allireland_winners_list = list(allireland.allireland_winners)
	try:
		if x not in allireland_winners_list:
			raise ValueError('Not in All Ireland ')

		elif x in allireland_winners_list:
			return (x + str(1))
	except ValueError as ve:
		print(ve)
		


run_program = True

print('WELECOME\n')
print(add_title_to(1))

while(run_program):
	instruction()
	
	option = get_choice()

	if option == 'q':
		run_program =False
		print("Good bye!!")

	elif option== 'a':
		print("\nThe following Counties are and in the All Ireland\n{} ".format(get_county()))
	elif option == 'b':
		print("\nTotal number of All Ireland titles won:\n {}".format(total_titles()))
	elif option == 'c':
		print("\nThe county with the most All irelnad is:{}\n".format(most_titles()))
	elif  option == 'd':
		print("\nList of  counties , from most wins to least{}\n".format(mostToLeast()))
	elif  option == 'e':
		x =input("Enter  number of tiles :\n")
		print(no_of_titles(int(x)))
	elif  option == 'f':
		prov =input("Enter  provance name  :\n")
		prov=prov.lower()
		
		if prov == 'ulster':
			print(f'{prov}  has : {no_of_ulster_wins()} \n')
		elif prov == 'connacht':
			print(f'{prov}  has : {no_of_connacht_wins()} \n')
		elif prov == 'munster':
			print(f'{prov}  has : {no_of_munster_wins()} \n')
		elif prov == 'leinster':
			print(f'{prov}  has : {no_of_leinster_wins()} \n')

		
		
