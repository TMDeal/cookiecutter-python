FROM python:{{ cookiecutter.python_version }}

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy over docker entrypoint.sh
COPY ./docker/entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# Install system dependencies
# RUN apt-get update -y && apt-get -y install \

# Install poetry
RUN pip install --upgrade pip setuptools
RUN pip install poetry

# Set working directory
COPY . /opt/{{ cookiecutter.project_slug }}
WORKDIR /opt/{{ cookiecutter.project_slug }}

# Install project dependencies
RUN poetry install

# Set docker entrypoint script
ENTRYPOINT ["/docker-entrypoint.sh"]
