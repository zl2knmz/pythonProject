import os  # 获取当前工作路径
import pandas as pd  # 将数据保存至相应文件中


def read():
    df1 = pd.read_csv('../crawler/test.csv')
    for row in df1.iterrows():
        print(row)

    print('1111111111111111')

    df = pd.read_excel('test.xlsx', 'data', index_col=None, na_values=['NA'])
    # 打印头部数据，仅查看数据示例时常用
    print(df.head())

    # 打印列标题
    print(df.columns)

    # 打印行
    print(df.index)

    # 打印指定列
    # print(df["a"])

    # 描述数据
    # print(df.describe())


def save():
    file = os.getcwd() + '\\test.csv'  # 保存文件位置，即当前工作路径下的csv文件
    data = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})  # 要保存的数据
    data.to_csv(file, index=False)  # 数据写入，index=False表示不加索引

    # 新数据，与data具有相同的和列与列名
    data2 = pd.DataFrame({'a': [7, 8, 9], 'b': [1, 2, 3]})
    # 保存至file文件中，index=False表示文件中不添加索引，header=False表示不添加列名，mode='a+'表示在已有数据基础上添加新数据，并不覆盖已有数据
    data2.to_csv(file, index=False, mode='a+', header=False)

    # 方法1，推荐方法
    with pd.ExcelWriter('../crawler/test.xlsx') as writer:
        data.to_excel(writer, index=False, sheet_name='data')
        data2.to_excel(writer, index=False, sheet_name='data2')

    # 写法2
    # writer = pd.ExcelWriter('test.xlsx')
    # data.to_excel(writer, sheet_name='data')
    # data.to_excel(writer, sheet_name='data2')
    # writer.save()
    # writer.close()


if __name__ == '__main__':
    # save()
    read()

