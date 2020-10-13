<script>
import Button from "smelte/src/components/Button";


startMyAwesomeApp = function(){

	var myDisplayMessage = "Welcome to my awesome Web Application called: Info About Countries" ;
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

		$http( {
			method: "GET",
			url : mySparqlEndpoint + "?query=" + mySparqlQuery,
			headers : {'Accept':'application/sparql-results+json', 'Content-Type':'application/sparql-results+json'}
		} )
		.success(function(data, status ) {
			myDynamicLabels = [];
			myDynamicData = [];

			// now iterate on the results
			angular.forEach(data.results.bindings, function(val) {
				myDynamicLabels.push(val.teacher.value);
				myDynamicData.push(val.nbr_courses.value);
			});
		})
		.error(function(error ){
			console.log('Error running the input query!'+error);
		});

	};
// https://www.npmjs.com/package/sparql-http-client This is the package used for SPARQL
// Above code does return back shit from SPARQL, which is great but I can't get it to only run when clicking the Start Search Button. 
</script>

<div class="flex justify-center">
    <Button color="blue">Start Search</Button>
</div>