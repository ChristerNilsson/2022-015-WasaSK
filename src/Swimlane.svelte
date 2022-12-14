<script>
  import SvelteMarkdown from 'svelte-markdown'
	import _ from "lodash"
	export let col
	export let pos
	export let selected
	export let site
	export let width
	export let showAll
	export let w
	export let COLUMNS

	const THUMBNAIL_HEIGHT = 400 // px

	function click(key) {
		if (_.size(selected)==1) {
			selected = showAll()
		} else {
			selected = {}
			selected[key] = 0
		}
	}
	function noop(e) {}
	const style = _.size(selected) <= 1 ? "" : `width:${w[COLUMNS-1]}px;height:${THUMBNAIL_HEIGHT}px`
</script>

<div class="swimlane" style={"left:"+pos+";width:"+width}>
	{#each _.keys(selected) as key}
		{#if selected[key] == col}
			<div class="post" on:click={()=>click(key)} on:keydown={noop} {style}>
				<SvelteMarkdown source={site.md[key]} />
			</div>
		{/if}
	{/each}
</div>

<style>
	.swimlane {
		position: absolute;
		top: 0px;
		background: #FFC200;
	}

  .post {
		overflow:clip;

		margin-left:1px;
		margin-top:-10px;
		margin-bottom:0px;

		padding-left:1px;
		padding-right:1px;
		padding-top:-1px;
		padding-bottom:1px;

		background:white;
		overflow-wrap: break-word;

		-moz-border-radius: 5px;
		-webkit-border-radius: 5px;
		border-radius: 5px;
	}

</style>


