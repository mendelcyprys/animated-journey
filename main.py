import libsql_client
from dotenv import dotenv_values

config = dotenv_values(".env")

DATABASE_URL = config["DATABASE_URL"]

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello world!</p><ul><li><a href='patients'>Patients</a></li></ul>"


@app.route("/patients")
def patients():
    table_head = """<tr>
        <th style="width:10%;text-align:left;">Firstname</th>
        <th style="width:10%;text-align:left;">Lastname</th>
        <th style="width:10%;text-align:left;">Age</th>
        <th style="width:10%;text-align:left;">Gender</th>
        <th style="width:10%;text-align:left;">Email</th>
    </tr>"""
    table_rows = []
    with libsql_client.create_client_sync(DATABASE_URL) as client:
        patient_result = client.execute("SELECT * FROM patients")
        for row in patient_result:
            table_rows.append(f"""<tr>{''.join(map(lambda col: f"<td>{col}</td>", row[1:]))}</tr>""")
    table_html = f"""<table>{table_head}{''.join(table_rows)}</table>"""
    return f"<h1>Patients</h1>{table_html}"
