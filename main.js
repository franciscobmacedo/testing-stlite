const BASE_URL = "https://franciscobmacedo.github.io/testing-stlite";

function createAppList(arr) {
  const list = document.getElementById("apps-container");
  for (const entry of arr) {
    const item = document.createElement("li");
    const anchor = document.createElement("a");

    const scriptUrl = `${BASE_URL}/${entry.app}`;
    const packages = entry.requirements.join("&req=");
    let url = `https://share.stlite.net/#url=${scriptUrl}`;
    if (packages) {
      url = url + `&req=${packages}`;
    }
    anchor.href = url;
    anchor.textContent = entry.name;
    anchor.target = "_blank";
    item.appendChild(anchor);
    list.appendChild(item);
  }
  return list;
}
fetch("manifest.json")
  .then((response) => response.json())
  .then((json) => createAppList(json));
