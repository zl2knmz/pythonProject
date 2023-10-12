import pymysql
from mysql import POOL


def create_conn():
    conn = POOL.connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return conn, cursor


def close_conn(conn, cursor):
    conn.close()
    cursor.close()


def select_one(sql, args):
    conn, cur = create_conn()
    cur.execute(sql, args)
    result = cur.fetchone()
    close_conn(conn, cur)
    return result


def select_all(sql, args):
    conn, cur = create_conn()
    cur.execute(sql, args)
    result = cur.fetchall()
    close_conn(conn, cur)
    return result


def update_data(sql, args):
    conn, cur = create_conn()
    result = cur.execute(sql, args)
    conn.commit()
    close_conn(conn, cur)
    return result


if __name__ == '__main__':
    # sql = ("insert into `users` (`name`,`password`) values (%s,%s)")
    # values = ['test测试35', 124565]
    # res = update_data(sql, values)
    # print(res)

    # sql = "delete from users where name = %s"  #删除
    # res = update_data(sql, "哪吒")
    # print(res)

    sql = "select * from users"  #查询全部
    res = select_all(sql, [])
    print(res)

    # sql = "select * from users where name=%s"  #查询一条
    # res = select_one(sql, "赵振伟")
    # print(res)
