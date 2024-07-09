import re


def match_url(contents):
    result = None
    # 定义一个网址的模式
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    # 使用正则表达式模式在文本中查找匹配项
    url_list = re.findall(url_pattern, contents)
    # 输出匹配结果
    # for match in url_list:
    #     print(match)
    if url_list is not None and len(url_list) > 0:
        result = url_list[0]
    return result


if __name__ == '__main__':
    # 创建一个字符串，包含一些网址
    text = "这是一个网址，还有一个网址"
    # text = "这是一个网址：https://www.example.com，还有一个网址：http://www.example.org。"
    # text = "这是一个网址：https://5373588946019.huodongxing.com/event/9738517717000"
    # text = "https://5373588946019.huodongxing.com/event/9738517717000"

    # url = match_url(text)
    # print(url)

    # url = 'https://hdxu.cn/wiobu'
    # url = 'https://www.huodongxing.com/event/3737774529800'
    # if 'huodongxing.com' in url or 'hdxu.cn' in url:
    #     print(111111)
    # else:
    #     print(2222222222)

    # logoData = "https://cdn.huodongxing.com/Content/v2.0/img/event_logo.png"
    # filename = logoData.split('.')[-1]
    # print(filename)

    web_url = "https://cdn.hudongba.com/Content/v2.0/img/event_logo.png"
    if '.hudongba.com' in web_url or '.bagevent.com' in web_url or '.31huiyi.com' in web_url or '.duohui.cn' in web_url or '.huodongjia.com' in web_url or '.jinshuju.net' in web_url:
        print("111111！")
    else:
        print("输入或扫描的链接解析内容错误！")

