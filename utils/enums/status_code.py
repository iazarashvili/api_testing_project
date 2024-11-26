from enum import Enum


class StatusCode(Enum):
    OK = 200
    created = 201
    noContent = 204
    badRequest = 400
    unauthorized = 401
    notFound = 404
    internalServerError = 500
    badGateway = 502
    serverUnavailable = 503
