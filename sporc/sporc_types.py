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
    summary: NotRequired[str]
    method: Method
    path: str
    pathParameters: NotRequired[list[str]]
    queryParameters: NotRequired[list[str]]


class Service(TypedDict):
    id: str
    domains: Domains
    swagger: NotRequired[
        bool
    ]  # on true, will look for a swagger spec to define endpoints
    endpoints: NotRequired[list[Endpoint]]