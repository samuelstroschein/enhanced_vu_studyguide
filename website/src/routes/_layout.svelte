<svelte:head>
  <title>{name ? name : ''}</title>
</svelte:head>

<main class="mx-auto px-8 max-w-6xl">
  <slot />
</main>

<script>
  import "smelte/src/tailwind.css";
  import { stores } from "@sapper/app";
  import AppBar from "smelte/src/components/AppBar";
  import Button from "smelte/src/components/Button";
  import ProgressLinear from "smelte/src/components/ProgressLinear";
  import Tabs from "smelte/src/components/Tabs";
  import Tooltip from "smelte/src/components/Tooltip";
  import { Spacer } from "smelte/src/components/Util";
  import dark from "../utils/dark.js";
  const { preloading, page } = stores();
  $: path = $page.path;
  export let segment = "";
  $: n = (segment || "").replace(new RegExp("-", "g"), " ");
  $: name = n.length ? n.charAt(0).toUpperCase() + n.slice(1) : "";

  const darkMode = dark();
  const topMenu = [
    { to: "/", text: "Home" },
    { to: "/about", text: "About" },
    { to: "/blog", text: "Blog" },
  ];
</script>
