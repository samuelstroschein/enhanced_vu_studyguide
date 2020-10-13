<script>
import Button from "smelte/src/components/Button";
import { queryResponse } from '../store.js';

async function SparQL(){
	
	var mySparqlEndpoint = "https://dbpedia.org/sparql" ;
	var mySparqlQuery = `SELECT ?label (MAX(?density) AS ?oneDensity)
		WHERE{
		  ?country rdf:type dbo:Country;
				   dbo:populationDensity ?density;
				   rdfs:label ?label.
				   FILTER (lang(?label) = 'en')
		} 
		ORDER BY DESC(?oneDensity)
		LIMIT 5
		`;
	var response = await fetch(mySparqlEndpoint + "?query=" + mySparqlQuery, {
	method: "GET",
	headers: {'Accept':'application/sparql-results+json', 'Content-Type':'application/sparql-results+json'}
	})
	var json = await response.json()
	$queryResponse = [];
	json.results.bindings.forEach(function(val){
		var parsedJson = {
		text: val.label.value,
		items: [
		{ text:"Credits: " + val.label.value},
		{ text:"Level: " + val.label.value},
		{ text:"Professor: " + val.label.value},
		{ text:"Language: " + val.label.value},
    		]
		  }
		$queryResponse = [...$queryResponse, parsedJson]
		// console.log(val.label.value)
		// console.log(val.oneDensity.value)
	});
}
</script>

<div class="flex justify-center">
    <Button color="blue" on:click = {SparQL}>Start Search</Button>
</div>