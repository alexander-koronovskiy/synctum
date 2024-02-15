import sqlite3


def connect_sql():
    return sqlite3.connect("example.db")


def select_user_info(conn, user_id):
    sql = f"SELECT * FROM routes WHERE user_id = '{user_id}'"
    res = conn.cursor().execute(sql)
    return res.fetchall()


def add_info(conn, user_id, r:int, route:int, log:int):
    cur = conn.cursor()
    sql = f"INSERT INTO routes (user_id, round, route, log) VALUES ('{user_id}', '{r}', '{route}', '{log}')"
    cur.execute(sql)
    conn.commit()


def clear_routes_table(conn):
    cur = conn.cursor()
    cur.execute("DELETE FROM routes")
    conn.commit()


def count_by_user(conn, user_id):
    res = conn.cursor().execute("SELECT COUNT(*) FROM routes WHERE user_id = ?", (user_id,))
    return res.fetchall()[0][0]


def show_routes_table(conn):
    sql = "SELECT * FROM routes"
    res = conn.cursor().execute(sql)
    return res.fetchall()


def load_logs(conn, user_id, round):
    res = conn.cursor().execute("SELECT log FROM routes WHERE user_id = ? AND round = ?", (user_id, str(round)))
    return [x[0] for x in res.fetchall()]
