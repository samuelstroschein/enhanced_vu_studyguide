<script>
import Button from "smelte/src/components/Button";
import { queryResponse } from '../store.js';
import { ecFilter } from '../store.js';

async function SparQL(){
	
	var mySparqlEndpoint = "https://enhanced-vu-studyguide.vercel.app/api/sparql" ;
	var mySparqlQuery = `select DISTINCT * { 
	?course rdf:type teach:Course;
         	teach:academicTerm ?period;
          	vu:courseLevel ?level;
        	teach:ects ?credits;
         	vu:taughtBy ?teacher;
          	dbo:language ?language;
           	teach:courseTitle ?title.
           OPTIONAL {
        	?course teach:grading ?grading;
            vu:courseContent ?content;
            vu:courseObjective ?objective;
            vu:offeredByFaculty ?faculty;
            vu:literature ?literature;
            vu:teachingMethods ?teachingMethod. 
       		?faculty rdfs:label ?facultylabel.       	
    }   	
    FILTER (${$ecFilter})
} LIMIT 10`;
	var response = await fetch(mySparqlEndpoint + "?query=" + mySparqlQuery, {
	method: "GET",
	headers: {'Accept':'application/sparql-results+json', 'Content-Type':'application/sparql-results+json'}
	})
	var json = await response.json()
	console.log(json)
	$queryResponse = [];
	json.results.bindings.forEach(function(val){
		var parsedJson = {
		text: val.title.value,
		items: [
		{ text:"Period: " + val.period.value},
		{ text:"Credits: " + val.credits.value},
		{ text:"Level: " + val.level.value},
		{ text:"Professor: " + val.teacher.value},
		{ text:"Language: " + val.language.value},
		{ text:"Grading: " + val.grading.value},
		{ text:"Course Content: " + val.content.value},
		{ text:"Course Objective: " + val.objective.value},
		{ text:"Faculty: " + val.facultylabel.value},
		{ text:"Literature: " + val.literature.value},
		{ text:"Teaching Methods: " + val.teachingMethod.value}
    		]
		  }
		$queryResponse = [...$queryResponse, parsedJson]
	});
}
</script>

<div class="flex justify-center">
    <Button color="blue" on:click = {SparQL}>Start Search</Button>
</div>