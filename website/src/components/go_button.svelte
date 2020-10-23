<div class="flex justify-center py-8">
  {#if loading}
    <svg xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.0" width="218px" height="20px" viewBox="0 0 512 47" xml:space="preserve"><g><circle fill="#1e88e5" cx="-14.781" cy="22.328" r="12.813"/><animateTransform attributeName="transform" type="translate" values="88 0;182 0;251 0;298 0;321 0;323.33 0;325.66 0;327.99 0;330.32 0;332.65 0;334.98 0;337.31 0;339.64 0;341.97 0;344.3 0;346.63 0;348.96 0;351.29 0;353.62 0;356 0;379 0;426 0;494 0;542 0;542 0;542 0;542 0;542 0;542 0;542 0;542 0;542 0;542 0;542 0;542 0;542 0;542 0;542 0" dur="2590ms" repeatCount="indefinite"/></g><g><circle fill="#1e88e5" cx="-50.328" cy="22.328" r="12.797"/><animateTransform attributeName="transform" type="translate" values="0 0;0 0;0 0;0 0;0 0;88 0;182 0;251 0;298 0;321 0;323.33 0;325.66 0;327.99 0;330.32 0;332.65 0;334.98 0;337.31 0;339.64 0;341.97 0;344.3 0;346.63 0;348.96 0;351.29 0;353.62 0;356 0;406 0;452 0;522 0;577 0;577 0;577 0;577 0;577 0;577 0;577 0;577 0;577 0;577 0" dur="2590ms" repeatCount="indefinite"/></g><g><circle fill="#1e88e5" cx="-87.203" cy="22.328" r="12.797"/><animateTransform attributeName="transform" type="translate" values="0 0;0 0;0 0;0 0;0 0;0 0;0 0;0 0;0 0;0 0;88 0;182 0;251 0;298 0;321 0;323.33 0;325.66 0;327.99 0;330.32 0;332.65 0;334.98 0;337.31 0;339.64 0;341.97 0;344.3 0;346.63 0;348.96 0;351.29 0;353.62 0;356 0;403 0;450 0;520 0;614 0;614 0;614 0;614 0;614 0;614 0" dur="2590ms" repeatCount="indefinite"/></g><g><circle fill="#1e88e5" cx="-125.234" cy="22.328" r="12.797"/><animateTransform attributeName="transform" type="translate" values="0 0;0 0;0 0;0 0;0 0;0 0;0 0;0 0;0 0;0 0;0 0;0 0;0 0;0 0;0 0;88 0;182 0;251 0;298 0;321 0;323.33 0;325.66 0;327.99 0;330.32 0;332.65 0;334.98 0;337.31 0;339.64 0;341.97 0;344.3 0;346.63 0;348.96 0;351.29 0;353.62 0;356 0;402 0;448 0;518 0;611 0" dur="2590ms" repeatCount="indefinite"/></g></svg>
  {:else}
    <div class="px-2">
      <Button color="blue" on:click={runSparQL}>Start Search</Button>
    </div>
    <div class="px-2">
      <Button color="blue" on:click={reset}>Reset</Button>
    </div>
  {/if}
</div>

<!-- DEBUG STATEMENTS BELOW -->

<!-- <h5>DEBUG INFO</h5>
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
</div> -->
<script>
  import Button from "smelte/src/components/Button";
  import { queryResponse } from "../store.js";
  import { ecFilter } from "../store.js";
  import { levelFilter } from "../store.js";
  import { periodFilter } from "../store.js";
  import { languageFilter } from "../store.js";
  import { teacherFilter } from "../store.js";

  let loading = false;


  async function runSparQL() {
    loading = true;
    var mySparqlEndpoint =
      "https://enhanced-vu-studyguide.vercel.app/api/sparql";
    if ($teacherFilter === "NoTeacher") {
      var mySparqlQuery = `select DISTINCT ?StudieGids_URL ?Credits ?Level ?Period ?Title ?Grading ?Content ?Objective ?Teaching_Method ?Literature ?Language ?Faculty where { 
          ?StudieGids_URL rdf:type vu:CourseCredits;
                      teach:ects ?Credits.
          ?StudieGids_URL rdf:type vu:CourseLevel;
                      vu:courseLevel ?Level.
          ?StudieGids_URL rdf:type vu:CoursePeriod;
                      teach:academicTerm ?Period.
          ?StudieGids_URL rdf:type teach:Course;
                      dbo:language ?LanguageName;
                      teach:courseTitle ?Title.
           OPTIONAL {
        	?StudieGids_URL teach:grading ?Grading;
            vu:courseContent ?Content;
            vu:courseObjective ?Objective;
            vu:offeredByFaculty ?FacultyName;
            vu:literature ?Literature;
            vu:teachingMethods ?Teaching_Method.
          ?FacultyName rdfs:label ?Faculty.
          ?LanguageName rdfs:label ?Language.
    		}   
	FILTER (${$ecFilter})
	FILTER (${$levelFilter})
	FILTER (${$periodFilter})
	FILTER (${$languageFilter})
}
LIMIT 800`;
    } else {
      var mySparqlQuery = `select DISTINCT ?StudieGids_URL ?Credits ?Level ?Period ?Title ?Grading ?Content ?Objective ?Teaching_Method ?Literature ?Language ?Faculty where { 
          ?StudieGids_URL rdf:type vu:CourseCredits;
                  teach:ects ?Credits.
          ?StudieGids_URL rdf:type vu:CourseLevel;
                  vu:courseLevel ?Level.
          ?StudieGids_URL rdf:type vu:CoursePeriod;
                      teach:academicTerm ?Period.
          ?StudieGids_URL rdf:type teach:Course;
                      dbo:language ?LanguageName;
                      teach:courseTitle ?Title;
                      vu:taughtBy ?TeacherName.
           OPTIONAL {
        	?StudieGids_URL teach:grading ?Grading;
            vu:courseContent ?Content;
            vu:courseObjective ?Objective;
            vu:offeredByFaculty ?FacultyName;
            vu:literature ?Literature;
            vu:teachingMethods ?Teaching_Method.
          ?FacultyName rdfs:label ?Faculty.
          ?LanguageName rdfs:label ?Language.
          ?TeacherName rdfs:label '${$teacherFilter}'@en.
    		}   
	FILTER (${$ecFilter})
	FILTER (${$levelFilter})
	FILTER (${$periodFilter})
	FILTER (${$languageFilter})
}`;

    }
    var response = await fetch(mySparqlEndpoint + "?query=" + mySparqlQuery, {
      method: "GET",
      headers: {
        Accept: "application/sparql-results+json",
        "Content-Type": "application/sparql-results+json",
      },
    });
    var json = await response.json();
    $queryResponse = [];
    if (json.results.bindings.length != 0) {
      await processResponse(json.results.bindings);
    } else {
      $queryResponse = [
        { text: "There were no results that matched your filter" },
      ];
    }
    loading = false;
  }

  async function processResponse(bindings) {
    bindings.forEach((course) => {
      var parsedJson = {
        text: course.Title.value,
        items: [],
      };
      for (var property in course) {
        if (property == "Title") continue;
        parsedJson.items.push({
          text: property + ": " + course[property].value,
        });
      }
      // console.log(parsedJson)
      $queryResponse = [...$queryResponse, parsedJson];
    });
  }

  function reset() {
    location.reload();
  }
</script>
