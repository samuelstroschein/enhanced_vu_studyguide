<Header class="mb-20" />
<div class="grid gap-4 grid-cols-10 flex justify-center">
  <div
    class="col-span-3 bg-white-500 text-gray font-bold py-4 px-2 border-4
    border-grey-400 rounded"
  >
    <div>
      <GoButton />
    </div>
    <div>
      <Filters />
    </div>
  </div >
  <div class="col-span-7 bg-white-500 text-gray font-bold py-4 px-2 border-4
    border-grey-400 rounded">
    <Results />
  </div>
  <div class="col-span-10">
    <Explanation />
  </div>
</div>

<script>
  import Results from "../components/results.svelte";
  import Header from "../components/header.svelte";
  import Filters from "../components/filters.svelte";
  import GoButton from "../components/go_button.svelte";
  import Explanation from "../components/explanation.svelte"
</script>
