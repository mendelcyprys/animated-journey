import libsql_client
from dotenv import dotenv_values

config = dotenv_values(".env")

DATABASE_URL = config["DATABASE_URL"]

with libsql_client.create_client_sync(DATABASE_URL) as client:
    client.execute(
        """CREATE TABLE IF NOT EXISTS patients (
            patientID STRING PRIMARY KEY NOT NULL,
            firstname STRING,
            lastname STRING,
            age INTEGER,
            gender STRING,
            email STRING
        )"""
    )
    client.execute(
        "CREATE UNIQUE INDEX IF NOT EXISTS unique_patient_email ON patients(email)"
    )
    client.execute(
        """CREATE TABLE IF NOT EXISTS doctors (
            doctorID STRING PRIMARY KEY NOT NULL,
            firstname STRING,
            lastname STRING,
            speciality STRING,
            age INTEGER,
            gender STRING,
            email STRING
        )"""
    )
    client.execute(
        "CREATE UNIQUE INDEX IF NOT EXISTS unique_doctor_email ON doctors(email)"
    )