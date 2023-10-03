# AriadneDemo

A simple Flask-based GraphQL server utilizing the Ariadne library. Comes with an integrated GraphiQL explorer and is
Docker-ready for seamless deployment and scaling.

## Features

- **GraphQL Endpoint**: Processes and responds to GraphQL queries.
- **GraphiQL Explorer**: An interactive interface for executing GraphQL queries.
- **Docker Support**: Ensures consistent deployments and easy scaling.

## Setup & Installation

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:WilliamLuminary/AriadneDemo.git && cd AriadneDemo
   ```

2. **Build the Docker Image**:
   ```bash
   docker build -t ariadnedemo .
   ```

3. **Launch the Docker Container**:
   ```bash
   docker run -d -p 5002:5002 ariadnedemo
   ```

## Usage

- **GraphiQL Explorer**: Visit `http://localhost:5000/graphql` in your browser to interact with the GraphiQL explorer.
- **GraphQL Endpoint**: POST your GraphQL queries to `http://localhost:5000/graphql`.

### Sample Queries

1. **Simple Query**:
   ```graphql
   {
       hello
   }
   ```

    2. **Multiple Account Creation**:
       ```graphql
       mutation CreateTest {
       createWill: create_account(
       user_input: {name: "Will", age: 18, gender: "M", department: "frontend"}
         ) {
              name
              age
              gender
              department
       	}
       createWilliam: create_account(
       user_input: {name: "William", age: 24, gender: "M", department: "backend"}
         ) {
              name
              age
              gender
              department
           }
       creteBrook: create_account(
       user_input: {name: "Brook", age: 23, gender: "M", department: "finance"}
         ) {
              name
              age
              gender
              department
           }
       }
       ```

    3. **Fetch All Accounts**:
       ```graphql
       query CheckAll{
       	accounts{
               name
               gender
               age
               department
       	}
       }
       ```

    4. **Update Account**:
       ```graphql
       mutation UpdateTest{
           update_account(name: "Will", user_input:{
             age: 50
           }) {
           	age
           }
       }
       ```

    5. **Delete Account**:
       ```graphql
       mutation DeleteTest {
           delete_account(name: "Will") {
               success
               message
           }
       }
        
       ```

## Contributions

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.
