from ariadne import InterfaceType, ObjectType, QueryType, MutationType
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    department = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "department": self.department
        }


# Person: InterfaceType
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


# Account: ObjectType
AccountType = ObjectType("Account")


@AccountType.field("department")
def resolve_department(obj, info):
    return obj.get("department", "")


@AccountType.field("salary")
def resolve_salary(obj, info, city=None):
    return 10000 if city in ["LA", "NY"] else 8000


# Query
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
    return Account.Query.filter_by(name=user_name).first() if user_name else None


@Query.field("accounts")
def resolve_accounts(_, info):
    return Account.Query.all()


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
    new_account = Account(
        name=user_input["name"],
        age=user_input["age"],
        gender=user_input["gender"],
        department=user_input["department"]
    )
    db.session.add(new_account)
    db.session.commit()
    return new_account


@Mutation.field("update_account")
def resolve_update_account(_, info, name, user_input):
    account = Account.query.filter_by(name=name).first()
    if account:
        if "name" in user_input:
            account.name = user_input["name"]
        if "age" in user_input:
            account.age = user_input["age"]
        if "gender" in user_input:
            account.gender = user_input["gender"]
        if "department" in user_input:
            account.department = user_input["department"]
        db.session.commit()
    return account


@Mutation.field("delete_account")
def resolve_delete_account(_, info, name):
    account = Account.query.filter_by(name=name).first()
    if account:
        db.session.delete(account)
        db.session.commit()
        return {"success": True, "message": f"Deleted account with name {name}"}
    return {"success": False, "message": f"No account found with name {name}"}
