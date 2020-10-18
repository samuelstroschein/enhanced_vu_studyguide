import { writable } from 'svelte/store';

export const queryResponse = writable([]);
export const ecFilter = writable("?Credits = '6'^^xsd:integer || ?Credits = '3'^^xsd:integer");
export const levelFilter = writable("?Level = '600'^^xsd:integer || ?Level = '500'^^xsd:integer || ?Level = '400'^^xsd:integer || ?Level = '300'^^xsd:integer || ?Level = '200'^^xsd:integer || ?Level = '100'^^xsd:integer");
export const periodFilter = writable("?Period = 'P1'@en || ?Period = 'P2'@en || ?Period = 'P3'@en || ?Period = 'P4'@en || ?Period = 'P5'@en || ?Period = 'P6'@en");
export const languageFilter = writable("?Language = 'Dutch'@en || ?Language = 'English'@en");
export const teacherFilter = writable("NoTeacher");