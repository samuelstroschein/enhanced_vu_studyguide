<h5 class="flex justify-center py-4">Select Professor</h5>
<Select
  color="blue"
  outlined
  autocomplete
  bind:value={selected}
  on:change={handleChange}
  {label}
  {items}
/>

<script>
  import Select from "smelte/src/components/Select";
  import { onMount } from "svelte";
  import { teacherFilter } from "../../store.js";

  var selected = null;

  var items = [];

  const label = "Search professor...";

  function handleChange() {
    $teacherFilter = items[selected].text;
  }

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
    processResponse(json.results.bindings);
  }

  function processResponse(bindings) {
    var i = 0;
    bindings.forEach(teacher => {
      var parsedJson = {
        value: i,
        text: teacher.TeacherLabel.value
      };
      if (parsedJson.text.length < 3) return;
      // console.log(parsedJson);
      items = [...items, parsedJson];
      i += 1;
    });
  }

  onMount(async () => {
    fetchProf();
  });
</script>
