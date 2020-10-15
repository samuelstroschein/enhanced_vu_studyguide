import { writable } from 'svelte/store';

export const queryResponse = writable([]);
export const ecFilter = writable("?Credits = '6'^^xsd:integer || ?Credits = '3'^^xsd:integer");
export const levelFilter = writable("?Level = '600'^^xsd:integer || ?Level = '500'^^xsd:integer || ?Level = '400'^^xsd:integer || ?Level = '300'^^xsd:integer || ?Level = '200'^^xsd:integer || ?Level = '100'^^xsd:integer");
export const periodFilter = writable("?Period = 'P1' || ?Period = 'P2' || ?Period = 'P3' || ?Period = 'P4' || ?Period = 'P5' || ?Period = 'P6'");
export const languageFilter = writable("INSERT QUERY");