import libsql_client
from dotenv import dotenv_values

config = dotenv_values(".env")

DATABASE_URL = config["DATABASE_URL"]

with libsql_client.create_client_sync(DATABASE_URL) as client:
    client.execute("CREATE TABLE IF NOT EXISTS users (username STRING)")
    client.execute("INSERT INTO users VALUES ('Some Name')")
    result_set = client.execute("SELECT * from users")
    print(len(result_set.rows), "rows")
    for row in result_set.rows:
        print(row)
