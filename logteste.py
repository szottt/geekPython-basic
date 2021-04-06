import logging

logging.basicConfig(level = logging.INFO, filename='logteste.log', filemode='w')

logging.debug("UMa mensagem basica de debug")
logging.info("Um informação do log")
logging.warning("Uma mensagem de perigo")
logging.error("Uma mensagem de erro")
logging.critical("Uma mensagem critica")