<script>
  import Select from "smelte/src/components/Select";


  
  async function FetchProf(){
    
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
  
  let value1 = "";
  let value2 = "";
  let value3 = "";
  let value4 = "";

  let showList = false;

  const items = [
    { value: 1, text: "Daddy Bhulai" },
    { value: 2, text: "German Schlobach" },
    { value: 3, text: "Fraud Detected" },
    { value: 4, text: "Mister Pain" },
  ];

  let selectedItems = [];

  function toggle(i) {
    return v => v.detail
      ? selectedItems.push(i)
      : selectedItems = selectedItems.filter(si => si !== i);
  }

  $: selectedLabel = selectedItems.map(i => i.text).join(", ");

  const label = "Search professor...";
</script>

<h5 class="flex justify-center">Select Professor</h5>
<Select color= 'blue' bind:value={value3} outlined autocomplete {label} {items} />