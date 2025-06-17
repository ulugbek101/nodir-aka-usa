# 🚀 Quick‑start (MacOD / Linux)


### 1. Create a local Python virtual environment called `.venv`
```bash
python3 -m venv .venv
```


### 2. Activate it
```bash
source .venv/bin/activate
```

### 3. Upgrade pip (optional but recommended)
```bash
python -m pip install --upgrade pip
```

### 4. Install project dependencies
```bash
pip install -r requirements.txt
```

### 5. Make and apply database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the development server
```bash
python manage.py runserver
```
