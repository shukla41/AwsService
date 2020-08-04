import pymongo
tarClient = pymongo.MongoClient('mongodb://shuva:12345678@mydoc.cluster-ckjr8tsufjqd.us-east-1.docdb.amazonaws.com:27017/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred')
client = pymongo.MongoClient("mongodb://shuva:passport@ec2-3-93-194-198.compute-1.amazonaws.com/my_db") # defaults to port 27017
db = client.my_db
tarDB=tarClient.my_db
##Specify the collection to be used
col = db.reviews
print('Total Record for the collection: ' + str(col.count()))

result = tarDB.reviews.insert_one(col)

##Insert a single document
col.insert_one({'hello':'Amazon DocumentDB'})

##Find the document that was previously written
x = col.find_one({'hello':'Amazon DocumentDB'})

##Print the result to the screen
print(x)

##Close the connection
tarClient.close()