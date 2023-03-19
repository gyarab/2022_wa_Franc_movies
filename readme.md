# How to install

## Activate your python enviroment

```git bash
source ./venv/Scripts/activate
```

## install dependencies

```Bash
pip install -r requirements.txt
```

## Run local server

```Bash
python manage.py runserver
```

## Creating fixtures

```Bash
python manage.py dumpdata <app_model_name> --format yaml > fixtures/<name>.yaml
```
## Loading fixtures

```Bash
python manage.py loaddata fixtures/<name>.yaml --app <app_model_name>
```
