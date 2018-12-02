
# a dictionary stores the number of titles
allireland_winners = { 'Antrim': 0,
                       'Armagh': 1,
                       'Carlow': 0,
                       'Cavan': 5,
                       'Clare': 0,
                       'Cork': 7,
                       'Derry': 1,
                       'Donegal': 2,
                       'Down': 5,
                       'Dublin': 28,
                       'Fermanagh': 0,
                       'Galway': 9,
                       'Kerry': 37,
                       'Kildare': 4,
                       'Kilkenny': 0,
                       'Laois': 0,
                       'Leitrim': 0,
                       'Limerick': 2,
                       'Longford': 0,
                       'Louth': 3,
                       'Mayo': 3,
                       'Meath': 7,
                       'Monaghan': 0,
                       'Offaly': 3,
                       'Roscommon': 2,
                       'Sligo': 0,
                       'Tipperary': 4,
                       'Tyrone': 3,
                       'Waterford': 0,
                       'Westmeath': 0,
                       'Wexford': 5,
                       'Wicklow': 0,
                       }

# sets hold the counties per provance 
connacht = {"Galway", "Leitrim", "Roscommon", "Mayo", "Sligo"}

leinster = set(['Carlow', 'Dublin', 'Kildare', 'Kilkenny', 'Laois',
                'Longford', 'Louth', 'Meath', 'Offaly', 'Westmeath',
                'Wexford', 'Wicklow'])

munster = {'Clare', 'Cork', 'Kerry', 'Limerick', 'Tipperary', 'Waterford'}

ulster = set(['Antrim', 'Armagh', 'Cavan', 'Donegal', 'Down',
              'Fermanagh', 'Derry', 'Monaghan', 'Tyrone'])




##print(allireland_winners)
##print(connacht)
##print(leinster)
##print(munster)
##print(ulster)
##print(allireland_winners['Down'])

# 1) create set of all the counties in Ireland using set methonds
# 2) ** Write at least one function for each of the following: **
#   * List all the counties in alabetical order?
#   * List all the counties in order of titles most to least?
#   * How many All Ireland have been won in total?
#   * Calculate who has won the most titles?
#   * How many counties have won x amount of titles.
#   * How many titles have been won by:
#       Connacht?
#       Leinster?
#       Munster?
#       Ulster?

# 3) write function add_title_to that adds 1 to the named county.
# It should raise and exception if the argument is not a valid county. 


