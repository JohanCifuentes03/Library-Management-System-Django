

# 📚 Library Management System - Django

A simple and functional **Library Management System** built with Django, providing core operations to manage books, members, lending, and fines.

---

## ✅ Features

This system supports full **CRUD** (Create, Read, Update, Delete) operations for:

- 👤 **Members Management**: Add, view, edit, and delete library members.
- 📘 **Books Management**: Track and manage the book catalog.
- 🔄 **Book Lending**: Assign books to members.
- 🔁 **Book Return**: Process returns and check overdue status.
- 💵 **Borrowing Payment**: Track payments for borrowed books.
- 💳 **Fine Payment**: Manage fines for late returns.

---

## 🚀 Getting Started (Local Setup)

### 1. Clone the Repository

```bash
git clone https://github.com/hellen-22/Library-Management-System-Django.git
cd Library-Management-System-Django
````

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv  # or python -m venv venv
```

* **On Windows:**

  ```bash
  venv\Scripts\activate
  ```

* **On macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the `.env.sample` file and configure your environment:

```bash
cp .env.sample .env
```

Edit `.env` to match your local setup.

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit: [http://localhost:8000](http://localhost:8000)

---

## 🐳 Running with Docker (Optional)

To run the project using Docker and Docker Compose (or Podman Compose):

```bash
podman compose build
podman compose up
```

Ensure your `.env` file is correctly configured before running Docker.

---

## 🌐 Live Demo

Hosted on **Render**:
🔗 [https://library-wnd0.onrender.com/](https://library-wnd0.onrender.com/)

### Demo Credentials

```text
Email: admin@gmail.com
Password: Admin@LMS
```

Or you can register a new account.

---

## 🖼️ Screenshots

### 🔐 Login & Register

<img width="1440" src="https://github.com/hellen-22/Library-Management-System-Django/assets/58620060/5843a91c-c721-4a6d-bbbc-761c0ff6a713">
<img width="1439" src="https://github.com/hellen-22/Library-Management-System-Django/assets/58620060/8ea7d534-8371-4e4c-afa1-1e62e4bd64f9">

### 🏠 Dashboard

<img width="1426" src="https://github.com/hellen-22/Library-Management-System-Django/assets/58620060/db263fab-8589-474f-8b09-fb781fcd466c">

### 👥 Members

<img width="1440" src="https://github.com/hellen-22/Library-Management-System-Django/assets/58620060/ffb20c12-8a48-46a5-88a4-64744e40cd40">
<img width="1424" src="https://github.com/hellen-22/Library-Management-System-Django/assets/58620060/26abb84b-0a3f-4e27-872f-b9a58e36f597">

### 📚 Books

<img width="1424" src="https://github.com/hellen-22/Library-Management-System-Django/assets/58620060/7e18dd67-229f-4456-8278-f1252d66d387">
<img width="1423" src="https://github.com/hellen-22/Library-Management-System-Django/assets/58620060/74461a23-b1b9-4af8-a924-2d7312e4762f">

### 📄 Other Pages

<img width="1439" src="https://github.com/hellen-22/Library-Management-System-Django/assets/58620060/99f3dfc9-4136-4187-aa51-933a97ef161e">
<img width="1423" src="https://github.com/hellen-22/Library-Management-System-Django/assets/58620060/643579b1-7811-44c4-a07a-03b5196ccbe5">
<img width="1425" src="https://github.com/hellen-22/Library-Management-System-Django/assets/58620060/91cc7d5c-a15c-4755-ad1b-b112fd098420">

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---