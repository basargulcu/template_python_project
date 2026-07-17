from pathlib import Path
import environs

env = environs.Env()

ROOT_PATH = Path(env.str("{{ cookiecutter.project_name|upper }}_DIR"))
