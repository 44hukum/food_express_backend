# Use this template for creating backend in django

This is a backend services for django rest api specially configured for frontend application running on localhost:3000


# Setting up DOCKER
1. To build the project
```
docker build -t template_backend .
```
2. To Run on deatched mode
```
docker run -dp 8000:8000 template_backend
```

GOTO 
for registration: http://127.0.0.1:8000/api/auth/register/
