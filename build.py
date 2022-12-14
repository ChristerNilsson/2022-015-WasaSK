import json
import time
from os import scandir

def intro():
	pass

MACROS = {}
MACROS['$B'] = "https://storage.googleapis.com/bildbanken2/index.html"
MACROS['$A'] = "https://member.schack.se/turnering"
MACROS['$T'] = "https://member.schack.se/ShowTournamentServlet"

def pr(s): return s.replace("_"," ")
def split(s): return list(filter(lambda x: x != "",s.split(' ')))
def tel(s): return s[0:3] + ' - ' + s[4:7] + " " + s[7:9] + " " + s[9:11]

def level(s): return s.count('\t')

def indented2object(raw):
	def pop(n):
		for i in range(n): stack.pop()
	lst = raw.split('\n')
	levels = [level(item) for item in lst]
	tree = {}
	stack = []
	for i in range(len(lst)):
		if lst[i] == "": continue
		if i != 0:
			delta = levels[i] - levels[i-1]
			if delta < 0: pop(len(stack) - levels[i])
			elif delta == 0: stack.pop()
		stack.append(lst[i].strip())
		pos = tree
		for j in range(len(stack)-1):
			pos = pos[stack[j]]

		name = stack[-1]
		arr = name.split(': ')
		if len(arr)==1:
			pos[name] = {}
		else:
			key,filename = arr
			if filename.startswith('http') or filename.endswith('.md') and filename in files_md or filename in files_files:
				pos[key] = filename
			else:
				print('Filen saknas:', filename)

	return tree

def getNames(path):
	res = []
	for name in [f for f in scandir(path)]:
		res.append(name.name)
	res.sort()
	res.reverse()
	return res

def readMenuTree():
	with open('menu.tree', 'r', encoding="utf-8") as f:
		return indented2object(f.read())

def dumpjson(data,f):
	s = json.dumps(data, ensure_ascii=False, separators=(",", ":"), sort_keys=False)
	s = s.replace("],","],\n")
	s = s.replace(":{",":\n{")
	s = s.replace('},"','},\n"')
	s = s.replace('","','",\n"')
	f.write(s)

start = time.time()

files_md = getNames("md")
files_files = getNames("public/files")

mdData = {}
for filename in files_md:
	with open('md/'+filename, 'r', encoding="utf-8") as f:
		s = f.read()
		for key in MACROS:
				s = s.replace(key,MACROS[key])
		if filename[0:2]=="20":
			s = "## " + filename[11:-3] + "\n_" + filename[0:10] + "_\n\n" + s
		else:
			s = "## " + filename[:-3] + "\n" + s
		mdData[filename] = s

menu = readMenuTree()
total = {"menu":menu, "md": mdData}

with open("src/site.json", "w", encoding="utf8") as f:
	dumpjson(total,f)

print('Macros:',MACROS)
print('Poster:',len(files_md))
print('Filer:',len(files_files))

print('Körtid:',round(time.time()-start,3),'s')

########### graveyard ################

# raw = """animal
# \tcarnivorous
# \t\ttiger
# \t\tlion
# \tvegetarian
# \t\tcow
# \t\tsheep
# plant
# \talgea
# \ttree
# \t\tleaf
# \t\tpine
# \tfungus
# \t\tgood
# \t\tbad
# \t\t\tevil
# \t\t\tmean
# \tcactus
# \t\tbig
# \t\tsmall"""

# menu.tree

# raw = """Välkommen till Wasa SK
# 	Välkommen till Wasa SK: .md
# 	Medlemskap i Wasa: .md
# 	Rating: https://resultat.schack.se/ShowClubRatingServlet?clubid=38481
# Aktuellt
# 	Speldatum: .md
# Inbjudningar
# 	Juli-December 2022: .md
# 	Januari-Juni 2023: .md
# Bildbanken 2.0: storage.googleapis.com/bildbanken2/index.html
# Lag-DM i Stockholm: .md
# Kursmaterial: .pdf
# Wasa-Juniorerna
# 	Juniorer
# 		Svenskalag: https://www.svenskalag.se/wasask-juniorer
# 		Program: JuniorerProgram.md
# 	Föräldrainfo: .md
# 	Inför terminstarten: .pdf
# 	Aktiviteter
# 		Schackläger på Beatelund: https://player.vimeo.com/video/724273589
# 	Schack4an: https://schack.se/schackfyran/schackfyranmastaren
# 	Schack4an Stockholm: http://www.s4sthlm.se
# 	Tävlingar 2022
# 		Schack-SM: .md
# 		Uppsala Chess Festival: .md
# 		Minior-Lag-DM: .md
# 		Skol-SM: .md
# 		Rockadenjunioren: .md
# 		JDM i blixt: .md
# 		Kristallens JGP: .md
# 		Trojanska Hästen: .md
# 	Blanketter
# 		Ansökan: .pdf
# Seniorer
# 	Program: SeniorerProgram.md
# 	Facebook: https://www.facebook.com/WasaSK
# 	Svenskalag: https://www.svenskalag.se/wasask
# 	Tävlingar
# 		Schack-SM 2022: .md
# 		Bilder från KM: https://bildbanken.schack.se/?query&folder=1kiMjh4UlbsUEyw0De2sLJ_ypuqp_Apsu
# 	Aktiviteter
# 		Gästföreläsning: https://bildbanken.schack.se/?query&folder=1AW8pTtQibmslCzN5x1YqoxFOvdI87n95
# 	Blanketter
# 		Nya medlemmar: .pdf
# 		Byte av huvudklubb: .pdf
# Arkiv: http://wasask.se/arkiv_frames_wasa.html
# Övrigt: http://wasask.se/ovrigt_frames_wasa.html
# Schackorganisationer
# 	FIDE: http://www.fide.com
# 	Sveriges Schackförbund: http://www.schack.se
# 	Stockholms Schackförbund: http://www.stockholmsschack.se
# 	Rilton Cup: http://rilton.se
# Schackbloggar
# 	Inte bara schack: http://larsgrahn.blogspot.se
# 	Lelleschack: http://lelleschack.bloggo.nu
# 	Magnus Carlsen: https://twitter.com/magnuscarlsen
# 	Näringslivet möter förorten: https://naringslivetmoterfororten.se
# 	Schackelina: https://schackelina.bloggo.nu
# 	Schacksnack: http://www.schacksnack.se
# 	Bergens Schakklub: https://bergensjakk.no
# 	Dansk Skak Union: https://skak.dk
# 	Tata Steel Chess: https://tatasteelchess.com
# 	Uppsala Young Champions: https://www.uppsalayoungchampions.se
# Schackbutiker
# 	Wasa Schackshop: https://wasask.se/Wasa Schackshop - Prislista vid JGP 2022.pdf
# 	Svenska Schackbutiken: http://www.schackbutiken.se"""

# assert g(raw) == {
# 'animal': {
# 	'carnivorous': {
# 		'tiger': {},
# 		'lion': {}},
# 	'vegetarian': {
# 		'cow': {},
# 		'sheep': {}}},
# 'plant': {
# 	'algea': {},
# 	'tree': {
# 		'leaf': {},
# 		'pine': {}},
# 	'fungus': {
# 		'good': {},
# 		'bad': {
# 			'evil': {},
# 			'mean': {}}},
# 	'cactus': {
# 		'big': {},
# 		'small': {}}}}

# R = -1
# lst = ["A","\tB","\t\tC","\t\tD"]
#levels = [0,1,0]
#parents = [R,0,R]

# def recurse(node, i=0, lvl=0):
# 	if i == len(lst): return "x"
# 	s = lst[i].strip()
# 	l = levels[i]
# 	if l == lvl:
# 		node[s] = recurse(node,i+1,l)
# 	return node

#levels = []
#stack = []

# def f(lst):
# 	global stack
# 	n = len(lst)
# 	levels = []
# 	for i in range(n):
# 		levels.append(level(lst[i]))
#
# 	parents = {}
# 	for i in range(n):
# 		key = lst[i].strip()
# 		if levels[i] == 0:
# 			stack = [key]
# 			parents[key] = "root"
# 		elif levels[i] == levels[i-1] + 1:
# 			parents[key] = stack[-1]
# 			stack.append(key)
# 		else:
# 			pop(1 + levels[i-1] - levels[i])
# 			parents[key] = stack[-1]
# 			stack.append(key)
# 	return parents

# def tree(lst):
# 	res = {}
# 	parents = f(lst)
# 	for key in parents:
# 		res[key] = parents[key]

# Z = ""
# assert f(["A","\tB","\t\tC","D"]) == {'A': 'root', 'B': 'A', 'C': 'B', 'D': 'root'}
# assert f(["A","\tB","\t\tC","\tD"]) == {'A': 'root', 'B': 'A', 'C': 'B', 'D': 'A'}
# assert f(["A","\tB","\t\tC","\t\tD"]) == {'A': 'root', 'B': 'A', 'C': 'B', 'D': 'B'}
# assert f(["A","\tB","\t\tC","\t\t\tD"]) == {'A': 'root', 'B': 'A', 'C': 'B', 'D': 'C'}
# assert f(["A","\tB","\t\tC","D","E"]) == {'A': 'root', 'B': 'A', 'C': 'B', 'D': 'root', 'E':"root"}
#assert tree(["A","\tB","\t\tC","D"]) == {'A': {'B': {'C':Z}}, 'D': Z}

# def parse_tree(lines):
# 	"""
# 	Parse an indented outline into (level, name, parent) tuples.  Each level
# 	of indentation is 4 spaces.
# 	"""
# 	#regex = re.compile(r'^(?P<indent>(?: {4})*)(?P<name>\S.*)')
# 	regex = re.compile(r'^(?P<indent>(?:\t)*)(?P<name>\S.*)')
# 	stack = []
# 	for line in lines:
# 		match = regex.match(line)
# 		if not match:
# 			raise ValueError('Indentation not a multiple of one tab: "{0}"'.format(line))
# 		level = len(match.group('indent'))
# 		if level > len(stack):
# 			raise ValueError('Indentation too deep: "{0}"'.format(line))
# 		stack[level:] = [match.group('name')]
# 		yield level, match.group('name'), (stack[level - 1] if level else None)


#################################################

# def recurse(nodes, path=""):
# 	for node in nodes:
# 		path1 = path + '.' + node.tag
# 		if path1 == trigger: result.append(node.text)
# 		recurse(node, path1)
#
# def XH(s): # Header
# 	# 0 $XH makronamn
# 	# 1 7   antal ronder
#
# 	arr = split(s)
#
# 	ronder = int(arr[1])
#
# 	s = ["Lag","Serie"]
# 	for rond in range(ronder): s.append(str(rond+1))
# 	s = s + ["Lagledare","Telefon"]
#
# 	t = ["-","-"]
# 	for rond in range(ronder): t.append(":-:")
# 	t = t + ["-","-"]
#
# 	return "|".join(s) + "\n" + "|".join(t)
#
# def X(s):
# 	# 0 makronnamn
# 	# 1 antal ronder
# 	# 2 antal lag
# 	# 3 id
# 	# 4 lag
# 	# 5 serie
# 	# 6 lagledare
# 	# 7 telefon
#
# 	global result
# 	arr = split(s)
#
# 	macro = arr[0]
# 	ronder = int(arr[1])
# 	teams = int(arr[2])
# 	id = arr[3]
# 	lag = pr(arr[4])
# 	serie = pr(arr[5])
# 	lagledare = pr(arr[6])
# 	telefon = tel(arr[7])
#
# 	url = TOUR(id)
# 	html = requests.get(url).text
# 	pq = PyQuery(html)
# 	result = []
# 	recurse(pq)
# 	index0 = 7
# 	rader = teams//2
#
# 	dates = []
#
# 	for rond in range(ronder):
# 		for rad in range(rader):
# 			base     = index0 + rond * rader*14 + rad*14
# 			date     = result[base + 2]
# 			hemmalag = result[base + 4].strip()
# 			bortalag = result[base + 8].strip()
# 			if lag in [hemmalag,bortalag]: dates.append(date)
#
# 	s = lag + "|" + "[" + serie + "](" + url + ")"
#
#
# 	for rond in range(ronder):
# 		d = dates[rond]
#
# 		s += "|[" +d[8:10]+"/"+ d[5:7]+ "](" + BB(dates[rond]) + ")"
# 	s += "|" + lagledare
# 	s += "|" + telefon
# 	return s
#
# def XD(s): # specialare för Monrad, där datum anges explicit
# 	# 0 makronnamn
# 	# 1 antal ronder
# 	# 2 antal lag
# 	# 3 id
# 	# 4 lag
# 	# 5 serie
# 	# 6 lagledare
# 	# 7 telefon
# 	# 8.. datum
#
# 	arr = split(s)
#
# 	macro = arr[0]
# 	ronder = int(arr[1])
# 	teams = int(arr[2])
# 	id = arr[3]
# 	lag = pr(arr[4])
# 	serie = pr(arr[5])
# 	lagledare = pr(arr[6])
# 	telefon = tel(arr[7])
# 	dates = arr[8:]
#
# 	url = TOUR(id)
# 	s = lag + "|" + "[" + serie + "](" + url + ")"
#
# 	for rond in range(ronder):
# 		d = dates[rond]
#
# 		s += "|[" +d[8:10]+"/"+ d[5:7]+ "](" + BB(dates[rond]) + ")"
# 	s += "|" + lagledare
# 	s += "|" + telefon
# 	return s
#
# def YH(s):
# 	s = "Namn Ort Datum Anmälan Resultat".split(" ")
# 	t = "- - - - -".split(" ")
# 	return "|".join(s) + "\n" + "|".join(t)
#
# def YA(s):
# 	# 0 $Y
# 	# 1 namn     (Pjäsen GP)
# 	# 2 ort      (Stockholm)
# 	# 3 datum    (2022-12-16 eller 2022-12-10_2022-12-11 eller **2022-12-10_2022-12-11** (junior))
# 	# 4 anmälan  ( _ = tomt 12345=member.schack annat=annan länk t ex chess-results )
# 	# 5 resultat ( _ = tomt 12345=member.schack annat=annan länk t ex chess-results )
# 	# 6 inbjudan (länk, oftast pdf)
#
# 	arr = split(s)
#
# 	macro = arr[0]
# 	namn = pr(arr[1])
# 	ort = arr[2]
# 	datum = arr[3].replace("_"," .. ")
# 	anmälan = arr[4]
# 	resultat = arr[5]
# 	inbjudan = arr[6]
#
# 	if anmälan=="_": anmälan=""
# 	elif len(anmälan)<=6: anmälan = "[Anmäl dig här](" + ANM(anmälan) + ")"
# 	else: anmälan = "[Anmäl dig här](" + anmälan + ")"
#
# 	if resultat=="_": resultat=""
# 	elif len(resultat)<=6: resultat = "[Anmälda](" + TOUR(resultat) + ")"
# 	else: resultat = "[Anmälda](" + resultat + ")"
#
# 	return "[" + namn + "](" + inbjudan + ")|" + ort + "|" + datum + "|" + anmälan + "|" + resultat
#
# def Y(s):
# 	# 0 $Y
# 	# 1 namn     (Pjäsen GP)
# 	# 2 ort      (Stockholm)
# 	# 3 datum    (2022-12-16 eller 2022-12-10_2022-12-11 eller **2022-12-10_2022-12-11** (junior))
# 	# 4 anmälan  ( _ = tomt 12345=member.schack annat=annan länk t ex chess-results )
# 	# 5 resultat ( _ = tomt 12345=member.schack annat=annan länk t ex chess-results )
# 	# 6 inbjudan (länk, oftast pdf)
#
# 	arr = split(s)
#
# 	macro = arr[0]
# 	namn = pr(arr[1])
# 	ort = arr[2]
# 	datum = arr[3].replace("_"," .. ")
# 	anmälan = ""
# 	resultat = arr[5]
# 	inbjudan = arr[6]
#
# 	if resultat=="_": resultat=""
# 	elif len(resultat)<=6: resultat = "[Resultat](" + TOUR(resultat) + ")"
# 	else: resultat = "[Resultat](" + resultat + ")"
#
# 	return "[" + namn + "](" + inbjudan + ")|" + ort + "|" + datum + "|" + anmälan + "|" + resultat
#
# data = """
# $XH 7
# $X 7 8 10430 Wasa_SK_II  DIV_II:3 Birger_Wenzel       076-1234567
# $X 7 8 10430 Wasa_SK_III DIV_II:3 Niclas_Hedin        073-6453407
#
# $XH 5
# $X 5 6 10508 Wasa_SK Elitserien Birger_Wenzel 076-1234567
# $X 5 6 10509 Wasa_SK_II Division_1 Karl-Gustav_Sjölund 073-6453407
# $X 5 6 10510 Wasa_SK_III Division_2 Birger_Wenzel 076-1234567
# $X 5 6 10511 Wasa_SK_IV Division_3 Birger_Wenzel 076-1234567
# $X 5 6 10512 Wasa_SK_V Division_4 Birger_Wenzel 076-1234567
# $XD 5 8 10513 Wasa_SK_VI Division_5 Birger_Wenzel 076-1234567 2022-10-03 2022-10-31 2022-11-28 2023-01-16 2023-02-13
#
# ### November 2022
# $YH
# $Y Göstas_Minne  Katarina_Södra_Skola,_Stockholm   2022-11-27                _    10769 https://wasask.se/Inbjudan_Gostas_minnesturnering_2022.pdf
# ### December 2022
# $YH
# $Y Flickornas_JGP-final               Stockholm    **2022-12-03**            _    10885 https://wasask.se/Flickornas_JGP-final_2022.pdf
# $Y **JGP-finaler**                    Stockholm    **2022-12-10_2022-12-11** _    _     https://wasask.se/Inbjudan-JGP-finaler_2022.pdf
# $Y Pia_Cramlings_Online-schacktävling Lichess.org  2022-12-16                _    _     https://wasask.se/Inbjudan_Tjejt%C3%A4vlingen_online_december_2022.pdf
# $YA Malmö_Open_-_GP                   Malmö        2022-12-16_2022-12-18     3069 10376 https://wasask.se/malmoopeninbj2022.pdf
# $YA Karlstad_Open                     Karlstad     2022-12-27_2022-12-30     3288 10768 https://wasask.se/Karlstad-Open-2022-inbjudan.pdf
# $YA Rilton_Amatör                     Stockholm    2022-12-28                _    _     https://wasask.se/Riltonamator28dec22B.pdf
# $YA Rilton_Cup_&_Rilton_ELO           Stockholm    2022-12-27_2023-01-05 https://chess-results.com/Anmeldung.aspx?lan=6&tnr=661619 https://chess-results.com/tnr661619.aspx?lan=6 https://wasask.se/Inbjudan_Rilton_Cup_svenska_2022_2023.pdf
# """
#
# hash = {}
#
# hash['$XH']=XH # Header för spelschema
# hash['$X'] =X  # Datum hämtas via screenscraping från member.schack (normalfallet)
# hash['$XD']=XD # Datum hämtas ur inbjudan (specialare)
#
# hash['$YH']=YH # Header för Inbjudan
# hash['$YA']=YA # Inbjudan med Anmälan.  Evenemanget har ej börjat
# hash['$Y'] =Y  # Inbjudan med Resultat. Evenemanget är över
#
#
# def createMD():
# 	for row in data.split("\n"):
# 		if len(row) > 3:
# 			arr = row.split(' ')
# 			if arr[0] in hash: print(hash[arr[0]](row))
# 			else: print(row)
# 		else:
# 			print()
#

# $-makron är ej nödvändiga. Man kan skriva .md eller .html syntax istället.
# Makron => MarkDown => HTML

# Macros hanteras i denna fil. Deras namn består av $ + ett eller två tecken
# Utdata ska uppfylla MarkDown-syntaxen.
# De expanderas till HTML i klienten.

#trigger = '.html.body.div.center.table.table.tr.td.span'
#result = []

# def BB(query): return "https://storage.googleapis.com/bildbanken2/index.html?query=" + query
# def ANM(nr):   return "https://member.schack.se/turnering/" + str(nr) + "/anmalan"
# def TOUR(nr):  return "https://member.schack.se/ShowTournamentServlet?id=" + str(nr)

