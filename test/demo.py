import re


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
    s = 'http发斯蒂芬的jpgpng'
    match_img = re.search('^http.*(jpg|jpeg|png)$', s)
    print(match_img)
    if match_img:
        print(True)
    else:
        print(False)


