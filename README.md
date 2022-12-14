Svelte Markdown https://github.com/pablo-abc/svelte-markdown (3k/week)  
marked          https://github.com/markedjs/marked           (6.7M/week)  

## Inledning

Idéen är att webansvarig huvudsakligen ska arbeta i [MarkDown](https://en.wikipedia.org/wiki/Markdown).

Om Markdown inte räcker till, kan man skriva HTML i samma fil. Hela filen kan vara HTML om så behövs.

* Makron finns definierade för att underlätta redigering.
	* $B = https://storage.googleapis.com/bildbanken2/index.html
	* $T = https://member.schack.se/ShowTournamentServlet

Arbetsgången blir:
* Skapa/Modifiera .md-fil
* Modifiera menu.tree om behov finns
* Kör build.py som uppdaterar site.json mha *.md och menu.tree
* rsync till Google Cloud Storage

## GUI

Gui:t består av en trädmeny till vänster samt en yta till höger för en eller flera md-poster.

* Input: Search
* Button: Up to parent
* Button: Clear, Share, Help
* Label: Current Directory
* Buttons: Down to children

## Meny

* Uppbyggd med javascript-objekt. Löven består av en URL, ett filnamn eller en md-post.
* Vissa md-poster är nåbara via menyn. De flesta måste dock sökas fram.
	* Alternativt skrollar man fram dem mha infinity scroll.
	* Posterna kan egentligen klassificeras i flera dimensioner men kataloghierarkin kan ej återge det.
	* Tags behövs inte eftersom allt är sökbart.
* Använd **TAB** för indentering
* Observera: kolon + mellanslag skiljer menytext från filnamn.
* Exempel:
```
Välkommen till Wasa SK
	Välkommen till Wasa SK: 2000-01-01 Välkommen till Wasa SK.md
	Medlemskap i Wasa: 2000-01-01 Medlemskap i Wasa.md
	Rating: https://resultat.schack.se/ShowClubRatingServlet?clubid=38481
Aktuellt
	Speldatum: 2022-06-30 Speldatum.md
```

## Katalogstruktur
```
Home
	[md]
		2022-10-11 Junior-DM i blixt.md
		inbjudningar.md
	[public] (endast denna katalog rsyncas till Google Cloud Storage)
		[build]
			bundle.css
			bundle.js
			bundle.js.map
		favicon.png
		[files]
		global.css
		index.html
		site.json
	[src]
		App.svelte
		main.js
	build.py
```

# Kommandon
* npm run dev
* npm run build
* build.py
* rsync

# Markdown
*   Man kan alltid skriva om till HTML i .md-filen om inget annat hjälper
*   Påverka styles med .css. (t ex table)

