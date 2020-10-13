<script>
  import Results from "../components/results.svelte";
  import Header from "../components/header.svelte";
  import Filters from "../components/filters.svelte";
  import GoButton from "../components/go_button.svelte";
</script>

<div class="grid gap-4 grid-cols-10">
  <div class="col-span-10 ..."><Header /></div>
  <div class="col-span-2 ..."><Filters /></div>
  <div class="col-span-8 ..."><Results /></div>
  <div class="col-span-2 ..."><GoButton /></div>
</div>