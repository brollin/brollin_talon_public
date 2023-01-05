from .sporc_types import Service
from .swagger import get_swagger_endpoints


services: dict[str, Service] = {
    "schools dash": {
        "id": "sd2",
        "domains": {
            "prod": "https://schools.clever.com",
            "dev": "https://clever-dev--sd2.int.clever.com",
            "local": "http://localhost:5013",
        },
        "endpoints": [
            {
                "name": "users",
                "method": "GET",
                "path": "/users",
                "queryParameters": ["limit"],
            },
            {
                "name": "student",
                "method": "GET",
                "path": "/students/%s",
                "pathParameters": ["studentID"],
                "queryParameters": ["limit"],
            },
        ],
    },
    "ham": {
        "id": "hall-monitor",
        "domains": {
            "prod": "https://hall-monitor.int.clever.com/",
            "dev": "https://clever-dev--hall-monitor.int.clever.com/",
            "local": "http://localhost:5012",
        },
        "endpoints": [],
    },
    "idm config service": {
        "id": "idm-config-service",
        "domains": {
            "prod": "https://production--idm-config-service.int.clever.com/",  # TODO
            "dev": "https://clever-dev--idm-config-service.int.clever.com/",
            "local": "http://localhost:5099",  # TODO
        },
        "swagger": True,
    },
}

# get endpoints from any swagger services
for service_spoken, service in services.items():
    if "swagger" in service and service["swagger"] is True:
        services[service_spoken]["endpoints"] = get_swagger_endpoints(
            "/Users/ben.rollin/go/src/github.com/Clever/"
            + service["id"]
            + "/swagger.yml"
        )
