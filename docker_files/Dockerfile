# 1. Use a slim version of Python to keep the image small
FROM python:3.11-slim

# 2. Set the directory inside the container where your code will live
WORKDIR /app
COPY code/ .
COPY code/requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Then copy the rest of the code
COPY code/ .

# 7. Tell Docker which port your app runs on (e.g., 5000 for Flask, 8000 for FastAPI)
EXPOSE 8080

# 8. Define the command to run your app
# Replace 'app.py' with your main entry file
CMD ["python", "main.py"]