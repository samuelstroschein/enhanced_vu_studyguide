<script>
  import RadioButtonGroup from "smelte/src/components/RadioButton";
//   https://smeltejs.com/components/selection-controls 
</script>

<h5 class="flex justify-center">Number of Credits</h5>


<div class="flex justify-center">
    <RadioButtonGroup
    name="Credits"
    color="blue" 
    classes = "h-30 grid grid-rows-2 grid-flow-col-1 gap-0"
    items={[{ value: 3, label: '3 EC' }, { value: 6, label: '6 EC' }]} />
</div>