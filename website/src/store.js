import { writable } from 'svelte/store';

export const queryResponse = writable([]);
export const ecFilter = writable("?credits = '6'^^xsd:integer || ?credits = '3'^^xsd:integer");