<script>
  import SvelteMarkdown from 'svelte-markdown'
  const source = `
Lag|Serie|1|2|3|4|5|6|7|Lagledare|Telefon
-|-|:-:|:-:|:-:|:-:|:-:|:-:|:-:|-|-
Wasa SK II|[DIV II:3](https://member.schack.se/ShowTournamentServlet?id=10430)|[23/10](https://storage.googleapis.com/bildbanken2/index.html?query=2022-10-23)|[13/11](https://storage.googleapis.com/bildbanken2/index.html?query=2022-11-13)|[04/12](https://storage.googleapis.com/bildbanken2/index.html?query=2022-12-04)|[15/01](https://storage.googleapis.com/bildbanken2/index.html?query=2023-01-15)|[05/02](https://storage.googleapis.com/bildbanken2/index.html?query=2023-02-05)|[05/03](https://storage.googleapis.com/bildbanken2/index.html?query=2023-03-05)|[19/03](https://storage.googleapis.com/bildbanken2/index.html?query=2023-03-19)|Birger Wenzel|076 - 123 45 67
Wasa SK III|[DIV II:3](https://member.schack.se/ShowTournamentServlet?id=10430)|[23/10](https://storage.googleapis.com/bildbanken2/index.html?query=2022-10-23)|[13/11](https://storage.googleapis.com/bildbanken2/index.html?query=2022-11-13)|[04/12](https://storage.googleapis.com/bildbanken2/index.html?query=2022-12-04)|[15/01](https://storage.googleapis.com/bildbanken2/index.html?query=2023-01-15)|[05/02](https://storage.googleapis.com/bildbanken2/index.html?query=2023-02-05)|[05/03](https://storage.googleapis.com/bildbanken2/index.html?query=2023-03-05)|[19/03](https://storage.googleapis.com/bildbanken2/index.html?query=2023-03-19)|Niclas Hedin|073 - 645 34 07

Lag|Serie|1|2|3|4|5|Lagledare|Telefon
-|-|:-:|:-:|:-:|:-:|:-:|-|-
Wasa SK|[Elitserien](https://member.schack.se/ShowTournamentServlet?id=10508)|[19/09](https://storage.googleapis.com/bildbanken2/index.html?query=2022-09-19)|[17/10](https://storage.googleapis.com/bildbanken2/index.html?query=2022-10-17)|[14/11](https://storage.googleapis.com/bildbanken2/index.html?query=2022-11-14)|[12/12](https://storage.googleapis.com/bildbanken2/index.html?query=2022-12-12)|[30/01](https://storage.googleapis.com/bildbanken2/index.html?query=2023-01-30)|Birger Wenzel|076 - 123 45 67
Wasa SK II|[Division 1](https://member.schack.se/ShowTournamentServlet?id=10509)|[26/09](https://storage.googleapis.com/bildbanken2/index.html?query=2022-09-26)|[24/10](https://storage.googleapis.com/bildbanken2/index.html?query=2022-10-24)|[21/11](https://storage.googleapis.com/bildbanken2/index.html?query=2022-11-21)|[19/12](https://storage.googleapis.com/bildbanken2/index.html?query=2022-12-19)|[06/02](https://storage.googleapis.com/bildbanken2/index.html?query=2023-02-06)|Karl-Gustav Sjölund|073 - 645 34 07
Wasa SK III|[Division 2](https://member.schack.se/ShowTournamentServlet?id=10510)|[03/10](https://storage.googleapis.com/bildbanken2/index.html?query=2022-10-03)|[31/10](https://storage.googleapis.com/bildbanken2/index.html?query=2022-10-31)|[28/11](https://storage.googleapis.com/bildbanken2/index.html?query=2022-11-28)|[16/01](https://storage.googleapis.com/bildbanken2/index.html?query=2023-01-16)|[13/02](https://storage.googleapis.com/bildbanken2/index.html?query=2023-02-13)|Birger Wenzel|076 - 123 45 67
Wasa SK IV|[Division 3](https://member.schack.se/ShowTournamentServlet?id=10511)|[10/10](https://storage.googleapis.com/bildbanken2/index.html?query=2022-10-10)|[07/11](https://storage.googleapis.com/bildbanken2/index.html?query=2022-11-07)|[05/12](https://storage.googleapis.com/bildbanken2/index.html?query=2022-12-05)|[23/01](https://storage.googleapis.com/bildbanken2/index.html?query=2023-01-23)|[20/02](https://storage.googleapis.com/bildbanken2/index.html?query=2023-02-20)|Birger Wenzel|076 - 123 45 67
Wasa SK V|[Division 4](https://member.schack.se/ShowTournamentServlet?id=10512)|[10/10](https://storage.googleapis.com/bildbanken2/index.html?query=2022-10-10)|[07/11](https://storage.googleapis.com/bildbanken2/index.html?query=2022-11-07)|[05/12](https://storage.googleapis.com/bildbanken2/index.html?query=2022-12-05)|[23/01](https://storage.googleapis.com/bildbanken2/index.html?query=2023-01-23)|[20/02](https://storage.googleapis.com/bildbanken2/index.html?query=2023-02-20)|Birger Wenzel|076 - 123 45 67
Wasa SK VI|[Division 5](https://member.schack.se/ShowTournamentServlet?id=10513)|[03/10](https://storage.googleapis.com/bildbanken2/index.html?query=2022-10-03)|[31/10](https://storage.googleapis.com/bildbanken2/index.html?query=2022-10-31)|[28/11](https://storage.googleapis.com/bildbanken2/index.html?query=2022-11-28)|[16/01](https://storage.googleapis.com/bildbanken2/index.html?query=2023-01-16)|[13/02](https://storage.googleapis.com/bildbanken2/index.html?query=2023-02-13)|Birger Wenzel|076 - 123 45 67

### November 2022
Namn|Ort|Datum|Anmälan|Resultat
-|-|-|-|-
[Göstas Minne](https://wasask.se/Inbjudan_Gostas_minnesturnering_2022.pdf)|Katarina_Södra_Skola,_Stockholm|2022-11-27||[Resultat](https://member.schack.se/ShowTournamentServlet?id=10769)
### December 2022
Namn|Ort|Datum|Anmälan|Resultat
-|-|-|-|-
[Flickornas JGP-final](https://wasask.se/Flickornas_JGP-final_2022.pdf)|Stockholm|**2022-12-03**||[Resultat](https://member.schack.se/ShowTournamentServlet?id=10885)
[**JGP-finaler**](https://wasask.se/Inbjudan-JGP-finaler_2022.pdf)|Stockholm|**2022-12-10 .. 2022-12-11**||
[Pia Cramlings Online-schacktävling](https://wasask.se/Inbjudan_Tjejt%C3%A4vlingen_online_december_2022.pdf)|Lichess.org|2022-12-16||
[Malmö Open - GP](https://wasask.se/malmoopeninbj2022.pdf)|Malmö|2022-12-16 .. 2022-12-18|[Anmäl dig här](https://member.schack.se/turnering/3069/anmalan)|[Anmälda](https://member.schack.se/ShowTournamentServlet?id=10376)
[Karlstad Open](https://wasask.se/Karlstad-Open-2022-inbjudan.pdf)|Karlstad|2022-12-27 .. 2022-12-30|[Anmäl dig här](https://member.schack.se/turnering/3288/anmalan)|[Anmälda](https://member.schack.se/ShowTournamentServlet?id=10768)
[Rilton Amatör](https://wasask.se/Riltonamator28dec22B.pdf)|Stockholm|2022-12-28||
[Rilton Cup & Rilton ELO](https://wasask.se/Inbjudan_Rilton_Cup_svenska_2022_2023.pdf)|Stockholm|2022-12-27 .. 2023-01-05|[Anmäl dig här](https://chess-results.com/Anmeldung.aspx?lan=6&tnr=661619)|[Anmälda](https://chess-results.com/tnr661619.aspx?lan=6)
`
</script>

<SvelteMarkdown {source} />

<style>
  :global(table) {border-collapse: collapse;}
  :global(table td) {padding: 5px}
  :global(table thead) {
    background-color: #000;
    color: #ff0;
    font-size: 14px;
    border: 1px solid #555;
  }
  :global(table tbody td) {border: 1px solid #555;}
  :global(table tbody tr) {background-color: #eee;}
  :global(table tbody tr:nth-child(odd)) {background-color: #fff;}
</style>