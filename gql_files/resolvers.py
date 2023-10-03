from ariadne import QueryType, MutationType

from database import fakeDb

# Create a QueryType object to associate resolvers with fields.
query = QueryType()


# Resolver for the 'hello' field of the 'Query' type.
@query.field("hello")
def resolve_hello(_, info):
    return "Hello world!"


# Resolver for the 'account_name' field of the 'Query' type.
@query.field("account_name")
def resolve_account_name(_, info):
    return "William"


# Resolver for the 'age' field of the 'Query' type.
@query.field("age")
def resolve_age(_, info):
    return 18


# Resolver for the 'account' field of the 'Query' type.
@query.field("account")
def resolve_account(_, info, user_name=None, city_name=None):
    return {
        "name": user_name if user_name else "Unknown",
        "age": 20,
        "gender": "M",
        "department": "Backend",
        "salary": 10000 if city_name in ["LA", "NY"] else 8000
    }


@query.field("accounts")
def resolve_accounts(_, info):
    return list(fakeDb.values())


@query.field("get_classmates")
def resolve_get_classmates(_, info, class_no):
    obj = {
        "31": ['Will', 'Bk'],
        "61": ['William', 'Brook']
    }
    return obj[str(class_no)]


mutation = MutationType()


@mutation.field("create_account")
def resolve_create_account(_, info, user_input):
    fakeDb[user_input["name"]] = user_input
    return fakeDb[user_input["name"]]


@mutation.field("update_account")
def resolve_update_account(_, info, id, user_input):
    if id not in fakeDb:
        fakeDb[id] = user_input
    else:
        for key, value in user_input.items():
            fakeDb[id][key] = value

    return fakeDb[id]
