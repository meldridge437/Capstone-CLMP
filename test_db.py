import db_client as db

#db.createNewDBEntry(["username","pin","fingerID"],["Peyton","1234","1"])

# test to see whats there
res = db.findInDB(["username"],["pin"],[32651])
print(res)

# update entry
db.updateDBEntry(["username"],res,["pin", "fingerID"],[110100,60])
res2 = db.findInDB(["username","pin","fingerID"],["fingerID"],[60])
print(res2)