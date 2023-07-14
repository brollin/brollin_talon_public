from .sporc_types import Service
from .swagger import get_swagger_endpoints


services: dict[str, Service] = {
    "talon": {
        "id": "talon_umbrella",
        "repoPath": "~/.talon/user/talon_umbrella",
        "domains": {"prod": "https://talonvoice.com/"},
        "endpoints": [],
    },
    "schools dash": {
        "id": "sd2",
        "githubPath": "Clever/sd2",
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
                "path": "/students/{studentID}",
                "pathParameters": ["studentID"],
                "queryParameters": ["limit"],
            },
        ],
    },
    "launchpad": {
        "id": "launchpad",
        "githubPath": "Clever/launchpad",
        "domains": {
            "prod": "https://clever.com/in/brollin",
            "dev": "https://clever-dev--launchpad--b46b913d.int.clever.com/in/brollin",
            "local": "http://localhost:5004/in/brollin",
        },
        "endpoints": [],
    },
    "ham": {
        "id": "hall-monitor",
        "githubPath": "Clever/hall-monitor",
        "domains": {
            "prod": "https://hall-monitor.int.clever.com",
            "dev": "https://clever-dev--hall-monitor.int.clever.com",
            "local": "http://localhost:5012",
        },
        "endpoints": [],
    },
    "idm config": {
        "id": "idm-config-service",
        "githubPath": "Clever/idm-config-service",
        "domains": {
            "prod": "https://production--idm-config-service--crossbill.int.clever.com",
            "dev": "https://clever-dev--idm-config-service--quail.int.clever.com",
            "local": "http://localhost:8080",
        },
        "swagger": True,
        "endpoints": [],
    },
    "idm": {
        "id": "idm",
        "githubPath": "Clever/idm",
        "domains": {
            "prod": "https://production--idm-config-service--crossbill.int.clever.com",
            "dev": "https://clever-dev--idm-config-service--quail.int.clever.com",
            "local": "http://localhost:8080",
        },
        "endpoints": [],
    },
    "ui": {
        "id": "ui",
        "githubPath": "Clever/clever-ui",
        "domains": {
            "prod": "https://master--62fbbb0daff0aa52aea739ac.chromatic.com/",
            "dev": "https://master--62fbbb0daff0aa52aea739ac.chromatic.com/",
            "local": "http://localhost:8080",  # update
        },
        "endpoints": [],
    },
    "lila": {
        "id": "lila",
        "githubPath": "lichess-org/lila",
        "domains": {
            "prod": "https://github.com/lichess-org/lila",
            "local": "http://localhost:9663",
        },
        "endpoints": [],
    },
    "lichess": {
        "id": "lichess",
        "githubPath": "lichess-org/lila",
        "domains": {
            "prod": "https://lichess.org",
            "local": "http://localhost:9663",
        },
        "endpoints": [],
    },
    "next": {
        "id": "nextjs",
        "domains": {
            "prod": "https://brollin.space",
            "local": "http://localhost:3000",
        },
        "endpoints": [],
    },
    "worldhopper": {
        "id": "worldhopper",
        "domains": {
            "prod": "https://worldhopper.vercel.app",
            "local": "http://localhost:3000",
        },
        "endpoints": [],
    },
    "conjurer": {
        "id": "conjurer",
        "githubPath": "SotSF/conjurer",
        "domains": {
            "prod": "https://canopyconjurer.vercel.app",
            "local": "http://localhost:3000",
        },
        "endpoints": [],
    },
}


def get_full_github_path(service: Service):
    return "https://github.com/" + (
        service["githubPath"] if "githubPath" in service else "brollin/" + service["id"]
    )


def get_local_repo_path(service: Service):
    if "repoPath" in service:
        return service["repoPath"]
    elif "githubPath" in service and service["githubPath"].startswith("Clever"):
        return "~/go/src/github.com/Clever/" + service["id"]
    else:
        return "~/projects/" + service["id"]


# get endpoints from any swagger services
for service_spoken, service in services.items():
    if "swagger" in service and service["swagger"] is True:
        services[service_spoken]["endpoints"] = get_swagger_endpoints(
            "/Users/ben.rollin/go/src/github.com/Clever/"
            + service["id"]
            + "/swagger.yml"
        )
