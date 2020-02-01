<template>
	<div id="right-sidebar">
		<h3>Quotes</h3>
		<div class="sidebar-section">
			<p class="sidebar">"Less mental clutter means more mental resources available for deep thinking."</p>
			<h6>-Cal Newport</h6>
		</div>
		<h3>Concepts</h3>
		<div>
			<p class="sidebar">"Attention residue is when thoughts about a task persist and intrude while performing another task"</p>
			<h6>-Sophie Leroy</h6>
		</div>

	</div>
</template>


<style>
  .sidebar {
    font-size: 1.1em;
  }

  .sidebar-section {
    margin: 0px 0px 30px 0px;
  }

 @media screen and (min-width: 0px) and (max-width: 800px) {
  #right-sidebar { display: none; }
}
</style>