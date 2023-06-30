# FastApi Tutorial

## Installation

Create and enable venv. You need to have Python 3.11 installed on your system.

```bash
python3 -m venv venv
source venv/bin/activate
```

Install pip packages

```bash
pip install -r requirements.txt
```

## Build and Deploy with Docker

### Build

```bash
docker build -t fastapi-tutorial .
```

### Deploy

```bash
docker run -d --name fastapi-tutorial -p 80:80 fastapi-tutorial
```

