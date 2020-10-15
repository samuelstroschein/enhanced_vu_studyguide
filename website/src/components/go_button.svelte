<script>
import Button from "smelte/src/components/Button";
import { queryResponse } from '../store.js';
import { ecFilter } from '../store.js';
import { levelFilter } from '../store.js';
import { periodFilter } from '../store.js';
import { languageFilter } from '../store.js';

async function SparQL(){
	
	var mySparqlEndpoint = "https://enhanced-vu-studyguide.vercel.app/api/sparql" ;
	var mySparqlQuery = `select DISTINCT * { 
	?Course rdf:type teach:Course;
         	teach:academicTerm ?Period;
          	vu:courseLevel ?Level;
        	teach:ects ?Credits;
         	vu:taughtBy ?Teacher;
          	dbo:language ?Language;
           	teach:courseTitle ?Title.
           OPTIONAL {
        	?Course teach:grading ?Grading;
            vu:courseContent ?Content;
            vu:courseObjective ?Objective;
            vu:offeredByFaculty ?FacultyName;
            vu:literature ?Literature;
            vu:teachingMethods ?Teaching_Method.
       		?FacultyName rdfs:label ?Faculty.
    }   	
	FILTER (${$ecFilter})
	FILTER (${$levelFilter})
	FILTER (${$periodFilter})
}LIMIT 100`;
	var response = await fetch(mySparqlEndpoint + "?query=" + mySparqlQuery, {
	method: "GET",
	headers: {'Accept':'application/sparql-results+json', 'Content-Type':'application/sparql-results+json'}
	})
	var json = await response.json()
	$queryResponse = [];
	checkResponse(json.results.bindings)
}

	function checkResponse(bindings){
		var result = {}
		bindings.forEach(course => {
			var parsedJson = {
				text: course.Title.value,
				items: []
			}
			for (var property in course){
				if (property == "Title") continue
				parsedJson.items.push({ text: property + ": " + course[property].value})
			}
			// console.log(parsedJson)
			$queryResponse = [...$queryResponse, parsedJson]
		});
	}
</script>

<div class="flex justify-center">
    <Button color="blue" on:click = {SparQL}>Start Search</Button>
</div>

<!-- DEBUG STATEMENTS BELOW -->

<h5>DEBUG INFO</h5>
<div>
<p>DEBUG LEVEL: {$levelFilter}</p>
</div>

<div>
<p>DEBUG CREDITS: {$ecFilter}</p>
</div>

<div>
<p>DEBUG Period: {$periodFilter}</p>
</div>

<div>
<p>DEBUG Language: {$languageFilter}</p>
</div>
