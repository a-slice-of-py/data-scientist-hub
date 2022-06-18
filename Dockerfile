# SEE: https://medium.com/swlh/alpine-slim-stretch-buster-jessie-bullseye-bookworm-what-are-the-differences-in-docker-62171ed4531d
#      https://pythonspeed.com/articles/base-image-python-docker-images/
ARG BASE_CONTAINER=python:3.9-bullseye
FROM $BASE_CONTAINER as builder

LABEL maintainer="Silvio Lugaro <silvio.lugaro@gmail.com>"

WORKDIR /dsh
COPY ./pyproject.toml dsh/pyproject.toml
COPY ./setup.cfg dsh/setup.cfg

RUN cd dsh && pip install -e .

# Expose MkDocs development server port
EXPOSE 8000

# SEE: https://github.com/squidfunk/mkdocs-material/blob/master/Dockerfile
# Start development server by default
ENTRYPOINT ["mkdocs"]
CMD ["serve", "--dev-addr=0.0.0.0:8000"]