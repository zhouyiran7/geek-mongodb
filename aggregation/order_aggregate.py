from pymongo import MongoClient
from pprint import pprint
from dateutil import parser

uri = "localhost:27017"
client = MongoClient(uri)

db = client["mock"]
db_col = db["orders"]


def aggregate_order(pipeline):
    result = db_col.aggregate(pipeline)

    pprint(result)
    for r in result:
        pprint(r)


# 计算目前为止所有的订单的总销售额
pipeline = [
    {
        "$group":
        {
            "_id": None,
            "total": {"$sum": "$total"},
        }
    }
]
aggregate_order(pipeline)


# 查询2019年第一季度(1月1日~3月31日)已完成订单(completed)的订单总金 额和订单总数

# 匹配条件
match = {
    "$match": {
        "status": "completed",
        "orderDate":
        {
            "$gte":  parser.parse("2019-01-01T00:00:00.000Z"),
            "$lt":  parser.parse("2019-04-01T00:00:00.000Z"),
        }
    }
}

# 聚合订单总金额 总运费 总数量
group = {
    "$group": {
        "_id": None,
        "total": {"$sum": "$total"},
        "shippingFee": {"$sum": "shippingFee"},
        "count": {"$sum": 1},
    }
}

# 计算总金额
project = {
    "$project": {
        "grandTotal": {
            "$add": ["$total", "$shippingFee"],
        },
        "count": 1,
        "_id": 0,
    }
}


pipeline = [match, group, project]
aggregate_order(pipeline)
