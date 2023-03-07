# Příkazy
Zadat django do requirements.txt

instalovat:
```Bash
pip install -r requirements.txt
```

Započetí projektu:
```Bash
django-admin startproject gamdb
```

A v adresáři názvu projektu spustíme server:
```Bash
python manage.py runserver
```

### Tvorba podprojetků
pak potřeba uvést ještě v settings.py jako installed_apps bez "django.contrib"
```Bash
django-admin startapp subapp1
```

### Generování databáze z models.py v podprojektu
```Bash
python manage.py makemigrations
python manage.py migrate
```

#### Co neverzovat v gitu?
``venv/
``*pye
``db.sqlite3

### Tvorba databází
Soubor models.py v adresáři projektu

### Něco dále (tvorba tabulek)
```Bash
python manage.py migrate
```