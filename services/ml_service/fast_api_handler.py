"""Класс FastApiHandler, который обрабатывает запросы API."""

from sklearn.linear_model import Lasso
import joblib
import numpy as np

class FastApiHandler:
    """Класс FastApiHandler, который обрабатывает запрос и возвращает предсказание."""

    def __init__(self):
        """Инициализация переменных класса."""

        # типы параметров запроса для проверки
        self.param_types = {
            "flat_id": str,
            "model_params": dict
        }

        self.model_path = "models/model.pkl"
        self.load_flats_model(model_path=self.model_path)
        
        # необходимые параметры для предсказаний модели стоимости недвижимости
        self.required_model_params = [
                'num__spl__latitude_sp_1', 'num__spl__longitude_sp_4',
                'num__spl__longitude_sp_0', 'num__spl__latitude_sp_5', 'building_id',
                'num__pol__total_area ceiling_height', 'num__spl__latitude_sp_0',
                'num__spl__latitude_sp_4', 'num__spl__longitude_sp_1', 'floor'
            ]

    def load_flats_model(self, model_path: str):
        """Загружаем обученную модель предсказания цены недвижимости.
        Args:
            model_path (str): Путь до модели.
        """
        
        try:
            self.model = joblib.load(model_path)
            print("Model loaded successfully")
        except Exception as e:
            print(f"Failed to load model: {e}")

    def flats_predict(self, model_params: dict) -> float:
        """Предсказываем цену недвижимости.

        Args:
            model_params (dict): Параметры для модели.

        Returns:
            float — предсказанную цену недвижимости
        """
        param_values_list = np.reshape(list(model_params.values()), (1, -1))
        return self.model.predict(param_values_list)[0]
        
    def check_required_query_params(self, query_params: dict) -> bool:
                """Проверяем параметры запроса на наличие обязательного набора.
                
                Args:
                    query_params (dict): Параметры запроса.
                
                Returns:
                        bool: True — если есть нужные параметры, False — иначе
                """
                if "flat_id" not in query_params or "model_params" not in query_params:
                        return False
                
                if not isinstance(query_params["flat_id"], self.param_types["flat_id"]):
                        return False
                        
                if not isinstance(query_params["model_params"], self.param_types["model_params"]):
                        return False
                return True
    
    def check_required_model_params(self, model_params: dict) -> bool:
            """Проверяем параметры пользователя на наличие обязательного набора.
        
            Args:
                model_params (dict): Параметры пользователя для предсказания.
        
            Returns:
                bool: True — если есть нужные параметры, False — иначе
            """
            if set(model_params.keys()) == set(self.required_model_params):
                return True
            return False
    
    def validate_params(self, params: dict) -> bool:
                """Разбираем запрос и проверяем его корректность.
            
                Args:
                    params (dict): Словарь параметров запроса.
            
                Returns:
                    - **dict**: Cловарь со всеми параметрами запроса.
                """
                if self.check_required_query_params(params):
                        print("All query params exist")
                else:
                        print("Not all query params exist")
                        return False
                
                if self.check_required_model_params(params["model_params"]):
                        print("All model params exist")
                else:
                        print("Not all model params exist")
                        return False
                return True
        
    def handle(self, params):
            """Функция для обработки входящих запросов по API. Запрос состоит из параметров.
        
            Args:
                params (dict): Словарь параметров запроса.
        
            Returns:
                - **dict**: Словарь, содержащий результат выполнения запроса.
            """
            try:
                # валидируем запрос к API
                if not self.validate_params(params):
                    print("Error while handling request")
                    response = {"Error": "Problem with parameters"}
                else:
                    model_params = params["model_params"]
                    flat_id = params["flat_id"]
                    print(f"Predicting for flat_id: {flat_id} and model_params:\n{model_params}")
                    # получаем предсказания модели
                    price = self.flats_predict(model_params)
                    response = {
                            "flat_id": flat_id, 
                            "price": round(price, 1),
                        }
            except Exception as e:
                print(f"Error while handling request: {e}")
                return {"Error": "Problem with request"}
            else:
                return response
            

if __name__ == "__main__":

    # создаём тестовый запрос
    test_params = {
        "flat_id": "123",
        "model_params": {
          "num__spl__latitude_sp_1": 0.196077,
          "num__spl__longitude_sp_4": 0.002689,
          "num__spl__longitude_sp_0": 0.002521,
          "num__spl__latitude_sp_5": 0.000000,
          "building_id": 19350,
          "num__pol__total_area ceiling_height": 157.206001,
          "num__spl__latitude_sp_0": 0.000464,
          "num__spl__latitude_sp_4": 0.008655,
          "num__spl__longitude_sp_1": 0.126068,
          "floor": 9
      }
    }

    # создаём обработчик запросов для API
    handler = FastApiHandler()

    # делаем тестовый запрос
    response = handler.handle(test_params)
    print(f"Response: {response}") 
