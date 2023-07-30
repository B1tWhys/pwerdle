import type { RequestHandler } from './$types';
import countries from '$lib/server/country_data.json';
import random, { RNG } from 'random';
import seedrandom from 'seedrandom';
import { json } from '@sveltejs/kit';

export const GET = (() => {
	const today = new Date();
	const daysSinceEpoch = Math.floor(today.getTime() / (60 * 60 * 24));
	const seed = String(daysSinceEpoch);
	console.debug(`Seeing rng with: ${seed}`);

	random.use(seedrandom(seed) as unknown as RNG);
	const country = random.choice(countries);

	return json(country);
}) satisfies RequestHandler;
