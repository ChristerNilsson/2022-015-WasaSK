Svelte Markdown https://github.com/pablo-abc/svelte-markdown (3k/week)  
marked          https://github.com/markedjs/marked           (6.7M/week)  

## Inledning

Idéen är att webansvarig huvudsakligen ska arbeta i [MarkDown](https://en.wikipedia.org/wiki/Markdown).

Om Markdown inte räcker till, kan man skriva HTML i samma fil.

Om man är ännu bekvämare, kan man använda några makros ($X, $Y, osv), jag tagit fram. Dessa är definierade i build.py
De är dock helt specialiserade för schack och hämtar data från member.schack.se mha build.py

Arbetsgången blir:
* Skapa/Modifiera .md-fil
* Modifiera menu.txt
* Kör build.py som uppdaterar site.json mha *.md och menu.txt
* rsync till Google Cloud Storage

md-fil ev med makros => site.json => html

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
```
{
	Home: (Visar senaste posterna)
	Klubben: {
		Välkommen till Wasa SK : .md
		Medlemskap i Wasa: .md
		Styrelsen : .md
		Rating: url
	}
	Inbjudningar: inbjudan.md
	Juniorer: {
		Tid och plats:
		Program: junior.md
		Föräldrainfo: foraldrainfo.pdf
		Blankett: blankett.pdf
	}
	Seniorer:{
		Tid och plats: .md
		Program: senior.md
		Facebook: url
		Svenska Lag: url
		Blanketter: {
			Nya medlemmar: .pdf
			Byte av huvudklubb: .pdf
		}
	}
	Bildbanken: bildbanken.se
	Länkar, länkar och åter länkar
}
```

## Katalogstruktur
```
Home
	md
		2022-10-11A Junior-DM i blixt.md
		inbjudningar.md
	public (endast denna katalog rsyncas till Google Cloud Storage)
		build
			bundle.css
			bundle.js
			bundle.js.map
		favicon.png
		global.css
		index.html
		site.json
	src
		App.svelte
		main.js
	build.py
```

# Kommandon
* npm run dev
* npm run build
* build.py
* rsync