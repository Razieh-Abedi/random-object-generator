# Use Python 3.10 as base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and input file to the container
COPY process_file.py /app/
COPY random_objects.txt /app/


# Command to run the Python script when the container starts
CMD ["python", "process_file.py"]



