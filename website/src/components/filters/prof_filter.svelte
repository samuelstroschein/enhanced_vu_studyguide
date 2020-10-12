<script>
  import Select from "smelte/src/components/Select";
  import Checkbox from "smelte/src/components/Checkbox";

  let value1 = "";
  let value2 = "";
  let value3 = "";
  let value4 = "";

  let showList = false;

  const items = [
    { value: 1, text: "Daddy Bhulai" },
    { value: 2, text: "German Schlobach" },
    { value: 3, text: "Fraud Detected" },
    { value: 4, text: "Mister Pain" },
  ];

  let selectedItems = [];

  function toggle(i) {
    return v => v.detail
      ? selectedItems.push(i)
      : selectedItems = selectedItems.filter(si => si !== i);
  }

  $: selectedLabel = selectedItems.map(i => i.text).join(", ");

  const label = "Professor Select";
</script>

<h5>Select Professor</h5>
<Select bind:value={value3} outlined autocomplete {label} {items} />