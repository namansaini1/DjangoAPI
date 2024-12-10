# Django Product Analytics Project

## Overview
This Django project provides a system for managing products, analyzing product data, and optimizing API performance. It includes three main tasks:

1. **Task 1:** Importing large datasets efficiently into the Product model.
2. **Task 2:** Providing an optimized API endpoint for data retrieval with filtering and aggregation.
3. **Task 3:** Enhancing performance using caching and indexing.

---

## Requirements
- Python 3.8+
- Django 4.2+
- A relational database (PostgreSQL is recommended for indexing capabilities).

---

## Setup Instructions

### 1. Clone the Repository
```bash
$ git clone <repository-url>
$ cd namanproject
```

### 2. Create a Virtual Environment
```bash
$ python -m venv env
$ source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
install Django framework 
```bash
pip install Django
install Request 
pip install requests
```
### 4. Set Up the Database
Update the database configuration in `settings.py` to use your database credentials. Example for PostgreSQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Run migrations:
```bash
$ python manage.py migrate
```

### 5. Load the Dataset
Download the dataset [here](https://drive.google.com/file/d/1OVonkcBUawYLzHoNEAZh4XQyGmdVHarR/view?usp=sharing) and save it in the root directory.

Run the custom Django management command to import the dataset:
Set path of large_dataset.csv  in import_products.py at defin handle in File path

---

## Tasks Implementation

### Task 1: Import Large Dataset
#### Features:
- **Efficient Processing:** Uses bulk inserts for importing large datasets into the `Product` model.
- **Validation:** Ensures `price` and `stock` fields are non-negative and handles invalid or missing data gracefully.

#### Command:
```bash
$ python manage.py import_dataset --file <path_to_csv>
```

---

### Task 2: Optimized API for Data Retrieval
#### API Endpoint:
`/api/products/analytics/`

#### Features:
1. **Filtering:**
   - Supports filtering by:
     - `category` (case-insensitive)
     - `min_price` and `max_price`
2. **Aggregation:**
   - Returns:
     - Total number of products
     - Average price of the filtered products
     - Total stock value (`stock * price`)

#### Example Request:
```http
GET /api/products/analytics/?category=electronics&min_price=10&max_price=100
```
#### Example Response:
```json
![image](https://github.com/user-attachments/assets/ae6793a9-3ff8-4dae-984d-ddd9ab3903b8)

```

---

### Task 3: Caching and Optimization
#### Features:
1. **Caching:**
   - Caches API results for 5 minutes.
   - Invalidates cache when query parameters change.
2. **Indexing:**
   - Adds database indexing on frequently queried fields (`category`, `price`).

---

## Testing
Run unit tests to verify functionality:
```bash
$ python manage.py test
```

---

## Performance Optimization
- **Bulk inserts** for dataset imports to handle large files efficiently.
- **Caching** for API responses to improve speed.
- **Database indexing** on `category` and `price` for faster query execution.

---

## Future Enhancements
- Add support for additional data analysis metrics.
- Implement a user-friendly front-end for product analytics.
- Extend API to support more query parameters.

---

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Open a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

