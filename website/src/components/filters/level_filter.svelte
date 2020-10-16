<h5 class="flex justify-center py-4">Level</h5>

<div class="flex justify-center">
  <label class="grid gap-4 grid-cols-4">
    <input
      class="form-radio h-5 w-8 text-blue-600"
      type="radio"
      bind:group={$levelFilter}
      value={"?Level = '100'^^xsd:integer"}
    />
    <span class="ml-2">{'100'}</span>
    <input
      class="form-radio h-5 w-8 text-blue-600"
      type="radio"
      bind:group={$levelFilter}
      value={"?Level = '200'^^xsd:integer"}
    />
    <span class="ml-2">{'200'}</span>
    <input
      class="form-radio h-5 w-8 text-blue-600"
      type="radio"
      bind:group={$levelFilter}
      value={"?Level = '300'^^xsd:integer"}
    />
    <span class="ml-2">{'300'}</span>
    <input
      class="form-radio h-5 w-8 text-blue-600"
      type="radio"
      bind:group={$levelFilter}
      value={"?Level = '400'^^xsd:integer"}
    />
    <span class="ml-2">{'400'}</span>
    <input
      class="form-radio h-5 w-8 text-blue-600"
      type="radio"
      bind:group={$levelFilter}
      value={"?Level = '500'^^xsd:integer"}
    />
    <span class="ml-2">{'500'}</span>
    <input
      class="form-radio h-5 w-8 text-blue-600"
      type="radio"
      bind:group={$levelFilter}
      value={"?Level = '600'^^xsd:integer"}
    />
    <span class="ml-2">{'600'}</span>
    <br />
  </label>
</div>

<script>
  import { levelFilter } from "../../store.js";
</script>
