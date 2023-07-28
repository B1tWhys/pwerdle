<script lang="ts">
	import type { PageData } from './$types';
	export let data: PageData;
	const country = data.country;
</script>

<main class="flex items-center justify-center flex-col">
	<h1 class="text-8xl">Pwerdle</h1>
	<h2 class="">{country.title}</h2>
</main>
