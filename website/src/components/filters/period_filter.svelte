<script>
  import RadioButtonGroup from "smelte/src/components/RadioButton";
//   https://smeltejs.com/components/selection-controls 
</script>

<h5 class="flex justify-center">Period</h5>

<div class="flex justify-center">
<RadioButtonGroup
  name="Credits"
  color="blue" 
  classes = "h-30 w-40 grid grid-rows-3 grid-flow-col gap-0"
  items={[{ value: 1, label: 'P1' }, { value: 2, label: 'P2' }, { value: 3, label: 'P3' },{ value: 4, label: 'P4' },{ value: 5, label: 'P5' }, { value: 6, label: 'P6' }]} />
 </div> 