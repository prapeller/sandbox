"""
Журналирование (логгирование) с использованием модуля logging. Базовая настройка
"""

import logging

# Быстрая настройка логгирования может быть выполнена так:
logging.basicConfig(
    # файл, в который добавляются журналируемые сообщения
    filename="app_01.log",
    # формат формирования сообщения
    # %(levelname)s - уровень важности
    # %(asctime)s - дата попадания записи в журнал
    # %(message)s - текст сообщения
    format="%(levelname)s %(asctime)s %(message)s",
    # будут обрабатывать сообщения с уровнем важности, равным указанному или выше
    # level=logging.CRITICAL,
    level=logging.WARNING,
    # level=logging.INFO,
    # level=logging.DEBUG,
)

# Для использования логгера его нужно получить/создать функцией getLogger
LOG = logging.getLogger('app.basic')


# После этого можно использовать логгирование таким образом
LOG.debug('Отладочная информация')
LOG.info('Информационное сообщение')
LOG.warning('Предупреждение')
LOG.critical('Критическое общение')

# Обратите внимание, что не все сообщения попали в лог-файл. Почему?