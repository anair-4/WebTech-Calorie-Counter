from pymongo import MongoClient
client = MongoClient('127.0.0.1', 27017)
client.drop_database('bulll')
db = client['bull']

words = db['words']

words.insert_one({"id":"1","hindi_word":"idli","english_word":"33","type":"NOUN","difficulty":"1"})
words.insert_one({"id":"2","hindi_word":"Dosa","english_word":"133","type":"NOUN","difficulty":"1"})
words.insert_one({"id":"3","hindi_word":"Coffee","english_word":"124","type":"NOUN","difficulty":"1"})
words.insert_one({"id":"4","hindi_word":"Poori","english_word":"197","type":"NOUN","difficulty":"1"})
words.insert_one({"id":"5","hindi_word":"Icecream","english_word":"207","type":"NOUN","difficulty":"1"})
words.insert_one({"id":"6","hindi_word":"Samosa","english_word":"262","type":"NOUN","difficulty":"1"})
words.insert_one({"id":"7","hindi_word":"Kachori","english_word":"104","type":"NOUN","difficulty":"1"})
words.insert_one({"id":"8","hindi_word":"Bhel","english_word":"289","type":"NOUN","difficulty":"1"})
words.insert_one({"id":"9","hindi_word":"Bhaji","english_word":"542","type":"NOUN","difficulty":"1"})
words.insert_one({"id":"10","hindi_word":"Tea","english_word":"60","type":"NOUN","difficulty":"1"})

words.insert_one({"id":"11","hindi_word":"Apple_pie","english_word":"237","type":"NOUN","difficulty":"2"})
words.insert_one({"id":"12","hindi_word":"Paste","english_word":"164","type":"NOUN","difficulty":"2"})
words.insert_one({"id":"13","hindi_word":"Taco","english_word":"226","type":"NOUN","difficulty":"2"})
words.insert_one({"id":"14","hindi_word":"Burritto","english_word":"206","type":"NOUN","difficulty":"2"})
words.insert_one({"id":"15","hindi_word":"Noodle","english_word":"138","type":"NOUN","difficulty":"2"})
words.insert_one({"id":"16","hindi_word":"Puloa","english_word":"163","type":"NOUN","difficulty":"2"})
words.insert_one({"id":"17","hindi_word":"Pudding","english_word":"120","type":"NOUN","difficulty":"2"})
words.insert_one({"id":"18","hindi_word":"Chicken","english_word":"203","type":"NOUN","difficulty":"2"})
words.insert_one({"id":"19","hindi_word":"Chapathi","english_word":"33","type":"NOUN","difficulty":"2"})
words.insert_one({"id":"20","hindi_word":"Waffles","english_word":"291","type":"NOUN","difficulty":"2"})

words.insert_one({"id":"21","hindi_word":"Souffle","english_word":"169","type":"NOUN","difficulty":"3"})
words.insert_one({"id":"22","hindi_word":"Tiramisu","english_word":"354","type":"NOUN","difficulty":"3"})
words.insert_one({"id":"23","hindi_word":"Keer","english_word":"343","type":"NOUN","difficulty":"3"})
words.insert_one({"id":"24","hindi_word":"Chole","english_word":"364","type":"NOUN","difficulty":"3"})
words.insert_one({"id":"25","hindi_word":"Mutton","english_word":"390","type":"NOUN","difficulty":"3"})
words.insert_one({"id":"26","hindi_word":"Spagetti","english_word":"158","type":"NOUN","difficulty":"3"})
words.insert_one({"id":"27","hindi_word":"LavaCake","english_word":"310","type":"NOUN","difficulty":"3"})
words.insert_one({"id":"28","hindi_word":"Milkshake","english_word":"182","type":"NOUN","difficulty":"3"})
words.insert_one({"id":"29","hindi_word":"Blackforest","english_word":"441","type":"VERB","difficulty":"3"})
words.insert_one({"id":"30","hindi_word":"Aloo","english_word":"277","type":"NOUN","difficulty":"3"})

'''words.insert_one({"uid":"u2","name":"name2","username": "customer2", "password": "5F4DCC3B5AA765D61D8327DEB882CF99", "account_type": "Customer","wallet":5000,"iid":"i1"})
words.insert_one({"uid":"u3","name":"name3","username": "customer3", "password": "5F4DCC3B5AA765D61D8327DEB882CF99", "account_type": "Customer","wallet":5000,"iid":"i2"})
words.insert_one({"uid":"u4","name":"name4","username": "customer4", "password": "5F4DCC3B5AA765D61D8327DEB882CF99", "account_type": "Customer","wallet":5000,"iid":"i2"})
words.insert_one({"uid":"u5","name":"name5","username": "customer5", "password": "5F4DCC3B5AA765D61D8327DEB882CF99", "account_type": "Customer","wallet":5000,"iid":"i2"})

words.insert_one({"uid":"u6","username": "canteen1", "password": "5F4DCC3B5AA765D61D8327DEB882CF99", "account_type": "Canteen","iid":"i1"})
words.insert_one({"uid":"u7","username": "canteen2", "password": "5F4DCC3B5AA765D61D8327DEB882CF99", "account_type": "Canteen","iid":"i1"})
words.insert_one({"uid":"u8","username": "canteen3", "password": "5F4DCC3B5AA765D61D8327DEB882CF99", "account_type": "Canteen","iid":"i2"})
words.insert_one({"uid":"u9","username": "canteen4", "password": "5F4DCC3B5AA7i65D61D8327DEB882CF99", "account_type": "Canteen","iid":"i2"})
words.insert_one({"uid":"u10","username": "canteen5", "password": "5F4DCC3B5AA765D61D8327DEB882CF99", "account_type": "Canteen","iid":"i2"})

words.insert_one({"uid":"u11","username": "caterer1", "password": "5F4DCC3B5AA765D61D8327DEB882CF99", "account_type": "Caterer"})
words.insert_one({"uid":"u12","username": "caterer2", "password": "5F4DCC3B5AA765D61D8327DEB882CF99", "account_type": "Caterer"})
words.insert_one({"uid":"u13","username": "caterer3", "password": "5F4DCC3B5AA765D61D8327DEB882CF99", "account_type": "Caterer"})
words.insert_one({"uid":"u14","username": "caterer4", "password": "5F4DCC3B5AA765D61D8327DEB882CF99", "account_type": "Caterer"})
words.insert_one({"uid":"u15","username": "caterer5", "password": "5F4DCC3B5AA765D61D8327DEB882CF99", "account_type": "Caterer"})

words.insert_one({"uid":"u16","username": "institute1", "password": "5F4DCC3B5AA765D61D8327DEB882CF99", "account_type": "Institution"})
words.insert_one({"uid":"u17","username": "institute2", "password": "5F4DCC3B5AA765D61D8327DEB882CF99", "account_type": "Institution"})


words.insert_one({"uid":"u18","username": "delivery1", "password": "5F4DCC3B5AA765D61D8327DEB882CF99", "account_type": "Delivery"})
words.insert_one({"uid":"u19","username": "delivery2", "password": "5F4DCC3B5AA765D61D8327DEB882CF99", "account_type": "Delivery"})
words.insert_one({"uid":"u20","username": "delivery3", "password": "5F4DCC3B5AA765D61D8327DEB882CF99", "account_type": "Delivery"})
words.insert_one({"uid":"u21","username": "delivery4", "password": "5F4DCC3B5AA765D61D8327DEB882CF99", "account_type": "Delivery"})
words.insert_one({"uid":"u22","username": "delivery5", "password": "5F4DCC3B5AA765D61D8327DEB882CF99", "account_type": "Delivery"})


'''
