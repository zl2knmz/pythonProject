import pandas as pd


def merge_and_count_duplicates(excel_path, output_path):
    """
    合并相同的 公司名称 ，并添加一列记录重复次数，列名叫员工个数。
    Args:
        excel_path (str): 输入 Excel 文件路径
        output_path (str): 输出 Excel 文件路径
    """

    df = pd.read_excel(excel_path)

    # Convert '员工编号' to strings
    df['员工编号'] = df['员工编号'].astype(str)

    # 使用 groupby 对 '公司名称' 进行分组
    grouped = df.groupby('公司名称')

    # 使用 agg 创建新的 DataFrame，将 '员工编号' 列用逗号连接，并将 '员工编号' 的数量统计到 '员工个数' 列
    merged_df = grouped.agg(
        员工编号=('员工编号', ', '.join),
        员工个数=('员工编号', 'size')
    ).reset_index()

    # 将合并后的数据写入新的 Excel 文件
    merged_df.to_excel(output_path, index=False)
    print(f"数据已合并并导出到 {output_path}")


if __name__ == '__main__':
    # 示例使用方法
    excel_path1 = 'input1.xlsx'  # 替换为你的输入 Excel 文件路径 表头：公司名称、员工编号
    output_path1 = 'output1.xlsx'  # 替换为你的输出 Excel 文件路径 表头：公司名称、员工编号、员工个数
    merge_and_count_duplicates(excel_path1, output_path1)
