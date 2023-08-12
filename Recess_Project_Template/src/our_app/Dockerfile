# Use an official Python runtime as a parent image
FROM python:3.10

# Install dbus-1 development libraries
RUN apt-get update && apt-get install -y libdbus-1-dev

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

COPY Recess_Project_Template/src/our_app/requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Expose port 80 to the outside world
EXPOSE 80

# Run the application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]
