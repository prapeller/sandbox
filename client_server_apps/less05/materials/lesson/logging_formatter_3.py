"""
Журналирование (логгирование) с использованием модуля logging
Расширенная настройка. Форматирование, обработчики
"""

import logging

# Создать логгер - регистратор верхнего уроовня
# с именем app.main
import sys

# create logger
LOG = logging.getLogger('app.main')

# create handler
SH = logging.StreamHandler(sys.stderr)
FH = logging.FileHandler('app.log', encoding='utf-8')

# set level to handler
SH.setLevel(logging.CRITICAL) # there will be only CRITICAL TO Stream
FH.setLevel(logging.INFO) #  and INFO+CRITICAL to File

# create format
FORMATTER = logging.Formatter("%(asctime)-10s - %(levelname)-30s - %(message)s ")

# set format to handler
FH.setFormatter(FORMATTER)
SH.setFormatter(FORMATTER)

# add handler to logger
LOG.addHandler(FH)
LOG.addHandler(SH)
LOG.setLevel(logging.DEBUG) # < -- anyway there will be only CRITICAL TO Stream and INFO+CRITICAL to File

# pass message to logger
LOG.debug('some debug information')
LOG.info('important information')
LOG.critical('some critical error')
