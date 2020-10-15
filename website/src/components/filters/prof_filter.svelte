<h5 class="flex justify-center">Select Professor</h5>
<Select color="blue" bind:value={items} on:change={$teacherFilter} outlined autocomplete {label} {items} />

<script>
  import Select from "smelte/src/components/Select";
  import { onMount } from "svelte";
  import { teacherFilter } from '../../store.js';

  async function fetchProf() {
    var mySparqlEndpoint =
      "https://enhanced-vu-studyguide.vercel.app/api/sparql";
    var mySparqlQuery = `select DISTINCT ?TeacherLabel { 
    ?Course vu:taughtBy ?Teacher.
    ?Teacher rdfs:label ?TeacherLabel.
}`;
    var response = await fetch(mySparqlEndpoint + "?query=" + mySparqlQuery, {
      method: "GET",
      headers: {
        Accept: "application/sparql-results+json",
        "Content-Type": "application/sparql-results+json"
      }
    });
    var json = await response.json();
    checkResponse(json.results.bindings);
  }

  function checkResponse(bindings) {
    var result = {};
    bindings.forEach(teacher => {
      var parsedJson = {
        text: teacher.TeacherLabel.value
      };
      if(parsedJson.text.length < 3) return
        // console.log(parsedJson);
        items = [...items, parsedJson];
    });
  }

  let showList = false;

  // var items = [];

  const label = "Search professor...";

  let value1 = "";
  let value2 = "";
  let value3 = "";
  let value4 = "";

  const items = [
    { value: 1, text: "One" },
    { value: 2, text: "Two" },
    { value: 3, text: "Three" },
    { value: 4, text: "Four" },
  ];
  onMount(async () => {
    // fetchProf();
  });


  $:if($teacherFilter){console.log($teacherFilter)}
</script>