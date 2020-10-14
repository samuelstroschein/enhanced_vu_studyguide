<script>
import Button from "smelte/src/components/Button";
import { queryResponse } from '../store.js';

async function SparQL(){
	
	var mySparqlEndpoint = "http://192.168.178.21:7200/repositories/FinalProject" ;
	var mySparqlQuery = `select DISTINCT * where { 
			?course teach:ects ?credit ;
         	vup:course_level ?level;
          	teach:academicTerm ?period;
           	teach:courseTitle ?title;
            teach:teacher ?teacher;
            dbo:language ?language;
            teach:grading ?grading;
            vup:course_content ?content;
            rdf:type teach:Course;
            vup:course_objective ?objective;
            vup:faculty ?faculty;
            vup:literature ?literature;
            vup:teaching_methods ?teachingMethod.
} LIMIT 10`;
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
		{ text:"grading: " + val.grading.value},
		{ text:"course content: " + val.content.value},
		{ text:"course objective: " + val.objective.value},
		{ text:"faculty: " + val.faculty.value},
		{ text:"literature: " + val.literature.value},
		{ text:"teaching methods: " + val.teachingMethod.value}
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