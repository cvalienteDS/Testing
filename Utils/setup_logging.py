import logging.config
import yaml
import os
import logging, logging.handlers
import time

def setup_logging(
    default_path=r'Utils/logging.yaml',
    default_level=logging.INFO,
    env_key='LOG_CFG',
    Logs_path=None
):
    """Setup logging configuration

    """
    directorio_actual = os.getcwd()
    path = default_path
    value = os.getenv(env_key, None)
    os.makedirs(Logs_path, exist_ok=True)
    os.chdir(Logs_path)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        # añadimos a filename la fecha actual para que cree un nuevo fichero de log en cada ejecución
        for handler in config['handlers'].values():
            if x := handler.get('filename'):
                x = x[:-4]
                x += time.strftime('_%Y%m%d-%H%M') + '.log'
                handler['filename'] = x

        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
    os.chdir(directorio_actual)
