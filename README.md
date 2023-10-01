# AriadneDemo

AriadneDemo is a simple Flask-based GraphQL server using the Ariadne library. It provides a GraphiQL explorer interface for running and testing GraphQL queries, encapsulated within a Docker container for easy deployment and scaling.

## Features

- GraphQL endpoint to process and respond to GraphQL queries.
- Integrated GraphiQL explorer for interactive query execution.
- Dockerized application for consistent deployment and scaling.

## Setup & Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/[your-username]/ariadneDemo.git
   cd ariadneDemo
   ```

   Replace `[your-username]` with your GitHub username or appropriate path.

2. **Build the Docker Image**:

   ```bash
   docker build -t ariadnedemo .
   ```

3. **Run the Docker Container**:

   ```bash
   docker run -p 5000:5000 ariadnedemo
   ```

   This maps port 5000 in the container to port 5000 on your host machine.

## Usage

1. **GraphiQL Explorer**: Once the Docker container is running, navigate to `http://localhost:5000/graphql` in your web browser to access the GraphiQL explorer, where you can interactively run and test GraphQL queries.

2. **GraphQL Endpoint**: Send POST requests with your GraphQL query payloads to the `http://localhost:5000/graphql` endpoint.

## Example Query

You can test the server with the following query:

```graphql
{
  hello
}
```

This should return a response with:

```json
{
  "data": {
    "hello": "Hello world!"
  }
}
```

## Contributing

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.
