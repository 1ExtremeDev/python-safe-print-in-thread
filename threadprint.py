from unittest.mock import (
    patch
)
for module in (
    'sys',
    'time',
    'threading'
):
    globals()[module] = __import__(module)


write = sys.stdout.write


def write_ln(text):
    time.sleep(1/2)
    write(str(text) + '\n')


def task(x):
    write_ln(x)


zz = patch('sys.stdout')
zz.write = write_ln
for x in range(30):
    threading.Thread(target=task, args=(x,)).start()
