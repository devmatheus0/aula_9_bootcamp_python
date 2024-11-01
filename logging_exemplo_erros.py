from loguru import logger

logger.debug('Um aviso para o dev no futuro')
logger.info('Informação importante do processo')
logger.warning('Um aviso de que algo vai parar de funcionar no futuro')
logger.error('Aconteceu uma falha')
logger.critical('Aconteceu uma falha que aborta a aplicação')
