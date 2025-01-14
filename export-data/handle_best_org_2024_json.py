import json
import requests

"""
年度主办方评选APP JSON 转换
JSON数据：https://cdn.huodongxing.com/hdx-wx/json/bestHost.JSON
"""


def convert_json_format(json1):
    json2 = []

    base_url = "https://topic.huodongxing.com/2025BestOrg/h5/h5.html"

    for entry in json1:
        new_entry = {
            "title": entry["title"],
            # "text": entry["text"],
            "url": base_url,
            "org": [str(org["linkUrl"]) for org in entry["org"] if org.get("linkUrl") not in (None, "")]
        }
        json2.append(new_entry)

    return json2


def read_json_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def write_json_to_file(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def read_json_from_cdn(url):
    response = requests.get(url)
    response.raise_for_status()  # 检查请求是否成功
    data = response.json()
    return data


def main():
    # 文件路径设置
    # input_file_path = 'json1_data.json'  # 输入的JSON1数据文件路径
    output_file_path = 'json2_data.json'  # 输出的JSON2数据文件路径

    # 从文件读取JSON1数据
    # json1_data = read_json_from_file(input_file_path)

    # CDN 文件路径设置
    cdn_url = 'https://cdn.huodongxing.com/hdx-wx/json/bestHost.JSON'  # 替换为实际的CDN URL
    # 从CDN读取JSON1数据
    try:
        json1_data = read_json_from_cdn(cdn_url)["list"]
    except requests.RequestException as e:
        print(f"从CDN读取数据时发生错误: {e}")
        return

    # 转换数据
    json2_data = convert_json_format(json1_data)

    # 将转换后的数据写入文件
    write_json_to_file(json2_data, output_file_path)

    print(f"转换完成，结果已保存到 {output_file_path}")


if __name__ == '__main__':
    main()
