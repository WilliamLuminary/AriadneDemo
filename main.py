from ariadne import make_executable_schema, gql
from flask import Flask

from config import Config
from gql_handlers.resolvers import query
from routes import init_app

with open("gql_handlers/schema.graphql", "r") as file:
    schema_str = file.read()

schema = make_executable_schema(gql(schema_str), query)

app = Flask(__name__)
app.config.from_object(Config)

init_app(app, schema)

if __name__ == "__main__":
    app.run(debug=True)
