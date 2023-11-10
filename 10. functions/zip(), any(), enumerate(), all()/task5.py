def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql',
              'select', 'update', 'exec', 'del', 'truncate']
    return any(filter(lambda x: x in command, ignore))
