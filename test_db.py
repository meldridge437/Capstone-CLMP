import db_client as db
import hashlib as h

username = "Matthew"
pin = "6502"
fingerID = 3

def hashPin(pin):
    rawHash = h.pbkdf2_hmac('sha256', pin.encode("utf-8"), "capstone".encode("utf-8"), 1000)
    strHash = ""
    for B in rawHash:
        strHash += str(B)
    print(strHash)
    return strHash

dataSet = [username, hashPin(pin), fingerID]

db.createNewDBEntry(db.DBFieldsList[1:],dataSet)

# test to see whats there
res = db.findInDB(["username"],["pin"],[dataSet[1]])
print(res)

# update entry
#newPin = "2211"
#db.updateDBEntry(db.DBFieldsList[1:],dataSet,["pin"],[hashPin(newPin)])
#res2 = db.findInDB(db.DBFieldsList[1:],["fingerID"],[1])
#print(res2)
