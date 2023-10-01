from ariadne import QueryType, graphql_sync, make_executable_schema, gql
from ariadne.explorer import ExplorerGraphiQL
from flask import Flask, jsonify, request, render_template

schema = gql('''
    type Query {
        hello: String
    }
''')

query = QueryType()


@query.field("hello")
def resolve_hello(_, info):
    return "Hello world!"


schema = make_executable_schema(schema, query)

app = Flask(__name__)

explorer_html = ExplorerGraphiQL().html(None)


@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')


@app.route("/graphql", methods=["GET"])
def graphql_explorer():
    return explorer_html, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value={"request": request},
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run(debug=True)
