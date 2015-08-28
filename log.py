import logging


logfile = '/tmp/bgp.log'
logger = logging.getLogger()
logger.setLevel(logging.INFO)
fh = logging.FileHandler(logfile)
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
app.logger.addHandler(fh)
