function showSection(index) {
    document.querySelectorAll('.tab').forEach((t, i) => {
        t.classList.toggle('active', i === index)
    })
    document.querySelectorAll('.section').forEach((s, i) => {
        s.classList.toggle('active', i === index)
    })
}

function toggleTheme() {
    document.body.classList.toggle('dark')
}

// ==========================================================================================
const uploadBox = document.getElementById("uploadBox");
const fileInput = document.getElementById("pdfInput");

// click to browse
uploadBox.addEventListener("click", () => {
  fileInput.click();
});

// drag over
uploadBox.addEventListener("dragover", (e) => {
  e.preventDefault();
  uploadBox.classList.add("dragging");
});

// drag leave
uploadBox.addEventListener("dragleave", () => {
  uploadBox.classList.remove("dragging");
});

// drop file
uploadBox.addEventListener("drop", (e) => {
  e.preventDefault();
  uploadBox.classList.remove("dragging");

  fileInput.files = e.dataTransfer.files;
});

// ==========================================================================================
