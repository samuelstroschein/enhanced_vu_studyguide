<script>
  import Button from "smelte/src/components/Button";
  import Example from "../components/example.svelte";
  var counter = 0;

  function increaseCounter() {
    counter += 1;
  }
</script>

<p class="text-2xl">{counter}</p>
<Example />
<Button on:click={increaseCounter}>increase counter</Button>
