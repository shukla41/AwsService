import pymongo
from random import randint
import pprint
import pandas as pd
from Crypto.Cipher import AES
from base64 import b64encode, b64decode


client = pymongo.MongoClient("mongodb://shuva:passport@ec2-3-93-194-198.compute-1.amazonaws.com/my_db") # defaults to port 27017
db = client.my_db

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
    print(i['name'])