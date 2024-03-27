import libsql_client
from dotenv import dotenv_values
import uuid
import csv

config = dotenv_values(".env")

DATABASE_URL = config["DATABASE_URL"]

with libsql_client.create_client_sync(DATABASE_URL) as client:
    # clear patients table
    client.execute("DELETE FROM patients")
    # insert the data from the csv into the patients table
    with open('scripts/sample_patients.csv') as patients_sample_file:
        parsed_csv = csv.reader(patients_sample_file)
        for row in parsed_csv:
            client.execute(
                """INSERT INTO patients(patientID, firstname, lastname, age, gender, email)
                VALUES (?, ?, ?, ?, ?, ?)""",
                [uuid.uuid4().hex] + row
            )

    # clear doctors table
    client.execute("DELETE FROM doctors")
    # insert the data from the csv into the doctors table
    with open('scripts/sample_doctors.csv') as doctors_sample_file:
        parsed_csv = csv.reader(doctors_sample_file)
        for row in parsed_csv:
            client.execute(
                """INSERT INTO doctors(doctorID, firstname, lastname, speciality, age, gender, email)
                VALUES (?, ?, ?, ?, ?, ?, ?)""",
                [uuid.uuid4().hex] + row
            )