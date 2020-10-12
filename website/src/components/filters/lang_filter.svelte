<script>
  import Select from "smelte/src/components/Select";
  import Checkbox from "smelte/src/components/Checkbox";

  let value1 = "";
  let value2 = "";
  let value3 = "";
  let value4 = "";

  let showList = false;

  const items = [
    { value: 1, text: "English" },
    { value: 2, text: "Zwahili" },
    { value: 3, text: "French" },
    { value: 4, text: "Dutch" },
  ];

  let selectedItems = [];

  function toggle(i) {
    return v => v.detail
      ? selectedItems.push(i)
      : selectedItems = selectedItems.filter(si => si !== i);
  }

  $: selectedLabel = selectedItems.map(i => i.text).join(", ");

  const label = "Language Select";
</script>

<h5>Select Language</h5>
<Select bind:value={value3} outlined autocomplete {label} {items} />