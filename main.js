function createAppList(arr) {
  const list = document.getElementById("apps-container");
  for (const entry of arr) {
    const item = document.createElement("li");
    const anchor = document.createElement("a");
    const appName = entry.app.replace(/^.*[\\\/]/, "");
    const scriptUrl = encodeURIComponent(entry.app);
    const packages = entry.requirements.join("&req=");
    const url = `https://share.stlite.net/#url=${scriptUrl}?req=${packages}`;
    anchor.href = url;
    anchor.textContent = appName;
    anchor.target = "_blank";
    item.appendChild(anchor);
    list.appendChild(item);
  }
  return list;
}
fetch("manifest.json")
  .then((response) => response.json())
  .then((json) => createAppList(json));