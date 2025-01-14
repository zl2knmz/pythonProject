import pandas as pd


# 读取Excel文件
def read_excel_file(file_path):
    df = pd.read_excel(file_path)
    return df


# 数据预处理和聚合
def aggregate_data(df):
    # 确保列名一致
    df.columns = ['account', 'operation_time']

    # 将操作记录时间转换为datetime类型
    # df['operation_time'] = pd.to_datetime(df['operation_time'])
    # 按天聚合
    # df['date'] = df['operation_time'].dt.date

    # 将操作记录时间转换为datetime类型
    df['operation_time'] = pd.to_datetime(df['operation_time'], format='%Y-%m-%d %H:%M:%S')

    # 按天聚合
    df['date'] = df['operation_time'].dt.strftime('%Y-%m-%d')

    # 计算每个账号在每一天的操作次数
    aggregated_df = df.groupby(['date', 'account']).size().reset_index(name='operation_count')

    return aggregated_df


# 保存结果到Excel文件
def save_result(df, output_path):
    df.to_excel(output_path, index=False)


# 主函数
def main():
    # 路径设置
    input_file = 'match_day.xlsx'  # 包含账号和操作记录时间的Excel文件
    output_file = 'aggregated_match_day.xlsx'  # 输出文件路径

    # 读取Excel文件
    df = read_excel_file(input_file)

    # 检查列名是否正确
    if len(df.columns) != 2 or set(df.columns) != {'account', 'operation_time'}:
        raise ValueError("输入的Excel文件列名不正确，应包含 'account' 和 'operation_time' 两列")

    # 数据预处理和聚合
    aggregated_df = aggregate_data(df)

    # 保存结果到新的Excel文件
    save_result(aggregated_df, output_file)

    print(f"处理完成，结果已保存到 {output_file}")


if __name__ == '__main__':
    main()
