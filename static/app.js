const btn = document.getElementById("mode");

btn.onclick = () => {
  document.body.classList.toggle("light");
  btn.textContent =
    document.body.classList.contains("light") ? "☀️" : "🌙";
};