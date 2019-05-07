#benchies[team][player]
#startinglineup[team][player]
import requests
from bs4 import BeautifulSoup
import re




result = requests.get("https://www.sport24.co.za/Rugby/SuperRugby/super-rugby-weekend-teams-20190211-3")

# print(result.status_code)   
src = result.content
soup = BeautifulSoup(src, 'lxml')

teamnames = soup.find_all("span")
titles = soup.find_all("p")

startinglineup = []
benchies = []
finalfifteen = []
finalbench = []
matchups = []
finalmatchups = []

for name in teamnames:
	team  = re.findall(r'\w+\s\bv\b\s\w+', name.text)
	matchups.append(team)
 

for i in range(len(matchups)):
	for j in range(len(matchups[i])):
		finalmatchups.append(matchups[i][j])
		finalmatchups.append(matchups[i][j])
print(finalmatchups)

for title in titles:
	if "15" and "12" and "1" and "13" in title.text:

		starters = re.findall(r'\d{1,2}\s[a-zA-Z\W?][^,]{0,50}', title.text)
		startinglineup.append(starters)





for firstfifteen in startinglineup:
	templist = []
	firstfifteen.reverse()
	for player in firstfifteen:

		if '\n' in player:
			player = player.split('\n')
			player = "".join(player)
			templist.append(player)
		if '\xa0' in player:
			player = player.split('\xa0')
			player = " ".join(player)
			templist.append(player)
		templist.append(player)
	finalfifteen.append(templist)
		


for title in titles:
	if "16" and "18" and "22" in title.text:
		bench = re.findall(r'\d{1,2}\s[a-zA-Z\W?][^,]{0,50}', title.text)
		benchies.append(bench)

for bencheight in benchies:	
	templist2 = []
	for player in bencheight:
		if '\n' in player:
			player = player.split('\n')
			player = "".join(player)
			templist2.append(player)
			
		if '\xa0' in player:
			player = player.split('\xa0')
			player = " ".join(player)
			templist2.append(player)
		templist2.append(player)
	finalbench.append(templist2)	
		

for i in range(len(finalfifteen)):
	print('_'*len(finalmatchups[i]))
	print(finalmatchups[i])
	print('_'*len(finalmatchups[i]))
	for x in range(len(finalfifteen[i])):
		print(finalfifteen[i][x])
	print()
	print("Substitutes:")	
	for y in range(len(finalbench[i])):
		print(finalbench[i][y])
	print()






		