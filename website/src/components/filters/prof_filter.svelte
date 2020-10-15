<h5 class="flex justify-center">Select Professor</h5>
<Select
  color="blue"
  outlined
  autocomplete
  bind:value={$teacherFilter}
  {label}
  {items}
/>

<script>
  import Select from "smelte/src/components/Select";
  import { onMount } from "svelte";
  import { teacherFilter } from "../../store.js";

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
        "Content-Type": "application/sparql-results+json",
      },
    });
    var json = await response.json();
    processResponse(json.results.bindings);
  }

  function processResponse(bindings) {
    var i = 0;
    bindings.forEach((teacher) => {
      var parsedJson = {
        value: i,
        text: teacher.TeacherLabel.value,
      };
      if (parsedJson.text.length < 3) return;
      // console.log(parsedJson);
      items = [...items, parsedJson];
      i += 1;
    });
  }

  var items = [];

  const label = "Search professor...";

  onMount(async () => {
    fetchProf();
  });
</script>
