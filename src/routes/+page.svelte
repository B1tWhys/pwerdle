<script lang="ts">
	// import { hierarchy } from 'd3-hierarchy';
	import type { PageData } from './$types';

	export let data: PageData;
	const country = data.country;

	// hierarchy(country);
</script>

<main class="flex items-center justify-center flex-col">
	<h1 class="text-8xl">Pwerdle</h1>
	<h2>{country.title}</h2>
</main>
