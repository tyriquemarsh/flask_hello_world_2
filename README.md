### Install a virtual environment
# On Windows:
py -3 -m venv .venv

# On MacOs/Linux:
python3 –m venv .venv

### Activate the environment (every startup)
# On Windows:
.venv\Scripts\activate

# on MacOS/Linux:
. .venv/bin/activate

### With the virtual envirornment activated 

# Install Flask
pip install Flask

# Install all dependencies
pip install -r requirements.txt

## Run your Flask application

flask --app hello run --debug
