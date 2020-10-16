<!-- This is the header -->

<div class="flex justify-between items-center py-4 bg-blue-600">
  <div class="flex-shrink-0 ml-10 cursor-pointer">
    <i class="fas fa-drafting-compass fa-2x text-orange-500"></i>
    <span on:click={reset} class="ml-1 text-3xl text-white font-semibold">StudyFilter</span>
  </div>
</div>


<script>

function reset(){
    location.reload();
}
</script>