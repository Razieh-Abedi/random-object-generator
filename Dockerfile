FROM python:3.10-slim


WORKDIR /app


COPY process_file.py /app/
COPY random_objects.txt /app/


CMD ["python", "process_file.py"]



