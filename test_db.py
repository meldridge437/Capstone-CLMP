import db_client as db
import hashlib as h

username = "Peyton"
pin = "12345"
fingerID = 1


def hashPin(pin):
    hashed_pin = h.pbkdf2_hmac('sha256', pin, b'capstone', 1000)
    return hashed_pin

dataSet = [username, hashPin(pin), fingerID]

db.createNewDBEntry(db.DBFieldsList[1:],dataSet)

# test to see whats there
res = db.findInDB(["username"],["pin"],[dataSet[1]])
print(res)

# update entry
newPin = "54321"
db.updateDBEntry(db.DBFieldsList[1:],res,["pin"],[hashPin(newPin)])
res2 = db.findInDB(db.DBFieldsList[1:],["fingerID"],[60])
print(res2)