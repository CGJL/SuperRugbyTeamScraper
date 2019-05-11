import pandas as pd
import requests 
import re

agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
site = requests.get("https://www.foxsports.com.au/rugby/super-rugby/lineups", headers=agent)


t = []
dfs = pd.read_html(site.text)
a = []
for df in dfs:
	print(df)
	print("-"*len(df)*2)
	a.append(df.values)

# print(a)


# b = [
# "LHP",
# "HOOK",
# "THP",
# "LCK1",
# "LCK2",
# "BSFL",
# "NUM8",
# "OSFL",
# "SHLF",
# "FHLF",
# "LWNG",
# "ICEN",
# "OCEN",
# "RWNG",
# "FBCK",
# "RHKR",
# "RPRP",
# "RLCK",
# "RFL",
# "RHLF",
# "RBCK"]

