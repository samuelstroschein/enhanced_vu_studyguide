<script>
  import RadioButtonGroup from "smelte/src/components/RadioButton";
  //   https://smeltejs.com/components/selection-controls 
</script>

<h5 class="flex justify-center">Level</h5>

<div class="flex justify-center">
<RadioButtonGroup
  name="Credits"
  color="blue"
  classes = "h-30 w-40 grid grid-rows-3 grid-flow-col gap-0"
  items={[{ value: 100, label: '100' }, { value: 200, label: '200' }, { value: 300, label: '300' },{ value: 400, label: '400' }, { value: 500, label: '500' }, { value: 600, label: '600' }]} />
</div>