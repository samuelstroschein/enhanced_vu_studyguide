<script>
import Button from "smelte/src/components/Button";
import { queryResponse } from '../store.js';

async function SparQL(){
	
	var mySparqlEndpoint = "https://enhanced-vu-studyguide.vercel.app/api/sparql" ;
	var mySparqlQuery = `select DISTINCT * where { 
	?course teach:ects ?credits ;
         	vu:courseLevel ?level;
          	teach:academicTerm ?period;
           	teach:courseTitle ?title;
            vu:taughtBy ?teacher;
            dbo:language ?language;
            teach:grading ?grading;
            vu:courseContent ?content;
            rdf:type teach:Course;
            vu:courseObjective ?objective;
            vu:offeredByFaculty ?faculty;
            vu:literature ?literature;
            vu:teachingMethods ?teachingMethod.
} LIMIT 100`;
	var response = await fetch(mySparqlEndpoint + "?query=" + mySparqlQuery, {
	method: "GET",
	headers: {'Accept':'application/sparql-results+json', 'Content-Type':'application/sparql-results+json'}
	})
	var json = await response.json()
	$queryResponse = [];
	json.results.bindings.forEach(function(val){
		var parsedJson = {
		text: val.title.value,
		items: [
		{ text:"Credits: " + val.period.value},
		{ text:"Level: " + val.level.value},
		{ text:"Professor: " + val.teacher.value},
		{ text:"Language: " + val.language.value},
		{ text:"Grading: " + val.grading.value},
		{ text:"Course Content: " + val.content.value},
		{ text:"Course Objective: " + val.objective.value},
		{ text:"Faculty: " + val.faculty.value},
		{ text:"Literature: " + val.literature.value},
		{ text:"Teaching Methods: " + val.teachingMethod.value}
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