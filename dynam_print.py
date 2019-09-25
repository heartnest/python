import time


for i in range(10):
    print(f'\r{i} foo bar', end=' ', flush=True)
    time.sleep(0.5)

print('\ndone!')