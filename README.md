# main-repository-template
Общий шаблон для других репозиториев

<hr>

#### Bages
[![Lint and 100% coverage](https://github.com/llm-network-control/main-repository-template/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/llm-network-control/main-repository-template/actions/workflows/ci.yml)
[![Build and Push image to Dockerhub](https://github.com/llm-network-control/main-repository-template/actions/workflows/dockerhub.yml/badge.svg?branch=main)](https://github.com/llm-network-control/main-repository-template/actions/workflows/dockerhub.yml)
[![On Dockerhub](https://img.shields.io/badge/on-dockerhub-ff0068.svg)](https://hub.docker.com/repository/docker/danteonline/llm-network-control-mcp-server/general)
[![Languages](https://img.shields.io/github/languages/count/llm-network-control/mcp-server)](https://github.com/llm-network-control/main-repository-template)
[![Top Language](https://img.shields.io/github/languages/top/llm-network-control/mcp-server)](https://github.com/llm-network-control/main-repository-template)

## Install

```commandline
pip install -r requirements.txt
pip install -r dev-requirementx.txt
```

## Run

```commandline
cp .env.example .env
```

```commandline
make migrate
```

```commandline
make run
```

## Run linters

```commandline
make lint
```

## Run Tests and Coverage

```commandline
make coverage
```