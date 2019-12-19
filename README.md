## Como contribuir?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/django-custom-manager-test.git
cd django-custom-manager-test
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

## Inserindo mais alguns dados

Abrir o `shell_plus`.

```
python manage.py shell_plus
```

Criar os dados:

```
from random import choice

companies = ['WTTD', 'Eventex']
[Company.objects.create(name=company) for company in companies]

# Inserindo metade dos usuários nas empresas
persons = Person.objects.all()[:16]
companies = Company.objects.all()
for person in persons:
    company = choice(companies)
    person.company = company
    person.save()
```

TODO

Testar o manager

