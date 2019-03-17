from elasticsearch import Elasticsearch
import json


def search(_index, _body):
    es = Elasticsearch(["127.0.0.1:9200"])
    return es.search(index=_index, body=_body)


result = search("logstash-log-2019.02",
                {
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
