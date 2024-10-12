## Setting up your repo

```
git clone <url_here>
Set-ExecutionPolicy Unrestricted -Scope CurrentUser
python3 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
flask run --reload
```

## Update dependencies (when new package is added)

```
pip freeze > requirements.txt
```
