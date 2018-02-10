import pymongo

client = pymongo.MongoClient(host='127.0.0.1', port=27017)
for url in client['spider']['Hospital'].find(projection={'_id': False, 'url': True}).limit(10):
    print(url)
