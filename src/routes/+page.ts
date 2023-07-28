import type { PageLoad } from './$types';

export const load = (async ({ fetch }) => {
	const res = await fetch(`/todaysCountry`);
	const country = await res.json();

	return { country };
}) satisfies PageLoad;
