FROM python:3.10-slim

WORKDIR /app

# Force a cache invalidation for the COPY . . step
ENV FORCE_REBUILD_APP=2  

# Copy all files
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]