import json
import os
from datetime import datetime

import pymysql
from elasticsearch import Elasticsearch, helpers
from extensions.logger import logger


def isNaN(string):
    return string != string


def get_date_format():
    return '%Y-%m-%d %H:%M:%S'


def get_now_date_string():
    return datetime.now().strftime(get_date_format())


def loadConfig():
    file_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(file_path) as config_file:
        config = json.load(config_file)
    return config


def execSql(sql, values):
    config = loadConfig()
    result = None
    db_opts = {
        'user': config["db.user"],
        'password': config["db.password"],
        'host': config["db.host"],
        'database': config["db.database"],
    }
    db = pymysql.connect(**db_opts)
    cur = db.cursor()
    try:
        cur.execute(sql, values)
        rows = cur.fetchall()
    finally:
        db.close()

    if rows:
        result = list()
        # 表头
        # column_names = list()
        # for i in cur.description:
        #     column_names.append(i[0])
        # result.append(column_names
        for row in rows:
            result.append(row)
    return result


def execUpdateSql(sql, values):
    config = loadConfig()
    result = 0
    db_opts = {
        'user': config["db.user"],
        'password': config["db.password"],
        'host': config["db.host"],
        'database': config["db.database"],
    }
    db = pymysql.connect(**db_opts)
    cur = db.cursor()
    try:
        result = cur.execute(sql, values)
        db.commit()
    finally:
        db.close()
        cur.close()
    return result


# 批量写es
def batch_save_es_data(docs):
    config = loadConfig()
    client = Elasticsearch([config["es.host"]])
    try:
        helpers.bulk(client, docs, request_timeout=300)
    except Exception as e:
        # print("\nERROR:", e)
        logger.error(f"ERROR={e}")


def loadSyncDate(file_path):
    # 检查文件是否存在
    if os.path.exists(file_path):
        # 如果文件存在，读取保存的日期
        with open(file_path, 'r') as file:
            saved_date = file.read().strip()
    else:
        # 如果文件不存在，创建新文件
        with open(file_path, 'w') as file:
            saved_date = get_now_date_string()
            # print("文件不存在，创建新文件。sync_data=", saved_date)
            file.write(saved_date)
            logger.info(f"文件不存在，创建新文件。sync_data={saved_date}")

    return saved_date


def saveSyncDate(file_path, sync_date):
    # 检查文件是否存在
    if os.path.exists(file_path):
        # 如果文件存在，读取保存的日期
        with open(file_path, 'r') as file:
            saved_date = file.read().strip()
    else:
        # 如果文件不存在，创建新文件
        with open(file_path, 'w') as file:
            saved_date = get_now_date_string()
            # print("文件不存在，创建新文件。")
            file.write(saved_date)
            logger.info(f"文件不存在，创建新文件。")

    # 保存当前日期到文件（如果日期有更新）
    if saved_date != sync_date:
        with open(file_path, 'w') as file:
            file.write(sync_date)
    else:
        logger.info(f"日期没有更新，无需保存。")


if __name__ == '__main__':
    # "3101, 4403, 1101"
    # sql = ("SELECT * FROM big_data.`area` WHERE `code` IN (%s,%s,%s)")
    # values = [3101, 4403, 1101]
    # rows = execSql(sql, values)
    # logger.info(f" data={rows}")

    # sql = ("SELECT * FROM users WHERE id > %s AND `name`=%s")
    # values = [2, '张三']

    sql = ("SELECT * FROM users WHERE id > %d AND `name`=%s" % (2, "'张三'"))
    values = []
    print(sql)
    rows = execSql(sql, values)
    logger.info(f"select data={rows}")

    # sql = ("insert into `users` (`name`,`password`) values (%s,%s)")
    # values = ['test测试35', 124565]
    # rows = execUpdateSql(sql, values)
    # logger.info(f"insert data={rows}")

    # sql = ("update `users` set name = %s where id=%s")
    # values = ['test测试31', 31]
    # rows = execUpdateSql(sql, values)
    # logger.info(f"update data={rows}")

    # sql = ("delete from `users` where name = %s")
    # values = ['test测试']
    # rows = execUpdateSql(sql, values)
    # logger.info(f"delete data={rows}")


