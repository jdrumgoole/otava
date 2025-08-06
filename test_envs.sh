poetry env use 3.8
poetry update
poetry run pytest

poetry env use 3.9
poetry update
poetry run pytest

poetry env use 3.10
poetry update
poetry run pytest

poetry env use 3.11
poetry update
poetry run pytest
