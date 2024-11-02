# Инструкции по запуску микросервиса

Каждая инструкция выполняется из директории репозитория mle-sprint3-completed
Если необходимо перейти в поддиректорию, напишите соотвесвтующую команду

## 1. FastAPI микросервис в виртуальном окружение
```bash
# команды создания виртуального окружения
# и установки необходимых библиотек в него
cd services
sudo apt-get update
sudo apt-get install python3.10-venv
python3.10 -m venv .mle-sprint-3-v001-venv
source .venv_mle-project-sprint-3-v001/bin/activate
pip install -r requirements.txt

# команда перехода в нужную директорию
cd services
# команда запуска сервиса с помощью uvicorn
uvicorn ml_service.flats_app:app --reload --port 8081 --host 0.0.0.0
```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:8081/api/flats/?flat_id=123' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"build_year": 2008,
      "building_type_int": 4,
      "latitude": 55.990021,
      "longitude": 37.232895,
      "ceiling_height": 2.65,
      "flats_count": 107,
      "floors_total": 14,
      "has_elevator": true,
      "floor": 9,
      "kitchen_area": 9.3,
      "living_area": 18.9,
      "rooms": 1,
      "is_apartment": false,
      "total_area": 37.599998}'
```


## 2. FastAPI микросервис в Docker-контейнере

```bash
# команда перехода в нужную директорию
cd services
# команда для запуска микросервиса с использованием docker container
docker image build . --tag flats
docker container run --publish 8081:8081 --volume=./models:/flats_app/models --env-file .env flats
```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:8081/api/flats/?flat_id=123' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"build_year": 2008,
      "building_type_int": 4,
      "latitude": 55.990021,
      "longitude": 37.232895,
      "ceiling_height": 2.65,
      "flats_count": 107,
      "floors_total": 14,
      "has_elevator": true,
      "floor": 9,
      "kitchen_area": 9.3,
      "living_area": 18.9,
      "rooms": 1,
      "is_apartment": false,
      "total_area": 37.599998}'
```

## 3. Docker compose для микросервиса и системы моониторинга

```bash
# команда перехода в нужную директорию
cd services
# команда для запуска микросервиса в режиме docker compose
docker compose up --build
```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:8081/api/flats/?flat_id=123' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"build_year": 2008,
      "building_type_int": 4,
      "latitude": 55.990021,
      "longitude": 37.232895,
      "ceiling_height": 2.65,
      "flats_count": 107,
      "floors_total": 14,
      "has_elevator": true,
      "floor": 9,
      "kitchen_area": 9.3,
      "living_area": 18.9,
      "rooms": 1,
      "is_apartment": false,
      "total_area": 37.599998}'
```

## 4. Скрипт симуляции нагрузки
Скрипт генерирует 40 запросов в течение 110 секунд каждые 2 секунды (с перерывом на 30 секунд после 30 запроса)

```bash
# команды необходимые для запуска скрипта
cd services
python test_requests.py
```

Адреса сервисов:
- микросервис: http://localhost:8081
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000