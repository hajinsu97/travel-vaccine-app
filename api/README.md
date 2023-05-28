# Travel-Vaccine-API

API for retrieving latest vaccine information for travel destinations provided by the CDC
<https://wwwnc.cdc.gov/travel/destinations/list>

## Local Development

Activate venv

```bash
# Create venv (for first time only)
python3 -m venv env
# Activate the venv
source env/bin/activate
# Install requirements
pip install -r requirements.txt
```

Start local server

```bash
python app.py
```

Navigate to the Flask UI
<http://127.0.0.1:8000/api/ui/>
