<!-- <p>DEBUG: Here come the results</p> -->

<div class="border-b-2 border-gray-300">
<h5 class="flex justify-center font-semibold" >Results</h5>
</div>

<Treeview items={$queryResponse} />

<script>
  import Treeview from "../modifiedSmelte/Treeview";
  import { queryResponse } from "../store.js";
</script>
