<script>
  import Treeview from "smelte/src/components/Treeview";
  import { queryResponse } from '../store.js';
</script>

<!-- <p>DEBUG: Here come the results</p> -->
<h5>Results:</h5>
<Treeview items={$queryResponse} />