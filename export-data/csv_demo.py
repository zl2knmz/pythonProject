import csv
from elasticsearch import Elasticsearch


def export_data():
    # 查看参数配置：https://pypi.org/project/elasticsearch/
    es_client = Elasticsearch(hosts=["192.168.16.225:9200"], sniff_on_start=True, sniff_on_connection_fail=True,
                              sniffer_timeout=60, timeout=60)

    id_list = []
    with open('id.txt', newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:
            id_list.append(row[0])
    # print(id_list)
    query_json = {
        "_source": {"includes": ["id", "name", "company", "job_extra"]},
        "query": {
            "bool": {
                "must": [
                    {"terms": {
                        "id": id_list
                    }}
                    # {"match": {
                    #     "title": "人工智能"
                    # }},
                    # {"match_phrase": {
                    #     "title": "AI"
                    # }}
                ]
            }
        }
    }
    response = es_client.search(index='user_profile', body=query_json, scroll='5m', size=1000)
    results = response['hits']['hits']  # es查询出的结果第一页
    total = response['hits']['total']['value']  # es查询出的结果总量
    scroll_id = response['_scroll_id']  # 游标用于输出es查询出的所有结果
    print("total =", total)
    for i in range(0, int(total / 100) + 1):
        # scroll参数必须指定否则会报错
        query_scroll = es_client.scroll(scroll_id=scroll_id, scroll='5m')['hits']['hits']
        results += query_scroll

    with open('data.csv', 'w', newline='', encoding='utf-8') as flow:
        csv_writer = csv.writer(flow, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for res in results:
            # print(res)
            # csv_writer.writerow([res['_id'] + ',' + res['_source']['title']])
            row = res['_source']
            company = ''
            job_extra = ''
            name = ''
            if "company" in row:
                company = row['company']
            if "job_extra" in row:
                job_extra = row['job_extra']
            if "name" in row:
                name = row['name']
            csv_writer.writerow([row['id'], name, company, job_extra])

    print('success!')
    # print(es_client.info())


if __name__ == '__main__':
    export_data()
