# 聚合运算

## 聚合运算的基本格式

```bash
pipline = [$stage1, $stage2, ..., $stageN];

db.<collection>.aggregate(
  pipeline,
  {
    options
  }
)
```

## 模拟数据说明

测试数据中模拟了2019年1月1日~2019年10月31日之间的订单和订单行数据，总计`100000`条。这些数据中包括以下主要字段：

- `userId`: 下单人ID；
- `name`: 订单人联系姓名；
- `orderDate`: 下单日期；
- `shippingFee`: 运费；
- `total`: 订单物品总金额（不包括运费）；
- `status`: 订单状态，取值包括`["created", "cancelled", "shipping", "fulfilled", "completed"]`
- `orderLines`: 订单包含的物品；
  - `price`: 物品售价；
  - `cost`: 物品成本；
  - `qty`: 购买件数；
  - `sku`: 产品唯一编号；

## 导入数据

```bash
# 解压实验数据文件
tar -zxvf dump.tar.gz
# 将实验数据导入到MongoDB
mongorestore -h 127.0.0.1:27017 dump
```
