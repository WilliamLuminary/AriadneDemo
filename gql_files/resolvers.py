from ariadne import ObjectType, QueryType, MutationType
from database import fakeDb

# Define the Account type using ObjectType
Account = ObjectType("Account")


# Bind resolvers to the Account type fields
@Account.field("name")
def resolve_name(obj, info):
    return obj.get("name", "")


@Account.field("age")
def resolve_age(obj, info):
    return obj.get("age", 0)


@Account.field("gender")
def resolve_gender(obj, info):
    return obj.get("gender", "")


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
    return list(fakeDb.values())


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
    fakeDb[user_input["name"]] = user_input
    return fakeDb[user_input["name"]]


@Mutation.field("update_account")
def resolve_update_account(_, info, id, user_input):
    if id not in fakeDb:
        fakeDb[id] = user_input
    else:
        for key, value in user_input.items():
            fakeDb[id][key] = value

    return fakeDb[id]
