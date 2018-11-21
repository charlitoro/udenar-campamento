# Use an official Python runtime as a parent image
FROM python:3.7

ARG DJANGO_ENV

ENV PYTHONUNBUFFERED=1

# Variable de entorno para nuestro directorio del proyecto
ENV WEBAPP_DIR=/src
ENV WEBAPP_CONF=/config

RUN mkdir $WEBAPP_CONF

# Añadir los pqeuetes requerido en el directorio del aplicativo
ADD /config/requirements.txt $WEBAPP_CONF/

# Install any needed packages specified in requirements.txt
RUN pip install -r /config/requirements.txt

# Crear la carpeta del proyecto
RUN mkdir $WEBAPP_DIR

# Set the working directory to /src
WORKDIR $WEBAPP_DIR

# Copy the current directory contents into the container at /src
ADD . $WEBAPP_DIR/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
