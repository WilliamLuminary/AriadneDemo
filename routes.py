import os
from ariadne import graphql_sync
from ariadne.explorer import ExplorerGraphiQL
from flask import jsonify, request, render_template


def init_app(app, schema):
    """Initialize routes for the Flask app."""

    @app.route("/", methods=["GET"])
    def index():
        """Serve the main index.html page."""
        mode = os.environ.get('VIEW_MODE', 'developer')
        if mode == 'client':
            return render_template('public/index.html')
        else:
            return render_template('index.html')

    @app.route("/graphql", methods=["GET"])
    def graphql_explorer():
        """Serve the GraphiQL explorer for GraphQL queries."""
        explorer_html = ExplorerGraphiQL().html(None)
        return explorer_html, 200

    @app.route("/graphql", methods=["POST"])
    def graphql_server():
        """Endpoint for processing GraphQL queries."""
        data = request.get_json()
        success, result = graphql_sync(
            schema,
            data,
            context_value={"request": request},
            debug=app.debug
        )
        status_code = 200 if success else 400
        return jsonify(result), status_code
