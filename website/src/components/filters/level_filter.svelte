<script>
  import RadioButtonGroup from "smelte/src/components/RadioButton";
  //   https://smeltejs.com/components/selection-controls 
</script>

<h5>Level</h5>

<RadioButtonGroup
  name="Credits"
  color="blue"
  items={[{ value: 100, label: '100' }, { value: 200, label: '200' }, { value: 300, label: '300' },{ value: 400, label: '400' }, { value: 500, label: '500' }, { value: 600, label: '600' }]} />