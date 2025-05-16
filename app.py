from dotenv import load_dotenv  # noqa

load_dotenv(verbose=True)  # noqa

import os  # noqa
from takehome_api.src.main import create_app  # noqa

config_name = os.getenv("APP_SETTING")
if config_name is None:
    config_name = "development"

application = create_app(config_name)

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5001)
