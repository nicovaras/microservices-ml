# Microservices ML Project

This project consists of two main microservices: 
- `user-management`: Handles user registration and authentication.
- `prediction-service`: Provides predictions using a machine learning model.

## Prerequisites
- Docker and Docker Compose installed on your machine.

## How to Run
1. Clone the repository
2. Build and start the services using Docker Compose:
    ```docker-compose up --build```

The services will be available at the following endpoints:
- User Management Service: `http://localhost:8001`
- Prediction Service: `http://localhost:8002`

## Testing the User Management Service

### Register a new user
```curl -X POST "http://localhost:8001/users/register" -H "Content-Type: application/json" -d '{"username": "testuser", "email": "test@example.com", "password": "testpass"}'```

### Log in with a user
```curl -X POST "http://localhost:8001/users/login" -H "Content-Type: application/json" -d '{"username":"test", "email": "test@example.com", "password": "testpass"}'```


## Testing the Prediction Service

### Get a prediction
```curl -X POST "http://localhost:8002/prediction/predict" -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}'```