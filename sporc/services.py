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
            "prod": "https://conjurer.se.cretfi.re",
            "local": "http://localhost:3000",
        },
        "endpoints": [],
    },
    "spire mod": {
        "id": "SpeakTheSpireMod",
        "domains": {
            "prod": "https://steamcommunity.com/sharedfiles/filedetails/?id=3159200524",
        },
        "endpoints": [],
    },
    "logan mod": {
        "id": "LoganMod",
        "domains": {
            "prod": "https://steamcommunity.com/sharedfiles/filedetails/?id=3266253644",
        },
        "endpoints": [],
    },
    "battle mod": {
        "id": "BattleStatsMod",
        "domains": {
            "prod": "",
        },
        "endpoints": [],
    },
    "spire": {
        "id": "speak-the-spire-talon",
        "repoPath": "~/.talon/user/talon_umbrella/speak-the-spire-talon",
        "domains": {
            "prod": "https://steamcommunity.com/sharedfiles/filedetails/?id=3159200524",
        },
        "endpoints": [],
    },
    "tracker": {
        "id": "tracker-app",
        "domains": {
            "prod": "http://localhost:5173",
            "local": "http://localhost:5173",
        },
        "endpoints": [],
    },
    "game": {
        "id": "game-wip",
        "domains": {
            "prod": "http://localhost:3000",
            "local": "http://localhost:3000",
        },
        "endpoints": [],
    },
    "craft": {
        "id": "craftinginterpreters",
        "githubPath": "munificent/craftinginterpreters",
        "domains": {
            "prod": "https://craftinginterpreters.com/contents.html",
        },
        "endpoints": [],
    },
    "lox": {
        "id": "loxcraft",
        "domains": {
            "prod": "https://craftinginterpreters.com/contents.html",
        },
        "endpoints": [],
    },
    "sotsf": {
        "id": "sotsf-website",
        "githubPath": "sotsf/sotsf-website",
        "domains": {
            "prod": "https://sotsf-website.vercel.app",
            "local": "http://localhost:3001",
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
