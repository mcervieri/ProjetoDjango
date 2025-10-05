document.addEventListener("DOMContentLoaded", () => {
  const sidebar = document.querySelector("aside");
  const toggle = document.createElement("button");
  toggle.innerText = "☰";
  toggle.className = "md:hidden fixed top-4 left-4 bg-gray-800 text-white p-2 rounded";
  document.body.appendChild(toggle);

  toggle.addEventListener("click", () => {
    sidebar.classList.toggle("hidden");
  });
});
