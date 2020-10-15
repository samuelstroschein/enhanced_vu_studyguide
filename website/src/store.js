import { writable } from 'svelte/store';

export const queryResponse = writable([]);
export const ecFilter = writable("?credits = '6'^^xsd:integer || ?credits = '3'^^xsd:integer");
export const levelFilter = writable("?level = '600'^^xsd:integer || ?level = '500'^^xsd:integer || ?level = '400'^^xsd:integer || ?level = '300'^^xsd:integer || ?level = '200'^^xsd:integer || ?level = '500'^^xsd:integer");
export const periodFilter = writable("?period = 'P1' || ?period = 'P2' || ?period = 'P3' || ?period = 'P4' || ?period = 'P5' || ?period = 'P6'");