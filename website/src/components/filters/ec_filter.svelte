<script>
  import RadioButtonGroup from "smelte/src/components/RadioButton";
//   https://smeltejs.com/components/selection-controls 
</script>

<h5>Number of Credits</h5>

<RadioButtonGroup
  name="Credits"
  color="blue" 
  items={[{ value: 3, label: '3 EC' }, { value: 6, label: '6 EC' }]} />