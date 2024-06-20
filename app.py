from ariadne import make_executable_schema, gql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config.config import Config
from gql_file.resolvers import Query, Mutation, Person, Account
from routes import init_app

with open("gql_file/schema.graphql", "r") as file:
    schema_str = file.read()

schema = make_executable_schema(gql(schema_str), Query, Mutation, Person, Account)

# Initialize Flask app with configurations
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
# Initialize routes and add them to the app.
init_app(app, schema)

# @app.before_request
# def check_auth():
#     if "/graphql" in request.path and "auth" not in request.cookies:
#         response = jsonify(error="You are not authorized!!!")
#         response.status_code = 401
#         return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)
