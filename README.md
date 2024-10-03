# Microservices ML Project

This project consists of three main microservices: 
- `user-management`: Handles user registration and authentication.
- `prediction-service`: Provides predictions using a machine learning model.
- `data-service`: Manages storing and retrieving prediction data for users.

## Prerequisites
- Docker and Docker Compose installed on your machine.

## How to Run
1. Clone the repository
2. Build and start the services using Docker Compose:
    ```bash
    docker-compose up --build
    ```

The services will be available at the following endpoints:
- User Management Service: `http://localhost:8001`
- Prediction Service: `http://localhost:8002`
- Data Service: `http://localhost:8003`

## Testing the User Management Service

### Register a new user
```bash
curl -X POST "http://localhost:8001/users/register" \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "email": "test@example.com", "password": "testpass"}'
```

### Log in with a user

```bash
curl -X POST "http://localhost:8001/users/login" \
-H "Content-Type: application/json" \
-d '{"email": "test@example.com", "password": "testpass"}'
```

You will receive a JWT token in the response, which you’ll use to authenticate requests to other services.

## Testing the Prediction Service
### Get a prediction (Requires JWT)

```bash
curl -X POST "http://localhost:8002/prediction/predict" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <your_token_here>" \
-d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```
This will return the prediction and probabilities based on the model.

## Testing the Data Service
### Save a prediction (Called automatically after prediction)

The prediction-service automatically sends data to data-service to store the prediction result. This happens internally after each prediction request.

### Fetch the prediction history (Requires JWT)

```bash
curl -X GET "http://localhost:8003/predictions/history/<user_id>" \
-H "Authorization: Bearer <your_token_here>"
```



