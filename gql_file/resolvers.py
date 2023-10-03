import sqlite3
import threading

from ariadne import InterfaceType, ObjectType, QueryType, MutationType

_thread_local = threading.local()


def get_db():
    if not hasattr(_thread_local, "conn"):
        _thread_local.conn = sqlite3.connect('database/identifier.sqlite', check_same_thread=False)
        _thread_local.cursor = _thread_local.conn.cursor()

    return _thread_local.conn, _thread_local.cursor


def close_db():
    if hasattr(_thread_local, "conn"):
        _thread_local.cursor.close()
        _thread_local.conn.close()
        del _thread_local.conn
        del _thread_local.cursor


# Define the Person interface using InterfaceType
Person = InterfaceType("Person")


@Person.field("name")
def resolve_name(obj, info):
    return obj.get("name", "")


@Person.field("age")
def resolve_age(obj, info):
    return obj.get("age", 0)


@Person.field("gender")
def resolve_gender(obj, info):
    return obj.get("gender", "")


# Define the Account type using ObjectType
Account = ObjectType("Account")


@Account.field("department")
def resolve_department(obj, info):
    return obj.get("department", "")


@Account.field("salary")
def resolve_salary(obj, info, city=None):
    return 10000 if city in ["LA", "NY"] else 8000


# Create a QueryType object to associate resolvers with fields.
Query = QueryType()


@Query.field("hello")
def resolve_hello(_, info):
    return "Hello world!"


@Query.field("account_name")
def resolve_account_name(_, info):
    return "William"


@Query.field("age")
def resolve_age(_, info):
    return 18


@Query.field("account")
def resolve_account(_, info, user_name=None):
    return {
        "name": user_name if user_name else "Unknown",
        "age": 20,
        "gender": "M",
        "department": "Backend"
    }


@Query.field("accounts")
def resolve_accounts(_, info):
    conn, cursor = get_db()
    cursor.execute("SELECT id, name, age, gender, department FROM ariadne_account_test")
    accounts = cursor.fetchall()
    close_db()
    return [{"id": account[0], "name": account[1], "age": account[2], "gender": account[3], "department": account[4]}
            for account in accounts]


@Query.field("get_classmates")
def resolve_get_classmates(_, info, class_no):
    obj = {
        "31": ['Will', 'Bk'],
        "61": ['William', 'Brook']
    }
    return obj.get(str(class_no), [])


# Define mutations
Mutation = MutationType()


@Mutation.field("create_account")
def resolve_create_account(_, info, user_input):
    conn, cursor = get_db()
    cursor.execute("INSERT INTO ariadne_account_test (name, age, gender, department) VALUES (?, ?, ?, ?)",
                   (user_input["name"], user_input["age"], user_input["gender"], user_input["department"]))
    conn.commit()
    new_id = cursor.lastrowid
    close_db()
    return {"id": new_id, **user_input}


@Mutation.field("update_account")
def resolve_update_account(_, info, name, user_input):
    conn, cursor = get_db()

    updates = []
    values = []
    for key, value in user_input.items():
        updates.append(f"{key} = ?")
        values.append(value)
    values.append(name)
    update_str = ", ".join(updates)

    cursor.execute(f"UPDATE ariadne_account_test SET {update_str} WHERE name = ?", values)
    conn.commit()  # Commit the transaction

    cursor.execute("SELECT * FROM ariadne_account_test WHERE name = ?", (name,))
    updated_record = cursor.fetchone()

    close_db()
    if updated_record:
        columns = [desc[0] for desc in cursor.description]
        return {col: updated_record[i] for i, col in enumerate(columns)}
    else:
        return None


@Mutation.field("delete_account")
def resolve_delete_account(_, info, name):
    conn, cursor = get_db()

    cursor.execute("DELETE FROM ariadne_account_test WHERE name = ?", (name,))
    deleted_rows = conn.total_changes
    conn.commit()
    close_db()
    if deleted_rows:
        return {"success": True, "message": f"Deleted account with name {name}"}
    else:
        return {"success": False, "message": f"No account found with name {name}"}
