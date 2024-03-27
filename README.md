# animated-journey
Flask project for CONEL course

### Setup instructions
The following instructions are for the Linux terminal, changes are necessary for Windows.
- Clone the repository: `git clone https://github.com/mendelcyprys/animated-journey.git your_folder_name`
- Move into the directory: `cd your_folder_name`
- Setup a Python virtual environment: `python3 -m venv .venv`
- Activate virtual environment: `source .venv/bin/activate`
- Install requirements: `pip install -r requirements.txt`
- Create an `.env` file: `touch .env`
- Add this line to the `.env` file, you can choose your own filename: `DATABASE_URL="file:local.db"`
- Script to set up the tables in the database: `python scripts/schema.py`
- Script to add sample data to the database: `python scripts/sample.py`
- More to be here ...
- `flask --app main run`

### Log
- Created a .venv folder
- Installed Flask
- Made a requirements file
- Installed `libsql-client`, `python-dotenv`
- Will try to use `libsql-client` for the database connections
