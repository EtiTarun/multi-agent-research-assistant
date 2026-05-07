from pathlib import Path


PROJECT_STRUCTURE = {
    "app": {
        "agents": {
            "analyst": ["agent.py"],
            "coordinator": ["agent.py"],
            "researcher": ["agent.py"],
            "writer": ["agent.py"],
        },

        "api": [
            "routes.py"
        ],

        "core": [
            "config.py",
            "logging_config.py",
            "prompts.py"
        ],

        "graph": [
            "state.py",
            "workflow.py"
        ],

        "schemas": [
            "request.py",
            "response.py"
        ],

        "services": {
            "llm": [
                "openrouter_service.py"
            ]
        },

        "utils": [
            "helpers.py"
        ],

        "__files__": [
            "main.py"
        ]
    },

    "logs": [],

    "tests": []
}


BASE_DIR = Path(__file__).resolve().parent


def create_structure(base_path, structure):

    for name, content in structure.items():

        current_path = base_path / name

        if isinstance(content, dict):

            current_path.mkdir(
                parents=True,
                exist_ok=True
            )

            create_structure(current_path, content)

        elif isinstance(content, list):

            current_path.mkdir(
                parents=True,
                exist_ok=True
            )

            for file_name in content:

                file_path = current_path / file_name

                file_path.touch(exist_ok=True)

        else:
            pass


def create_root_files():

    root_files = [
        "README.md",
        ".gitignore"
    ]

    for file_name in root_files:

        file_path = BASE_DIR / file_name

        file_path.touch(exist_ok=True)


def create_app_level_files():

    app_dir = BASE_DIR / "app"

    app_level_files = PROJECT_STRUCTURE["app"].get(
        "__files__",
        []
    )

    for file_name in app_level_files:

        file_path = app_dir / file_name

        file_path.touch(exist_ok=True)


if __name__ == "__main__":

    print("\nCreating project structure...\n")

    create_structure(BASE_DIR, PROJECT_STRUCTURE)

    create_root_files()

    create_app_level_files()

    print("Project structure created successfully.")