<!-- <script>
  import RadioButtonGroup from "smelte/src/components/RadioButton";
//   https://smeltejs.com/components/selection-controls 
  let value = "";
</script>

<h5 class="flex justify-center">Number of Credits</h5>


<div class="flex justify-center">
    <RadioButtonGroup bind:group={value} value
    name="Credits"
    color="blue" 
    classes = "h-30 grid grid-rows-2 grid-flow-col-1 gap-0"
    items={[{value: 3, label: '3 EC' }, { value: 6, label: '6 EC' }]}/>
</div>

<p>Value: {value}</p> 

THIS IS ORIGINAL OLD CODE THAT MAKES USE OF THE SMELTE FRAMEWORK, COULD NOT GET FETCHING THE VALUES FROM IT WORK SO RESORTED TO THE ORIGINAL WAY OF BUTTONS
-->

<script>
 import { ecFilter } from '../../store.js';
</script>


<h5 class="flex justify-center">Credits</h5>

<div class="flex justify-center">
  <label class="inline-flex items-center mt-3">
    <input class="form-radio h-5 w-8 text-blue-600" type=radio bind:group={$ecFilter} value={"?credits = '3'^^xsd:integer"}>
    <span class="ml-2">{"3EC"}</span>
    <input class="form-radio h-5 w-8 text-blue-600" type=radio bind:group={$ecFilter} value={"?credits = '6'^^xsd:integer"}>
    <span class="ml-2">{"6EC"}</span>
    <br>
  </label>
</div>


<p>DEBUG:{$ecFilter}</p>
