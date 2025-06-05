---

#  Securin CPE Viewer

A Flask-based web application that visualizes Common Platform Enumeration (CPE) data from a MySQL database with pagination, search, and filtering features. Frontend built with Tailwind CSS.

---

##  Features

* Display a list of CPEs with pagination.
* Search by **CPE title**.
* Filter by **Deprecation Date** (partial or full match).
* REST API endpoints for both data retrieval and search.
* Responsive UI built using Tailwind CSS.

---

##  Project Structure

```
securin/
├── backend/
│   ├── main.py             # Flask app
│   ├── models.py           # SQLAlchemy model
│   ├── config.py           # DB configs
│   ├── template/
│   │   └── frontend.html   # Tailwind-based UI
└── README.md               # This file
```

---

## ⚙ Setup Instructions

### 1. Install Python dependencies

Make sure you're using Python 3.10+

```bash
pip install flask flask_sqlalchemy pymysql
```

### 2. Configure your database

Edit `config.py`:

```python
SQLALCHEMY_DATABASE_URI = 'mysql://root:yourpassword@localhost/securin'
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### 3. Run the Flask app

```bash
python main.py
```

The app will run at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

##  API Endpoints

###  Get All CPEs (Paginated)

```
GET /api/cpes?page=1&limit=10
```

**Query Parameters:**

* `page`: Page number (default: 1)
* `limit`: Number of results per page (default: 10)

**Example:**

```
http://127.0.0.1:5000/api/cpes?page=1&limit=10
```

---

###  Search CPEs

```
GET /api/search?page=1&limit=10&search=&deprecation=
```

**Query Parameters:**

* `search`: Text to match in the `cpe_title` field
* `deprecation`: Partial or full `cpe_23_deprecation_date` (e.g., `2023` or `2023-12-26`)
* `page` and `limit`: As above

**Example:**

```
http://127.0.0.1:5000/api/search?page=1&limit=10&search=oracle&deprecation=2023-12-26
```

---

##  Frontend

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the user interface.

**Functionality includes:**

* Searching CPEs by title
* Filtering by deprecation date
* Pagination controls

---

##  Sample `Securin` Table Schema

Make sure your table follows this schema:

```sql
CREATE TABLE securin (
  id INT AUTO_INCREMENT PRIMARY KEY,
  cpe_title TEXT,
  cpe_23_uri TEXT,
  reference_links TEXT,
  cpe_23_deprecation_date TEXT
);
```

---

## 🛠 Notes

* Ensure MySQL server is running and database `securin` exists.
* Your model class should include a `to_dict()` method for JSON responses:

```python
def to_dict(self):
    return {
        "id": self.id,
        "cpe_title": self.cpe_title,
        "cpe_23_uri": self.cpe_23_uri,
        "reference_links": self.reference_links,
        "cpe_23_deprecation_date": self.cpe_23_deprecation_date,
    }

# OUTPUT

![image](https://github.com/user-attachments/assets/9f9c557c-cf45-4b38-8708-fa7147ca62b9)

![image](https://github.com/user-attachments/assets/e26b6702-ad5d-4bd6-9c06-03990d178d35)

![image](https://github.com/user-attachments/assets/4bc90acb-95fd-4e6b-92e8-0f28ac98183b)

```


