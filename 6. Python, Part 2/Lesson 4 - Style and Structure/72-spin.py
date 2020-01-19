# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 4. Style & Structure > Section 2:
# Pycodestyle

# Execute as 'pycodestyle -u filename.py' for unbufferred/time delay output
# But the above step is not necessary as 'flush=True' is used in print function

# spin code, spins the '/' (forward slash symbol) 100 times.


import time


def spin():
    for _ in range(100):
        for ch in '-\\|/':
            print(ch, end='', flush=True)
            time.sleep(0.1)
            print('\b', end='', flush=True)


if __name__ == '__main__':
    spin()
