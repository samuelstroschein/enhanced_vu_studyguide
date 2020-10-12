<script>
  import Button from "smelte/src/components/Button";
  import Results from "../components/results.svelte";
  import Header from "../components/header.svelte";
  import Filters from "../components/filters.svelte";
  var counter = 0;

  function increaseCounter() {
    counter += 1;
  }
</script>



<div class="grid gap-4 grid-cols-10">
  <div class="col-span-10 ..."><Header /></div>
  <div class="col-span-2 ..."><Filters /></div>
  <div class="col-span-8 ..."><Results /></div>
</div>