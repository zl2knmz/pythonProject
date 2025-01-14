import pandas as pd

'''
读取Excel文件：使用 pandas 读取两个Excel文件。
合并数据：将 Excel2 中的 user_account, create_time, create_time2与 Excel1 中的 user_account 进行合并，但保留 Excel1 中的原始顺序。
保存结果：将合并后的数据保存 excel1_with_create_time 文件。
'''


def read_excel_files(excel1_path, excel2_path):
    excel1_df = pd.read_excel(excel1_path)
    excel2_df = pd.read_excel(excel2_path)
    return excel1_df, excel2_df


# 合并数据并保留Excel1中的顺序
def merge_data(excel1_df, excel2_df):
    # 确保列名一致
    excel1_df.columns = ['user_account']
    excel2_df.columns = ['user_account', 'create_time', 'create_time2']

    # 创建一个映射字典
    create_time_dict = excel2_df.set_index('user_account').to_dict(orient='index')

    # 在Excel1中添加创建时间列
    excel1_df['create_time'] = excel1_df['user_account'].map(lambda x: create_time_dict.get(x, {}).get('create_time'))
    excel1_df['create_time2'] = excel1_df['user_account'].map(lambda x: create_time_dict.get(x, {}).get('create_time2'))

    return excel1_df


# 保存结果到Excel1
def save_result(merged_df, output_path):
    merged_df.to_excel(output_path, index=False)


# 主函数
def main():
    # 路径设置
    excel1_path = 'excel1.xlsx'  # 包含用户账号的Excel文件
    excel2_path = 'excel2.xlsx'  # 包含用户账号和创建时间的Excel文件
    output_path = 'excel1_with_create_time.xlsx'  # 输出文件路径

    # 读取Excel文件
    excel1_df, excel2_df = read_excel_files(excel1_path, excel2_path)

    # 合并数据并保留Excel1中的顺序
    merged_df = merge_data(excel1_df, excel2_df)

    # 保存结果到新的Excel文件
    save_result(merged_df, output_path)

    print(f"处理完成，结果已保存到 {output_path}")


if __name__ == '__main__':
    main()
