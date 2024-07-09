def get_data():
    data = [
        {
            "key": "20240701",
            "doc_count": 15
        },
        {
            "key": "20240705",
            "doc_count": 13
        },
        {
            "key": "20240624",
            "doc_count": 12
        },
        {
            "key": "20240708",
            "doc_count": 12
        },
        {
            "key": "20240620",
            "doc_count": 11
        },
        {
            "key": "20240626",
            "doc_count": 11
        },
        {
            "key": "20240702",
            "doc_count": 11
        },
        {
            "key": "20240621",
            "doc_count": 10
        },
        {
            "key": "20240628",
            "doc_count": 9
        },
        {
            "key": "20240703",
            "doc_count": 9
        },
        {
            "key": "20240622",
            "doc_count": 8
        },
        {
            "key": "20240629",
            "doc_count": 8
        },
        {
            "key": "20240630",
            "doc_count": 8
        },
        {
            "key": "20240704",
            "doc_count": 8
        },
        {
            "key": "20240707",
            "doc_count": 8
        },
        {
            "key": "20240627",
            "doc_count": 7
        },
        {
            "key": "20240623",
            "doc_count": 6
        },
        {
            "key": "20240625",
            "doc_count": 6
        },
        {
            "key": "20240618",
            "doc_count": 5
        },
        {
            "key": "20240619",
            "doc_count": 5
        },
        {
            "key": "20240706",
            "doc_count": 4
        }
    ]
    return data


if __name__ == '__main__':
    date_date = get_data()
    # 使用sorted函数和lambda表达式来根据'key'的值排序
    sorted_data = sorted(date_date, key=lambda x: x['key'])

    # 降序排序
    # sorted_data_desc = sorted(date_date, key=lambda x: x['key'], reverse=True)

    # 打印排序后的数据
    for item in sorted_data:
        print(item)


