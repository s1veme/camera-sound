<template>
  <router-view />
</template>
<style>
*,
*::after,
*::before {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body {
  background-color: rgb(31, 31, 31);
  font-family: "JetBrains Mono", monospace;
  font-size: 16px;
  color: #fff;
}
a {
  text-decoration: none;
}
.container {
  max-width: 1340px;
  margin: 0 auto;
  padding: 15px;
}
.button {
  background-color: #08092a;
  color: #dcdcdc;
  border: 0;
  padding: 10px 18px;
  font-size: 18px;
  border-radius: 8px;
  margin: 1rem 1rem;
}
input[type="file" i]::-webkit-file-upload-button {
  background: none;
  color: #fff;
  padding: 10px 18px;
  border: 0;
}
input[type="file" i] {
  cursor: default;
  color: inherit;
  white-space: pre;
  text-align: start !important;
}

</style>