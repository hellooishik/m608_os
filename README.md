

```md
# 📌 M608 REST API Backend Application  
**Flask + MongoDB + JWT Authentication | Secure CRUD API**

---

## 📝 Project Overview  

This project is developed as part of **Module M608 (Advanced Software Development)** and demonstrates the design, development, and testing of a secure REST API system using **Flask (Python)** with **MongoDB** as the database and **JWT authentication** for secure access.  

The application follows modular architecture, handles CRUD operations for **Customers, Products, and Orders**, ensures security implementation, and meets academic assessment criteria.  

---

## 🚀 Features

- Secure REST API built using **Flask**
- **JWT authentication** (register + login + token-based request handling)
- **MongoDB + MongoEngine ODM** for scalable data storage
- **CRUD operations** for:
  - Customers  
  - Products  
  - Orders  
- Pagination enabled on listing APIs
- Clean modular folder structure
- Fully testable using Postman / Thunder Client
- Ready for deployment or Dockerization

---

## 🧱 Tech Stack

| Category | Technology |
|----------|-------------|
| Language | Python 3 |
| Framework | Flask |
| Database | MongoDB Community |
| ODM | MongoEngine |
| Authentication | JWT (Flask-JWT-Extended) |
| Tools | pip, virtual environment |
| Recommended Tester | Postman / ThunderClient |
| IDE Used | VS Code |
| OS | macOS / Windows / Linux |

---

## 📁 Folder Structure

```

m608_rest_api/
├─ app/
│  ├─ **init**.py
│  ├─ config.py
│  ├─ models.py
│  ├─ schemas.py
│  ├─ auth.py
│  ├─ routes.py
│  ├─ utils.py
│  └─ seed.py
├─ sample_data/
│  └─ seed_data.json
├─ tests/
│  └─ test_api.py
├─ .env  (optional for secrets)
├─ requirements.txt
├─ run.py
└─ README.md

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone or open project folder
```bash
cd m608_rest_api
````

### 2️⃣ Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate     # macOS/Linux
# .venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4️⃣ Install & Start MongoDB

#### macOS (Homebrew)

```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community
```

#### Windows

Download & install from official MongoDB website:
[https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)

### 5️⃣ Run the server

```bash
python run.py
```

### Default Local URL

```
http://127.0.0.1:3000
```

---

## 🔐 Authentication Details

This API uses **JWT Bearer Token Authentication**.
To access protected endpoints:

**Step 1 — Register** → **Step 2 — Login** → **Step 3 — Copy token** → **Step 4 — Use in headers**

Add header to all protected API calls:

```
Authorization: Bearer <your_token_here>
```

---

## 🔗 API Endpoints

### 🔸 Auth API

| Method | Endpoint             | Description           |
| ------ | -------------------- | --------------------- |
| POST   | `/api/auth/register` | Register new user     |
| POST   | `/api/auth/login`    | Login & get JWT token |

---

### 👥 Customer API

| Method | Endpoint                            | Auth | Description                 |
| ------ | ----------------------------------- | ---- | --------------------------- |
| POST   | `/api/customers`                    | ✔    | Add new customer            |
| GET    | `/api/customers?page=1&per_page=10` | ✔    | Get paginated customer list |

---

### 📦 Product API

| Method | Endpoint                           | Auth | Description      |
| ------ | ---------------------------------- | ---- | ---------------- |
| POST   | `/api/products`                    | ✔    | Add product      |
| GET    | `/api/products?page=1&per_page=10` | ✔    | Get product list |

---

### 🛍 Order API

| Method | Endpoint                         | Auth | Description      |
| ------ | -------------------------------- | ---- | ---------------- |
| POST   | `/api/orders`                    | ✔    | Create new order |
| GET    | `/api/orders?page=1&per_page=10` | ✔    | Get orders list  |

---

## 🧪 Example JSON Requests

### 🔸 Register User

```json
{
  "username": "admin",
  "password": "admin123"
}
```

### 🔸 Add Customer

```json
{
  "name": "Apple Inc",
  "email": "support@apple.com",
  "phone": "999888777"
}
```

### 🔸 Add Product

```json
{
  "name": "iPhone 15",
  "sku": "IP15",
  "price": 1299.99,
  "stock": 25
}
```

### 🔸 Create Order

```json
{
  "customer": "<customer_id>",
  "total": 2599.00
}
```

---

## 📊 Pagination Format

Apply to customers, products, and orders:

```
?page=1&per_page=10
```

---

## 🧪 Testing Tools

| Tool                     | Purpose             |
| ------------------------ | ------------------- |
| Postman                  | Best for API Test   |
| Thunder Client (VS Code) | Lightweight testing |
| MongoDB Compass          | GUI DB viewer       |

---

## 📌 Next Possible Enhancements

| Feature                     | Status   |
| --------------------------- | -------- |
| PUT & DELETE endpoints      | Pending  |
| Swagger API documentation   | Optional |
| Docker & CI/CD pipeline     | Optional |
| Deployment on AWS / Railway | Optional |
| Role-based access levels    | Optional |

---

## 🙋 Contact & Support

If you require improvements, deployment, diagrams, documentation or demo video support — feel free to request.

---

### 📍 End of README

```
END OF FILE
```

---


