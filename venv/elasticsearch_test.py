from elasticsearch import Elasticsearch
import json


# loads()：将json数据转化成dict数据
# dumps()：将dict数据转化成json数据
# load()：读取json文件数据，转成dict数据
# dump()：将dict数据转化成json数据后写入json文件
def search(_index, _body):
    es = Elasticsearch(["127.0.0.1:9200"])
    return es.search(index=_index, body=_body)


result = search("logstash-log-2019.02", {
    "query": {
        "bool": {
            "must": [
                {
                    "match_all": {}
                }
            ]
        }
    }
})

# result_json = json.dumps(result)
# print(result['hits']['hits'])
for res in result['hits']['hits']:
    print(res)
