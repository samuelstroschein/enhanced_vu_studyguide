<h5 class="flex justify-center py-4">Credits</h5>

<div class="flex justify-center">
  <label class="inline-flex items-center mt-3">
    <input
      class="form-radio h-5 w-8 text-blue-600"
      type="radio"
      bind:group={$ecFilter}
      value={"?Credits = '3'^^xsd:integer"}
    />
    <span class="ml-2">{'3EC'}</span>
    <input
      class="form-radio h-5 w-8 text-blue-600"
      type="radio"
      bind:group={$ecFilter}
      value={"?Credits = '6'^^xsd:integer"}
    />
    <span class="ml-2">{'6EC'}</span>
    <br />
  </label>
</div>

<script>
  import { ecFilter } from "../../store.js";
</script>
