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
  -d '{          "num__spl__latitude_sp_1": 0.196077,
          "num__spl__longitude_sp_4": 0.002689,
          "num__spl__longitude_sp_0": 0.002521,
          "num__spl__latitude_sp_5": 0.000000,
          "building_id": 19350,
          "num__pol__total_area ceiling_height": 157.206001,
          "num__spl__latitude_sp_0": 0.000464,
          "num__spl__latitude_sp_4": 0.008655,
          "num__spl__longitude_sp_1": 0.126068,
          "floor": 9}'
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
  -d '{          "num__spl__latitude_sp_1": 0.196077,
          "num__spl__longitude_sp_4": 0.002689,
          "num__spl__longitude_sp_0": 0.002521,
          "num__spl__latitude_sp_5": 0.000000,
          "building_id": 19350,
          "num__pol__total_area ceiling_height": 157.206001,
          "num__spl__latitude_sp_0": 0.000464,
          "num__spl__latitude_sp_4": 0.008655,
          "num__spl__longitude_sp_1": 0.126068,
          "floor": 9}'
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
  -d '{          "num__spl__latitude_sp_1": 0.196077,
          "num__spl__longitude_sp_4": 0.002689,
          "num__spl__longitude_sp_0": 0.002521,
          "num__spl__latitude_sp_5": 0.000000,
          "building_id": 19350,
          "num__pol__total_area ceiling_height": 157.206001,
          "num__spl__latitude_sp_0": 0.000464,
          "num__spl__latitude_sp_4": 0.008655,
          "num__spl__longitude_sp_1": 0.126068,
          "floor": 9}'
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