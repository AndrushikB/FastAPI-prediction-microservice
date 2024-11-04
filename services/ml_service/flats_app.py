"""FastAPI-приложение для модели предсказания цен на недвижимость."""

from fastapi import FastAPI
from ml_service.fast_api_handler import FastApiHandler
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Histogram
from prometheus_client import Counter

# создаём приложение FastAPI
app = FastAPI()

# инициализируем и запускаем экпортёр метрик
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

# добавляем пользовательские метрики
main_app_predictions = Histogram(
    # имя метрики
    "main_app_predictions",
    # описание метрики
    "Histogram of predictions",
    # указываем корзины для гистограммы
    buckets=(1e+06, 5e+06, 1e+07, 1.5e+07, 2e+07)
) 

main_app_counter = Counter("main_app_counter", "count predictions")

# создаём обработчик запросов для API
app.handler = FastApiHandler()

@app.post("/api/flats/")
def get_prediction_for_item(flat_id: str, model_params: dict):
    """Функция для получения прогноза стоимости недвижимости.

    Args:
        flat_id (str): Идентификатор недвижимости.
        model_params (dict): Параметры недвижимости, которые нужно передать в модель.

    Returns:
        dict: Предсказание, цена недвижимости.
    """
    all_params = {
        "flat_id": flat_id,
        "model_params": model_params
    }

    #добавляем метрики в сервис
    main_app_predictions.observe(app.handler.flats_predict(all_params["model_params"]))

    main_app_counter.inc()

    return app.handler.handle(all_params)

@app.get("/")
def read_root():
    return {"Hello": "World"}