# encoding: utf-8

from elasticsearch_dsl.connections import connections
import redis

es = connections.create_connection(hosts=["106.54.68.249:9200"], http_auth=("elastic", "lxyLSFTgvmu5h8z2"),
                                   timeout=3600)


# r = redis.StrictRedis(host='106.54.68.249', port=6800, db=0, password="jokXNhyHEqgjvpmK")

res = es.search(index=["book_test1", "book_test2"], body={
    "_source": ["title", "author"],
    "query": {
        "multi_match": {
            "query": "魔法",
            "fields": ["title"]
        }
    },
    "size": 5
})

res_list = res["hits"]["hits"]

suggest_list = {}
for item in res_list:
    suggest_list[''](item["_source"]["title"])

print(suggest_list)

# print(es.indices.analyze(body={'text': "你好世界", 'analyzer': "ik_max_word"}))
