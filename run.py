from app.utils import get_config
from app import create_app

config_name = get_config('APP_SETTINGS')  # config_name = "development"
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
