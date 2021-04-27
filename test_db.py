import db_client as db

res = db.findInDB(["username","fingerID"],["pin"],[54321])

print(res)