<script>
	import _ from "lodash"
	import NavigationVertical from "./NavigationVertical.svelte"
	import NavigationHorisontal from "./NavigationHorisontal.svelte"
	import Search from "./Search.svelte"
	import Swimlane from "./Swimlane.svelte"

	import site from "./site.json"

	const log = console.log
	const range = _.range

	let sokruta = ""
	let buttons

	let sources = _.keys(site.md)
	log(sources)
	let n = sources.length

	let selected = {} // filenames

	$: COLUMNS = _.size(selected) == 1 ? 1 : 2 // 1,2 or 3
	$: WIDTH = 250
	const GAP = 1

	let stack = ["Home"]
	let path = [site.menu]

	const text0 = "text0"
	const text1 = "text1"

	$: keys = _.keys(_.last(path))
	$: log(keys)
	$: log('selected',selected)
	$: log('COLUMNS',COLUMNS)

	let a = 0
	let b = 0 

	$: selected = showAll()
	
	const round = (x,n) => Math.round(x*Math.pow(10,n))/Math.pow(10,n)
	const spreadWidth = (share,WIDTH) => Math.floor((WIDTH-2*GAP*(1/share+1))*share) - 2

	function push(key) {
		const obj = _.isObject(_.last(path)[key])
		if (obj) {
			path.push(_.last(path)[key])
			stack.push(key)
			path = path
			stack = stack
		} else {
			const url = _.last(path)[key]
			if (_.startsWith(url,'http')) {
				window.open(url)
			} else if (_.endsWith(url,'.md')) {
				selected = {}
				selected[url] = 0
			} else { // .pdf etc
				window.open('files/' + url)
			}
		}
	}

	function pop() {
		path.pop()
		stack.pop()
		path = path
		stack = stack
	}

	function showAll() {
		COLUMNS = 2
		selected = {}
		for (const i in _.range(sources.length)) {
			selected[sources[i]] = i % COLUMNS
		}
	 	log('selected',selected)
		return selected
	}

	function noop() {}

	$: w = [innerWidth-WIDTH-10,(innerWidth-WIDTH-20)/2,(innerWidth-WIDTH-30)/3]
	$: p = (COLUMNS==1) ?  [WIDTH] :
				 ((COLUMNS==2) ? [WIDTH,WIDTH+w[1]+10] :
												 [WIDTH,WIDTH+w[2]+10,WIDTH+w[2]+w[2]+20])
	
</script>

<div class="menu">
	<img src="files/WASA_SK_LOGO_v2.png" title="Wasa SK" alt="" style="padding:20px" on:click={()=> selected = showAll()} on:keydown={noop}>
	<Search bind:sokruta {text0} {text1} {stack} {WIDTH} {GAP} {spreadWidth} {_} {pop} />
	<NavigationHorisontal {stack} {WIDTH} />
	<NavigationVertical {keys} {push} {WIDTH} />
</div>

{#if COLUMNS==1}
	<Swimlane col=0 pos={p[0]}px bind:selected {site} width={w[0]}px {showAll} {w} {COLUMNS}/>
{/if}
{#if COLUMNS==2}
	<Swimlane col=0 pos={p[0]}px bind:selected {site} width={w[1]}px {showAll} {w} {COLUMNS} />
	<Swimlane col=1 pos={p[1]}px bind:selected {site} width={w[1]}px {showAll} {w} {COLUMNS} />
{/if}
{#if COLUMNS==3}
	<Swimlane col=0 pos={p[0]}px bind:selected {site} width={w[2]}px {showAll} {w} {COLUMNS} />
	<Swimlane col=1 pos={p[1]}px bind:selected {site} width={w[2]}px {showAll} {w} {COLUMNS} />
	<Swimlane col=2 pos={p[2]}px bind:selected {site} width={w[2]}px {showAll} {w} {COLUMNS} />
{/if}


<style>
	.menu {
		width: 200px;
		margin-left:1px;
		margin-top:0px;
		margin-bottom:0px;

		padding-left:1px;
		padding-right:1px;
		padding-top:-1px;
		padding-bottom:1px;
	}

	:global(img) {
		width: 200px;
		display: block;
		margin-left: auto;
		margin-right: auto;
	}

	:global(table) {
		border-collapse: collapse;
		margin: 1px auto;
	}
	:global(table td) {padding: 1px}
	:global(table thead) {
		background-color: #000;
		color: #ff0;
		font-size: 13px;
		border: 1px solid #555;
	}
	:global(table tbody td) {border: 1px solid #555;}
	:global(table tbody tr) {background-color: #eee;}
	:global(table tbody tr:nth-child(odd)) {background-color: #fff;}

</style>