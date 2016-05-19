from subprocess import Popen, PIPE
from time import sleep

# Create two threads as follows
subprocesses = []

for no in range(5):
    # celery -A proj worker --loglevel=INFO --concurrency=10 -n worker1.%h
    subprocesses.append(Popen(['python',
                               'manage.py',
                               'celery',
                               '-A', 'jobseek', 'worker',
                               '--loglevel=INFO',
                               '--concurrency=1',
                               '-n', 'worker{}@%h'.format(no)],
                              stdout=PIPE,
                              shell=True))
    sleep(3)

while 1:
    pass