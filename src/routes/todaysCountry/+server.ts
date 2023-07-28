import type { RequestHandler } from './$types';
import countries from '$lib/server/country_data.json';
import random, { RNG } from 'random';
import seedrandom from 'seedrandom';
import { json } from '@sveltejs/kit';

export const GET = (() => {
	const today = new Date();
	const daysSinceEpoch = Math.floor(today.getTime() / (60 * 60 * 24));

	random.use(seedrandom(String(daysSinceEpoch)) as unknown as RNG);
	const country = random.choice(countries);

	return json(country);
}) satisfies RequestHandler;
