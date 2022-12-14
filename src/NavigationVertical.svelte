<script>
	import _ from "lodash"
	export let keys
	export let push
	export let WIDTH
		
</script>

<div style="width:{WIDTH}px">

	{#each keys as key }
		<div>
			<span>
				<button class="row" value={key} on:click = {() => push(key)}>{key}</button>
			</span>
		</div>
	{/each}
</div>

<style>
	span {
		flex:1;
		overflow:hidden;
		white-space:nowrap;
	}
	div {
		margin:0px
	}
	.header {
		margin:0.5px;
		height:30px;
	}
	.row {
		margin:0px;
		height:30px;
		width:98%;
		text-align:left;
		flex:1;
		overflow:hidden;
		white-space:nowrap;
	}

</style>
