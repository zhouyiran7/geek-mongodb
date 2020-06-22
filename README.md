# MongoDB 下载安装

## 指定安装目录

```bash
mkdir -p /data/db
```

## 下载安装包

```bash
cd /data
curl -O https://fastdl.mongodb.org/osx/mongodb-macos-x86_64-4.2.8.tgz
```

## 解压

```bash
tar -xvf ./mongodb-macos-x86_64-4.2.8.tgz
```

## 添加 PATH

```bash
export PATH=$PATH:/data/mongodb-macos-x86_64-4.2.8/bin
```

## 导入样本

```bash
curl -O -k https://raw.githubusercontent.com/tapdata/geektime-mongodb-course/master/aggregation/dump.tar.gz
```

```bash
tar -xvf dump.tar.gz
```

## 恢复数据

```bash
mongorestore
```
