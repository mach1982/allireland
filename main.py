import allireland


def get_county():
	county = sorted(set(allireland.allireland_winners.keys()))
	return "\n".join(str(x) for x in county)


	
def total_titles():
	return sum(list(allireland.allireland_winners.values()))

def most_titles():
	max_titles = max(list(allireland.allireland_winners.values()))
	return list(allireland.allireland_winners.keys())[list(allireland.allireland_winners.values()).index(max_titles)]

	
def mostToLeast():
	most_to_least = sorted([(v,k) for k,v in allireland.allireland_winners.items()])
	return "\n".join(str(x) for x in most_to_least[::-1])


	
#print(get_county())

def no_of_titles(no_of_titles_won):
	for k, v in allireland.allireland_winners.items():
		if v == no_of_titles_won:
			print(k)
	

def no_of_ulster_wins():

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

print(no_of_ulster_wins())

		

		
		
		
		


		
	
	
#print(get_county())
#print(mostToLeast())
