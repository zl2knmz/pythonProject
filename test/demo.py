import ast
import xml.etree.ElementTree as ET
import re
import datetime


def zip_test():
    # zip函数，可迭代对象合并，bulk_predict
    # 也是按照docs的顺序的
    # 创建两个列表
    names = ["Alice", "Bob", "Charlie", "hello"]
    scores = [95, 88, 75]

    # 使用zip将两个列表合并成元组的序列
    combined = zip(names, scores)

    # 遍历合并后的序列并打印
    for item in combined:
        print(item)


def list_test():
    list1 = [1, 2]
    print(len(list1))


def yield_demo():
    x = 1
    yield x
    yield x + 1
    yield x + 2


# 解析活动详情表的表单数据
def parse_event_form(template):
    # 个人敏感数据
    exclude_chars = ['地址', '身份证', '身份证号', '姓名', '手机', '公司', '微信', '姓名', '证件', '邮箱', '单位',
                     '推荐人', '联系人', '联系方式', 'name', 'phone', 'Company', 'Credential', 'Number']
    tmpl_data = {}
    if template and len(template) > 0:
        template = ET.fromstring(template)
        # 遍历<Items>下的所有<Item>元素
        for item in template.findall('Items/Item'):
            # 提取<Sort>和<Title>元素的内容
            sort = item.find('Sort').text
            title = item.find('Title').text
            # 用户数据脱敏
            if all(char not in title for char in exclude_chars):
                tmpl_data['I_' + sort] = title

    return tmpl_data


# 解析活动报名票券的表单数据
def ticket_form_data(template, biz_extra):
    result = []
    tmpl_data = parse_event_form(template)
    if biz_extra and len(biz_extra) > 0:
        data_list = ast.literal_eval(biz_extra)
        # 将列表转换为字典
        data_dict = {d['Key']: d['Value'] for d in data_list}
        for key, value in data_dict.items():
            if key in tmpl_data:
                json_val = tmpl_data[key] + ':' + ",".join(value)
                result.append(json_val)
    return result


if __name__ == '__main__':
    # zip_test()
    # list_test()

    # gene_data = yield_demo()
    # for i in gene_data:
    #     print(i)
    # print(next(gene_data))
    # print(next(gene_data))
    # print(next(gene_data))

    # url = '3412421412432,121'
    # for e in url.split(','):
    #     print(e)

    # s = 'http://nscdn.huodongxing.com/Content/v2.0/img/poster/l_v2/zhanlan-v234124312.//nscdn.huodongxing.com/Content/v2.0/img/poster/l_v2/zhanlan-v234124312.png'
    # s = 'http发斯蒂芬的jpgpng'
    # match_img = re.search('^http.*(jpg|jpeg|png)$', s)
    # print(match_img)
    # if match_img:
    #     print(True)
    # else:
    #     print(False)

    # 获取当前时间
    # now = datetime.datetime.now()
    # 计算当前时间到今天的24点的秒数
    # seconds_to_24h = int((datetime.datetime.combine(now.date(), datetime.time.max) - now).total_seconds())
    # print(seconds_to_24h)

    template_str = '<Form max = "4"><Version>1</Version><Items><Item Category="FIELD_COMPANY"><Sort>10001</Sort><Group>-1</Group><Type>input</Type><Required>True</Required><Title>公司</Title></Item><Item><Sort>2</Sort><Group>-1</Group><Type>input</Type><Required>True</Required><Title>联系人VX号</Title></Item><Item><Sort>4</Sort><Group>-1</Group><Type>checkbox</Type><Required>True</Required><Title>您对哪些平台感兴趣</Title><SubItems><Text>Amazon</Text><Text>TikTok</Text><Text>Mercado</Text><Text>TEMU</Text><Text>SHEIN</Text><Text>SHEIN</Text><Text>速卖通</Text><Text>Walmart</Text><Text>其他</Text></SubItems></Item><Item><Sort>3</Sort><Group>-1</Group><Type>checkbox</Type><Required>True</Required><Title>您对哪个话题感兴趣</Title><SubItems><Text>国内电商如何转型跨境</Text><Text>传统工厂如何布局跨境</Text><Text>AI技术在跨境电商的应用</Text><Text>如何做好旺季营销准备</Text><Text>海外直播怎么做</Text><Text>全托管/半托管主题</Text><Text>其他</Text></SubItems></Item></Items></Form>'
    biz_extra_str = '[{"Key":"I_10001","Value":["橘橙传媒"]},{"Key":"I_2","Value":["1246"]},{"Key":"I_4","Value":["Amazon","TikTok","TEMU","Mercado"]},{"Key":"I_3","Value":["国内电商如何转型跨境"]}]'
    data = ticket_form_data(template_str, biz_extra_str)
    print(data)
