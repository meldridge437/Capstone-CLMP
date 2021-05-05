import db_client as db

newUserData = ["NewDemo","9999","5"]
fields = ["username","pin","fingerID"]

db.createNewDBEntry(fields,newUserData)

# test to see whats there
res = db.findInDB(fields,["pin"],[newUserData[1]])
print(res)

# update entry
#db.updateDBEntry(["username"],res,["pin", "fingerID"],[110100,60])
#res2 = db.findInDB(["username","pin","fingerID"],["fingerID"],[60])
#print(res2)
