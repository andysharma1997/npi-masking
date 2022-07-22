import logging

def get_logger(name):
    """logger method to get logger from
    author: andy
    Args:
        name (_type_): _description_
    Returns:
        _type_: _description_
    """
    log_format = '%(levelname)s : %(asctime)-15s %(filename)s:%(lineno)d %(funcName)-8s --> %(message)s'
    logging.basicConfig(format=log_format)
    logger = logging.getLogger(name)
    logger.setLevel('INFO')
    return logger
