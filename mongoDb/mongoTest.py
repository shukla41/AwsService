import pymongo
from random import randint
import pprint
import pandas as pd
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

default_key = 'SlTKeYOpHygTYkP3'
mykey = default_key.encode('utf8')

def encrypt(text_to_enc, actual_key):
    try:
        aes_obj = AES.new(actual_key, AES.MODE_CFB, mykey)
        hx_enc = aes_obj.encrypt(text_to_enc.encode('utf8'))
        mret = b64encode(hx_enc).decode('utf-8')
        return mret

    except ValueError as value_error:
        if value_error.args[0] == 'IV must be 16 bytes long':
            raise ValueError('Encryption Error: Key must be 16 characters long')
        elif value_error.args[0] == 'AES key must be either 16, 24, or 32 bytes long':
            raise ValueError('Encryption Error: Encryption key must be either 16, 24, or 32 characters long')
        else:
            raise ValueError(value_error)

def decrypt(encod_text_str, actual_key):
        try:
            aes_obj = AES.new(actual_key.encode('utf8'), AES.MODE_CFB, mykey)
            tmp = b64decode(encod_text_str.encode('utf8'))
            str_dec = aes_obj.decrypt(tmp)
            dcode= str_dec.decode('utf8')
            return dcode
        except ValueError as value_error:
            if value_error.args[0] == 'IV must be 16 bytes long':
                raise ValueError('Decryption Error: Key must be 16 characters long')
            elif value_error.args[0] == 'AES key must be either 16, 24, or 32 bytes long':
                raise ValueError('Decryption Error: Encryption key must be either 16, 24, or 32 characters long')
            else:
                raise ValueError(value_error)

client = pymongo.MongoClient("mongodb://ian:secretPassword@192.168.139.130/cool_db") # defaults to port 27017
db = client.cool_db

# print the number of documents in a collection
#print (db.cool_collection.count())
'''
names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
company_type = ['LLC','Inc','Company','Corporation']
company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']
for x in range(1, 501):
    test = {
        'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
        'rating' : randint(1, 5),
        'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))]
    }
    #Step 3: Insert business object directly into MongoDB via isnert_one
    result=db.reviews.insert_one(test)
    #Step 4: Print to the console the ObjectID of the new document
    print('Created {0} of 500 as {1}'.format(x,result.inserted_id))
#Step 5: Tell us that you are done
print('finished creating 500 business reviews')
'''
print("I am reading all the data")
reviews = db.reviews
print('Total Record for the collection: ' + str(reviews.count()))
#for record in reviews.find():
 #    pprint.pprint(record)

#data = pd.DataFrame(list(reviews.find()))
#print(data)

data=reviews.find()
test_key = 'MyKey4TestingYnP'

for i in data:
    print(decrypt(encrypt(i['name'],test_key),test_key) ,i['rating'] )
