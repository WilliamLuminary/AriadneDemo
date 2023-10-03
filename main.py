from ariadne import make_executable_schema, gql
from flask import Flask, request, jsonify

from config import Config
from gql_files.resolvers import query, mutation
from routes import init_app

# Load schema from schema.graphql file
with open("gql_files/schema.graphql", "r") as file:
    schema_str = file.read()

# Create an executable schema from the GraphQL schema string and resolvers.
schema = make_executable_schema(gql(schema_str), query, mutation)

# Initialize Flask app with configurations
app = Flask(__name__)
app.config.from_object(Config)

# Initialize routes and add them to the app.
init_app(app, schema)


# @app.before_request
# def check_auth():
#     if "/graphql" in request.path and "auth" not in request.cookies:
#         response = jsonify(error="You are not authorized!!!")
#         response.status_code = 401
#         return response


if __name__ == "__main__":
    app.run(debug=True)
