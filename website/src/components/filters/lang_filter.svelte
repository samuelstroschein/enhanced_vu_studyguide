<script>
  import { languageFilter } from '../../store.js';
</script>


<h5 class="flex justify-center">Language</h5>

<div class="flex justify-center">
  <label class="inline-flex items-center mt-3">
    <input class="form-radio h-5 w-8 text-blue-600" type=radio bind:group={$languageFilter} value={"?Language = 'Dutch'"}>
    <span class="ml-2">{"Dutch"}</span>
    <input class="form-radio h-5 w-8 text-blue-600" type=radio bind:group={$languageFilter} value={"?Language = 'English'"}>
    <span class="ml-2">{"English"}</span>
    <br>
  </label>
</div>