<h5 class="flex justify-center py-4">Period</h5>

<div class="flex justify-center">
  <label class="grid gap-4 grid-cols-4">
    <input
      class="form-radio h-5 w-8 text-blue-600"
      type="radio"
      bind:group={$periodFilter}
      value={"?Period = 'P1'@en"}
    />
    <span class="ml-2">{'P1'}</span>
    <input
      class="form-radio h-5 w-8 text-blue-600"
      type="radio"
      bind:group={$periodFilter}
      value={"?Period = 'P2'@en"}
    />
    <span class="ml-2">{'P2'}</span>
    <input
      class="form-radio h-5 w-8 text-blue-600"
      type="radio"
      bind:group={$periodFilter}
      value={"?Period = 'P3'@en"}
    />
    <span class="ml-2">{'P3'}</span>
    <input
      class="form-radio h-5 w-8 text-blue-600"
      type="radio"
      bind:group={$periodFilter}
      value={"?Period = 'P4'@en"}
    />
    <span class="ml-2">{'P4'}</span>
    <input
      class="form-radio h-5 w-8 text-blue-600"
      type="radio"
      bind:group={$periodFilter}
      value={"?Period = 'P5'@en"}
    />
    <span class="ml-2">{'P5'}</span>
    <input
      class="form-radio h-5 w-8 text-blue-600"
      type="radio"
      bind:group={$periodFilter}
      value={"?Period = 'P6'@en"}
    />
    <span class="ml-2">{'P6'}</span>
    <br />
  </label>
</div>

<script>
  import { periodFilter } from "../../store.js";
</script>
