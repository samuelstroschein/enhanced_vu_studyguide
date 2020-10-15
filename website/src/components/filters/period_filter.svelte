 <script>
  import { periodFilter } from '../../store.js';
</script>


<h5 class="flex justify-center">Period</h5>

<div class="flex justify-center">
  <label class="grid gap-4 grid-cols-4">
    <input class="form-radio h-5 w-8 text-blue-600" type=radio bind:group={$periodFilter} value={"?period = 'P1'"}>
    <span class="ml-2">{"P1"}</span>
    <input class="form-radio h-5 w-8 text-blue-600" type=radio bind:group={$periodFilter} value={"?period = 'P2'"}>
    <span class="ml-2">{"P2"}</span>
    <input class="form-radio h-5 w-8 text-blue-600" type=radio bind:group={$periodFilter} value={"?period = 'P3'"}>
    <span class="ml-2">{"P3"}</span>
    <input class="form-radio h-5 w-8 text-blue-600" type=radio bind:group={$periodFilter} value={"?period = 'P4'"}>
    <span class="ml-2">{"P4"}</span>
    <input class="form-radio h-5 w-8 text-blue-600" type=radio bind:group={$periodFilter} value={"?period = 'P5'"}>
    <span class="ml-2">{"P5"}</span>
    <input class="form-radio h-5 w-8 text-blue-600" type=radio bind:group={$periodFilter} value={"?period = 'P6'"}>
    <span class="ml-2">{"P6"}</span>
    <br>
  </label>
</div>