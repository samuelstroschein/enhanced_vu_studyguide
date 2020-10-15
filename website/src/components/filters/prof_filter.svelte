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

  var items = [];

  let selectedItems = [];

  function toggle(i) {
    return v =>
      v.detail
        ? selectedItems.push(i)
        : (selectedItems = selectedItems.filter(si => si !== i));
  }

  $: selectedLabel = selectedItems.map(i => i.text).join(", ");

  const label = "Search professor...";
  onMount(async () => {
    fetchProf();
  });

  
  $:if($teacherFilter){console.log($teacherFilter)}
</script>