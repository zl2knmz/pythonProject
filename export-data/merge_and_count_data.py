import pandas as pd


def merge_and_count_duplicates(excel_path, output_path):
    """
    合并相同的 id 和 手机号单元格，并添加一列记录重复次数。

    Args:
        excel_path (str): 输入 Excel 文件路径
        output_path (str): 输出 Excel 文件路径
    """

    # 读取 Excel 文件
    df = pd.read_excel(excel_path)

    # 使用 groupby 对 id 和 手机号进行分组
    grouped = df.groupby(['id', '手机号'])

    # 创建新列 '发布活动个数' 并填充计数结果
    df['发布活动个数'] = grouped['活动链接'].transform('size')

    # 创建新的 DataFrame 来存储合并后的数据
    merged_df = pd.DataFrame()

    # 遍历每个组
    for (id, phone), group in grouped:
        # 获取网站链接列表
        links = group['活动链接'].tolist()

        # 如果链接列表长度大于 1，表示存在重复
        if len(links) > 1:
            # 将重复的链接合并成一个字符串
            merged_link = ', '.join(links)
            # 添加合并后的数据到新 DataFrame
            merged_df = merged_df.append({'id': id, '手机号': phone, '活动链接': merged_link, '发布活动个数': len(links)},
                                         ignore_index=True)
        else:
            # 如果没有重复，直接添加原始数据
            merged_df = merged_df.append(group, ignore_index=True)

    # 将合并后的数据写入新的 Excel 文件
    merged_df.to_excel(output_path, index=False)
    print(f"数据已合并并导出到 {output_path}")


if __name__ == '__main__':
    # 示例使用方法
    excel_path1 = 'input.xlsx'  # 替换为你的输入 Excel 文件路径
    output_path1 = 'output.xlsx'  # 替换为你的输出 Excel 文件路径
    merge_and_count_duplicates(excel_path1, output_path1)
