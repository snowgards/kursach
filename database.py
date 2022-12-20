import sqlite3 as sql

async def db_connect() -> None:
    global db, cur

    db = sql.connect('create.db') #подключение к нашей бд (если файла нет, то файл будет создан автоматически)
    cur = db.cursor() #курсор помогает нам взаимодействовать с бд 

    #при помощи execute мы можем писать команды бд в питоне
    cur.execute("CREATE TABLE IF NOT EXISTS test(user_id INTEGER PRIMARY KEY, user INTEGER, corps TEXT, product TEXT, product_order TEXT, verifi TEXT, photo TEXT)")

    db.commit() #обновление нашей бд после каких-то изменений

async def get_all_order():
    order = cur.execute("SELECT * FROM test").fetchall()
    return order

async def get_status_order(message):
    verifi_ = cur.execute(f"SELECT user_id, corps, product_order, verifi FROM test WHERE user_id = {message.chat.id}").fetchone()
    return verifi_

async def create_profile(user_id):
    user = cur.execute("SELECT user_id FROM test WHERE user_id == '{key}'".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO test VALUES(?, ?, ?, ?, ?, ?, ?)", (user_id, '', '', '', '', '', ''))
        db.commit()

async def edit_profile(state, user_id):
    async with state.proxy() as data:
        order = cur.execute("UPDATE test SET user = '{}', corps = '{}', product = '{}', product_order = '{}', verifi = '{}', photo  = '{}' WHERE user_id == '{}' ".format(
            data['user'], data['corps'], data['product'], data['product_order'], data['verifi'], data['photo'], user_id))
        db.commit()

        return order

async def delete_order(user_id: int) -> None:
    cur.execute("DELETE FROM test WHERE user_id = ?", (user_id,))
    db.commit()

async def edit_status_order(user_id: int, verifi: str) -> None:
    cur.execute("UPDATE test SET verifi = ? WHERE user_id = ?", (verifi, user_id))
    db.commit()