from pymongo import MongoClient
from pprint import pprint

uri = "localhost:27017"
client = MongoClient(uri)

db = client["mock"]
db_col = db["orders"]

# 计算目前为止所有的订单的总销售额
pipeline = [
    {"$group":
     {
         "_id": "",
         "total": {"$sum": "$total"}
     }
     }
]
result = db_col.aggregate(pipeline)
pprint(result)
for r in result:
    """
    result:
    {'_id': '', 'total': Decimal128('44019609')}
    """
    pprint(r)
