from ariadne import graphql_sync
from ariadne.explorer import ExplorerGraphiQL
from flask import jsonify, request, render_template


def init_app(app, schema):
    @app.route("/", methods=["GET"])
    def index():
        return render_template('index.html')

    @app.route("/graphql", methods=["GET"])
    def graphql_explorer():
        explorer_html = ExplorerGraphiQL().html(None)
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
