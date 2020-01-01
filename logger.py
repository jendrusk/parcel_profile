import logging

# create logger with 'spam_application'
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter("%(asctime)s %(levelname)-7s: %(message)s")
ch.setFormatter(formatter)
# add the handlers to the logger
log.addHandler(ch)

# create file handler which logs even debug messages
#fh = logging.FileHandler('importer.log')
#fh.setLevel(logging.DEBUG)
#fh.setFormatter(formatter)
#logger.addHandler(fh)
