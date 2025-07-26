FROM docker.io/python:3.11.2-slim AS build-env
COPY LICENSE README.md main.py pyproject.toml uv.lock /install
WORKDIR /install
RUN pip3 install --prefix="/install" --no-cache-dir .

# NOTE: Python version 3.11.2
FROM gcr.io/distroless/python3-debian12:debug-nonroot-0093a0209f695c939427fd207c933bdbadcf7301
COPY --from=build-env /install /app
WORKDIR /app
CMD ["/app/lib/python3.11/site-packages/main.py"]
