ARG PYTHON_VERSION=3.11.2-bullseye

FROM python:${PYTHON_VERSION} as python


FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=local

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev

COPY ./requirements .

RUN pip wheel --wheel-dir /usr/src/app/wheels \
  -r ${BUILD_ENVIRONMENT}.txt


FROM python as python-run-stage
ARG BUILD_ENVIRONMENT=local

ARG APP_HOME=/app

# PYTHONDONTWRITEBYTECODE=1 You tell python to skip writing bytecode files which are PC files when importing modules.
# When Python imports a module, it usually compiles the source code to a bytecode and saves it as a PC
# file alongside the original PY file.
# This speeds up subsequent imports of the module as python can load precompiled bytecode directly.
ENV PYTHONDONTWRITEBYTECODE 1

# PYTHONUNBUFFERED=1 So the python and switch ensures that python's output is not buffered.
# This means that the python output is transmitted directly to the terminal without being buffered, and
# that allows displaying the application's output in real time.
ENV PYTHONUNBUFFERED 1

ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

RUN apt-get update && apt-get install --no-install-recommends -y \
  libpq-dev \
  gettext \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*


COPY --from=python-build-stage /usr/src/app/wheels /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
  && rm -rf /wheels/

COPY ./docker/local/django/entrypoint /entrypoint
# So the purpose of this "sed -i 's/\r$//g'" run command is to ensure that the slash entrypoint file 
# has unique style line endings instead of Windows style line endings.
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# COPY ./docker/local/django/celery/worker/start /start-celeryworker
# RUN sed -i 's/\r$//g' /start-celeryworker
# RUN chmod +x /start-celeryworker

# COPY ./docker/local/django/celery/flower/start /start-flower
# RUN sed -i 's/\r$//g' /start-flower
# RUN chmod +x /start-flower


COPY . ${APP_HOME}

ENTRYPOINT [ "/entrypoint" ]