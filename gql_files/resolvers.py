from ariadne import QueryType

# Create a QueryType object to associate resolvers with fields.
query = QueryType()


# Resolver for the 'hello' field of the 'Query' type.
@query.field("hello")
def resolve_hello(_, info):
    return "Hello world!"
