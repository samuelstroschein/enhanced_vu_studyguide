<script>
  import Button from "smelte/src/components/Button";
  import Results from "../components/results.svelte";
  import Header from "../components/header.svelte";
  import Filter from "../components/filter.svelte";
  var counter = 0;

  function increaseCounter() {
    counter += 1;
  }
</script>
<div><Header /></div>
<div class="grid gap-4 grid-cols-2">
  <div><Filter /></div>
  <div><Results /></div>
</div>