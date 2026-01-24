<div align="center">
<h1 align="center" style="border: none; margin: 10px; font-size: 3.5rem;">🍀Q U E S T I O N --V A U L T</h1>
  <br/>

  <p>
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
    <img src="https://img.shields.io/badge/SQL-CC2927?style=for-the-badge&logo=sqlite&logoColor=white" />
  </p>

  <p><b>A robust, server-side archive engineered to manage, query, and serve academic resources with precision.</b></p>

  ---
</div>

## 🛡️ The Architecture

The **Question Vault** is built on the philosophy of **Reliability** and **Schema Integrity**. Moving beyond simple file storage, this implementation uses a relational database to map subjects, years, and departments into a queryable academic network.

### ⚙️ Core Engine:
- **Django Framework:** Handling the heavy lifting of routing, authentication, and file serving.
- **Relational SQL:** A structured database designed for complex filtering (find any paper by subject code, semester, or year instantly).
- **Secure Storage:** Managed handling of academic PDFs and documents.

---

## 🚀 System Capabilities

<table border="0">
  <tr>
    <td width="50%">
      <img src="https://img.icons8.com/fluency/100/000000/database.png" width="45px" />
      <h3>Relational Mapping</h3>
      <p>Custom SQL models link question papers to specific MAKAUT regulations and curricula.</p>
    </td>
    <td width="50%">
      <img src="https://img.icons8.com/fluency/100/000000/api.png" width="45px" />
      <h3>Django REST Logic</h3>
      <p>Clean API endpoints providing structured JSON data for frontend consumers.</p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <img src="https://img.icons8.com/fluency/100/000000/admin-settings-male.png" width="45px" />
      <h3>Admin Control</h3>
      <p>Leveraging Django's powerful admin suite for effortless content moderation.</p>
    </td>
    <td width="50%">
      <img src="https://img.icons8.com/fluency/100/000000/search-database.png" width="45px" />
      <h3>Advanced Querying</h3>
      <p>Optimized SQL lookups to ensure the vault remains fast even as thousands of papers are added.</p>
    </td>
  </tr>
</table>

---

## 🛠️ Tech Stack

<div align="left">
  <img src="https://skillicons.dev/icons?i=py,django,postgres,sqlite,bash,docker,github,postman" />
</div>

---

## 📂 Project Blueprint

```text
question_vault/
├── 📁 core/               # Project Settings & Config
├── 📁 papers/             # Main App: Models, Views, Admin
│   ├── 📄 models.py       # SQL Schema Definition
│   ├── 📄 views.py        # Request Handling Logic
│   └── 📄 serializers.py  # Data Formatting
├── 📁 media/              # Stored PDFs & Assets
├── 📄 manage.py           # Django CLI
└── 📄 requirements.txt    # Python Dependencies
