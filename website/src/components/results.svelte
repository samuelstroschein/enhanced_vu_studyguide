<!-- <p>DEBUG: Here come the results</p> -->

<div class="border-b-2 border-gray-300">
<h5 class="flex justify-center" >Results</h5>
</div>

<Treeview items={$queryResponse} />

<script>
  import Treeview from "smelte/src/components/Treeview";
  import { queryResponse } from "../store.js";
</script>
