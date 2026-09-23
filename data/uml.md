# COSC 310 Team 19 — M0 UML Architecture

Repository inspected: `kunoa2580/cosc310-team19-food-delivery`, branch `main`, tree commit `22e8abe8b353e187810e49d2fa3a15638bb94e79`.


## 1. Proposed unified M0 architecture

The naming rule is **resource → layer → action**:

- Route functions use `restaurant_route_*`.
- Service functions use `restaurant_service_*`.
- Repository functions use `restaurant_repo_*`.
- Generic JSON functions use `json_store_*`.
- The final action vocabulary is consistent: `list`, `get_by_id`, `get_by_name`, `create`, `update`, `deactivate`, and `delete`.

```mermaid
classDiagram
    direction TB

    class Application {
        <<main.py>>
        +app: FastAPI
        +root_route_get() dict 
        +health_route_get() dict 
        +app_handle_restaurant_not_found(request, error) JSONResponse 
        +app_handle_duplicate_restaurant(request, error) JSONResponse 
        +app_handle_data_store_error(request, error) JSONResponse 
    }

    class RestaurantRoutes {
        <<restaurant_route.py>>
        +router: APIRouter
        +restaurant_route_list(cuisine: str or None) list~RestaurantRead~ 
        +restaurant_route_get_by_id(restaurant_id: int) RestaurantRead 
        +restaurant_route_create(payload: RestaurantCreate) RestaurantRead 
        +restaurant_route_delete(restaurant_id: int) Response
    }

    class RestaurantService {
        <<restaurant_service.py>>
        +restaurant_service_list(cuisine: str or None) list~RestaurantRead~ 
        +restaurant_service_get_by_id(restaurant_id: int) RestaurantRead 
        +restaurant_service_create(payload: RestaurantCreate) 
        +restaurant_service_get_by_cuisine(cuisine:str) list~RestaurantRead~
        +restaurant_service_delete_by_id(restaurant_id: int) response
    }

    class RestaurantRepository {
        <<restaurant_repo.py>
        +DEFAULT_DATA_DIR: Path
        +json_store_get_data_path(file_name: str) Path 
        +json_store_load(file_name: str) list~dict~ 
        +RESTAURANTS_FILE: str
        +restaurant_repo_list() list~dict~ 
        +restaurant_repo_get_by_id(restaurant_id: int) 
        +restaurant_repo_get_by_name(name: str) 
        +restaurant_repo_create(data: dict) dict 
        -restaurant_repo_next_id(restaurants: list~dict~) int
        +restaurant_repo_delete_by_id(restaurant_id:int)
    }


    class RestaurantBase {
        +model_config : ConfigDict()
        +name: str
        +address: str
        +phone_number: str
        +email: EmailStr
        +website: HttpUrl
        +cuisine_type: str
        +opening_hours: str
        +rating: float
    }

    class RestaurantCreate {
        +model_config : ConfigDict()
    }

    class RestaurantUpdate {
        +model_config : ConfigDict()
        +name: str or None
        +address: str or None
        +phone_number: str or None
        +email: EmailStr or None
        +website: HttpUrl or None
        +cuisine_type: str or None
        +opening_hours: str or None
        +rating: float or None
    }

    class RestaurantRead {
        +model_config : ConfigDict()
        +id: int
    }

    class RestaurantNotFoundError {
        +restaurant_id: int
    }

    class DuplicateRestaurantError {
        +restaurant_name: str
    }

    class DataStoreError {
        +file_name: str
    }

    class RestaurantsJson {
        +records: list~dict~
    }

    class Pytest {
        +isolated_data(tmp_path,monkeypatch) 
        +client() TestClient 
    }

    class RestaurantRouteTests {
        +test_health_route_get() 
        +test_restaurant_route_list() 
        +test_restaurant_route_filter_by_cuisine() 
        +test_restaurant_route_create_returns_201() 
        +test_restaurant_route_create_duplicate_returns_409()  
    }

    class RestaurantServiceTests {
        +test_restaurant_service_create_rejects_duplicate_name() 
        +test_restaurant_service_get_by_id_raises_when_missing()
        +test_restaurant_service_list_filters_by_cuisine() 
    }

    class RestaurantRepositoryTests {
        +test_restaurant_repo_create_assigns_stable_id() 
        +test_restaurant_repo_create_persists_record() 
        +test_restaurant_repo_get_by_id_returns_none_when_missing()
    }

    RestaurantBase <|-- RestaurantCreate
    RestaurantBase <|-- RestaurantRead

    pplication --> RestaurantRoutes : includes router
    Application ..> RestaurantNotFoundError : maps to HTTP 404
    Application ..> DuplicateRestaurantError : maps to HTTP 409
    Application ..> DataStoreError : maps to HTTP 500

    RestaurantRoutes --> RestaurantService : calls business API
    RestaurantRoutes ..> RestaurantCreate : request body
    RestaurantRoutes ..> RestaurantRead : response model

    RestaurantService --> RestaurantRepository : calls persistence API
    RestaurantService ..> RestaurantNotFoundError : raises
    RestaurantService ..> DuplicateRestaurantError : raises
    RestaurantService ..> RestaurantCreate : accepts
    RestaurantService ..> RestaurantRead : returns

    RestaurantRepository ..> DataStoreError : may propagate

    Pytest --> RestaurantRepository : redirects data directory
    RestaurantRouteTests --> Application : TestClient requests
    RestaurantServiceTests --> RestaurantService : unit tests
    RestaurantRepositoryTests --> RestaurantRepository : persistence tests
```
