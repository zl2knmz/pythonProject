import re


def method_name():
    field = {
        "title": "test",
        "activity_setting": "<Setting><IsPrivate>True</IsPrivate><Summary><![CDATA[开发测试711]]></Summary><HdxTags><![CDATA[创业]]></HdxTags><NotRecommendReason><![CDATA[*同意*.]]></NotRecommendReason><ShowGroupMsg>False</ShowGroupMsg><DistributionEntrance><![CDATA[False]]></DistributionEntrance></Setting>"
    }
    activity_setting = field["activity_setting"]
    summary = ''
    if len(activity_setting) > 0:
        # if activity_setting.__contains__("<Summary>"):
        # if "<Summary>" in activity_setting:
        if activity_setting.find("<Summary>") > 0:
            summary_xml = str(activity_setting).split("<Summary>")[1].split("</Summary>")[0]
            if summary_xml.startswith("<![CDATA["):
                summary = str(summary_xml).split("<![CDATA[")[1].split("]]>")[0]
    print(summary)
    return summary


def method_name1():
    field = {
        "title": "test",
        "activity_setting": "<Setting><IsPrivate>True</IsPrivate><Summary><![CDATA[开发测试711]]></Summary><HdxTags><![CDATA[创业]]></HdxTags><NotRecommendReason><![CDATA[*同意*.]]></NotRecommendReason><ShowGroupMsg>False</ShowGroupMsg><DistributionEntrance><![CDATA[False]]></DistributionEntrance></Setting>"
    }
    activity_setting = field["activity_setting"]
    summary = re.search(r"<Summary>(.*)</Summary>", activity_setting)
    if summary:
        summary = summary.group(1)
    else:
        summary = ''
    if summary.startswith('<![CDATA[') and summary.endswith(']]>') and summary.find('<![CDATA[') == 0 and summary.find(
            ']]>') == len(summary) - len('<![CDATA[]]>'):
        summary = summary[len('<![CDATA['):len(summary) - len(']]>')]
    else:
        summary = ''
    print(summary)
    return summary


if __name__ == '__main__':
    # method_name()
    method_name1()



