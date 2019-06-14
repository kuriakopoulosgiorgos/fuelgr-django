Το Project αφορά εργασία εξαμήνου στο μάθημα "ΕΙΔΙΚΑ ΘΕΜΑΤΑ ΠΑΓΚΟΣΜΙΟΥ ΙΣΤΟΥ" του καθηγητή Φώτη Κόκκορα


# ![Logo](https://fuelgr.gr/web/img/app_logo/fuelGR-map.png) Fuelgr-django


Το project κάνει χρήση των εννοιών που διδάχτηκαν στο μάθημα και του python framework το django

## Quickstart

**1. Clone the repository:**

```
$ git clone https://github.com/kuriakopoulosgiorgos/fuelgr-django.git
```

**2. create a new virtual environment:**

**3. Install dependencies:**

In the project root directory run:

```
(venv) $ pip install -r requirments.txt
```

**4. Create a new MySQL Schema name it as fuelgr-django or modify settings.py (currently configured for xampp) and query files accordingly:**

```
From the database folder run sql queries in this order
  1) db-tables.sql
  2) users.sql
  3) gasstations.sql
  4) pricedata.sql
```

**5. Migrate to MySQL:**

```
$ python manage.py migrate
```

**6. Run the server:**

```
$ python manage.py runserver
```


All done. The server is up and running!
