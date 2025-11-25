# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build and test RESTful APIs using the FastAPI framework in Python. Students will create endpoints, handle requests and responses, and practice API design principles.

## 📝 Tasks

### 🛠️ Basic FastAPI Setup

#### Description
Set up a FastAPI project and create a simple API with one endpoint that returns a welcome message.

#### Requirements
Completed program should:
- Install and import FastAPI
- Create an app instance
- Define a GET endpoint `/` that returns a JSON welcome message
- Run the server locally

### 🛠️ CRUD Operations API

#### Description
Expand your API to support basic CRUD (Create, Read, Update, Delete) operations for a resource (e.g., items, books, or users).

#### Requirements
Completed program should:
- Define a resource model using Pydantic
- Implement endpoints for:
  - Creating a new resource (POST)
  - Reading all resources (GET)
  - Reading a single resource by ID (GET)
  - Updating a resource by ID (PUT)
  - Deleting a resource by ID (DELETE)
- Return appropriate status codes and messages

### 🛠️ API Documentation & Testing

#### Description
Explore FastAPI's automatic documentation and test your endpoints using the interactive Swagger UI.

#### Requirements
Completed program should:
- Access and review the auto-generated docs at `/docs`
- Test all endpoints using the Swagger UI
- Ensure all endpoints work as expected and handle errors gracefully
