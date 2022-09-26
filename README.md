# LITReview
LITReview is a web app where users can share and ask for reviews of books and articles.

---

## How to run LITReview
### Step 0: Get sources
```
git clone https://github.com/evrard1301/lit-review.git
cd lit-review
```

### Step 1: Create a virtual environment
```
python -m venv env
source env/bin/activate
```
### Step 2: Install dependencies
```
(env) pip install -r requirements.txt
```
### Step 3: Run all migrations
```
(env) cd litreview
(env) ./manage.py migrate
```

### Step 4: Run the server
```
(env) ./manage.py runserver
```

You can now access the web app from your browser at ``localhost:8000``.

## How to use LITReview

Four account already exists:

* The administrator (username **admin**, password **admin**)
* Three users:
  - alice (username **alice**, password **azerty2323**)
  - bob (username **bob**, password **azerty2323**)
  - claire (username **claire**, password **azerty2323**)
