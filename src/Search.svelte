<script>
	export let sokruta
	export let text0
	export let text1
	export let stack
	export let WIDTH
	export let GAP
	export let spreadWidth
	export let _
	export let pop

	import { saveAs } from 'file-saver'

	function clear() {
		sokruta = ""
		document.getElementById("search").focus()
	}

	function share () {
		const q1 = stack.length <= 1 ? "" : "folder=" + stack.join("\\") 
		const q2 = sokruta == "" ? "" : "query=" + sokruta		
		const q = q1=="" && q2=="" ? "" : "?"
		const a = q1!="" && q2!="" ? "&" : ""
		navigator.clipboard.writeText(location.origin + location.pathname + q + q1 + a + q2)
	}

	function help() {
		window.open("https://github.com/ChristerNilsson/2022-015-WasaSK#readme")
	}

	window.onload = () => document.getElementById("search").focus()

</script>

<input autocomplete="off" id="search" bind:value={sokruta} placeholder='Search' style="width:{WIDTH-2*GAP-1}px">
<div class="center" style="width:{WIDTH}px">
		{text1}
</div>

<div style="width:{WIDTH}px; height:34px">

	{#if _.last(stack) == "Home"}
		<button style="left:{0*WIDTH/4}px; width:{spreadWidth(1/4,WIDTH)}px" on:click = {pop} disabled >Up</button>
	{:else}
		<button style="left:{0*WIDTH/4}px; width:{spreadWidth(1/4,WIDTH)}px" on:click = {pop} >Up</button>
	{/if}

	<button on:click={clear} style="left:{1*WIDTH/4}px; width:{spreadWidth(1/4,WIDTH)}px">Clear</button>
	<button on:click={share} style="left:{2*WIDTH/4}px; width:{spreadWidth(1/4,WIDTH)}px">Share</button>
	<button on:click={help}  style="left:{3*WIDTH/4}px; width:{spreadWidth(1/4,WIDTH)}px">Help</button>
</div>

{#if (sokruta.split(" ").length <= 3) && (sokruta.length > 0)}
	<div class="center" style="width:{WIDTH}px">
		{text0}
	</div>
{/if}

<style>
	.center {
		margin-top:7px;
		text-align:center;
		height:27px
	}
	div {
		margin:0px;
	}
	button {
		position:absolute;
		margin:2px;
		height:30px;
	}
	input {
		margin:0px;
		height:30px;
	}
	::placeholder {
		color: lightgray;
		opacity: 1;
	} 
</style>
