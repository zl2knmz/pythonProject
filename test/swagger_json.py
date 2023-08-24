import pandas as pd
import json


# json直接转Excel
def swagger_json_excel():
    df = pd.read_json('D:\\data\\hdxLive-swagger.json', lines=True, encoding='utf-8')
    df.to_excel('D:\\data\\data.xlsx')


# 取swagger json数据的接口路径和名称 导出Excel
def swagger_json_excel1():
    json_list = []
    # 读取JSON文件
    # with open('hdxLive-swagger.json', 'r', encoding="utf-8") as f:
    with open('D:\\data\\hdxLive-swagger.json', 'r', encoding="utf-8") as f:
        data = json.load(f)
        paths = data['paths']
        tags = data['tags']

    for key in paths:
        json_data = {}
        value = {}
        value_type = str(paths[key])
        if value_type.startswith('{\'get'):
            value = paths[key]['get']
        elif value_type.startswith('{\'post'):
            value = paths[key]['post']
        elif value_type.startswith('{\'put'):
            value = paths[key]['put']
        elif value_type.startswith('{\'delete'):
            value = paths[key]['delete']

        controller = value['tags'][0]
        controller_description = ''
        for tag in tags:
            if tag['name'] == controller:
                controller_description = tag['description']

        json_data["controller"] = controller
        json_data["controller_description"] = controller_description
        json_data["path"] = key
        json_data["path_description"] = value['summary']
        json_list.append(json_data)

    # 将JSON数据转换为DataFrame格式
    df = pd.json_normalize(json_list)

    # 将DataFrame写入Excel文件
    writer = pd.ExcelWriter('D:\\data\\data1.xlsx', engine='openpyxl')
    df.to_excel(writer, index=False)
    writer.save()


if __name__ == "__main__":
    # swagger_json_excel()
    swagger_json_excel1()

