from typing import Union
from typing_extensions import TypedDict, NotRequired, Literal

Method = Union[
    Literal["GET"], Literal["PATCH"], Literal["PUT"], Literal["POST"], Literal["DELETE"]
]


class Domains(TypedDict):
    prod: str
    dev: NotRequired[str]
    local: NotRequired[str]


class Endpoint(TypedDict):
    name: str
    method: Method
    path: str
    pathParameters: NotRequired[list[str]]
    queryParameters: NotRequired[list[str]]


class Service(TypedDict):
    id: str
    name: str
    domains: Domains
    endpoints: NotRequired[list[Endpoint]]


services: list[Service] = [
    {
        "id": "sd2",
        "name": "schools dash",
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
    }
]
