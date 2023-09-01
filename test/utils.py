import re


def handle_event_logo(logo):
    if logo:
        logo_arr = logo.split(",")
        # 活动logo取最后第二张
        logo_path = logo_arr[-2]
        # 如果路径中不包含"http"，则添加上https://cdn.huodongxing.com/logo/
        # if not re.search(r"http", logo_path):
        if not logo_path.__contains__("http"):
            logo_path = "https://cdn.huodongxing.com/logo/" + logo_path
    else:
        logo_path = "https://cdn.huodongxing.com/Content/v2.0/img/event_logo.png"
    return logo_path


def get_featured_list(featured):
    max_length = 50
    feature_list = []
    result = bin(featured)[2:]
    tmp = list(result)
    bytes_list = list(reversed(tmp))
    for i in range(len(bytes_list)):
        if bytes_list[i] == '1' and i < max_length:
            feature_list.append(i + 1)
    if len(feature_list) == 0:
        feature_list.append(0)
    return feature_list


if __name__ == '__main__':
    # logo = "http://202306/8706264664900/354904621521242.jpg"
    # logo = "202306/8706264664900/354904621521242.jpg,202306/8706264664900/924904656977156.jpg,202306/8706264664900/304905448131266.jpg,202306/8706264664900/754933452474291.jpg,202306/8706264664900/654964803030672.jpg,202306/8706264664900/754981702117927.jpg,202306/8706264664900/844981702110713_v2large.jpg,202306/8706264664900/844981702110713_v2.jpg,202306/8706264664900/844981702110713_v2small.jpg"
    # a = handle_event_logo(logo)
    # print(a)

    b = get_featured_list(562949955520512)
    print(b)
