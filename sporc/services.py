from .sporc_types import Service


services: dict[str, Service] = {
    "talon": {
        "id": "talon_umbrella",
        "repoPath": "~/.talon/user/talon_umbrella",
        "domains": {"prod": "https://talonvoice.com/"},
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
    "spire mod": {
        "id": "SpeakTheSpireMod",
        "domains": {
            "prod": "",
        },
        "endpoints": [],
    },
    "spire": {
        "id": "speak-the-spire-talon",
        "domains": {
            "prod": "",
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
    else:
        return "~/projects/" + service["id"]
