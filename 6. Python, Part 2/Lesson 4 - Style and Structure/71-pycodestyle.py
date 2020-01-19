# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 4. Style & Structure > Section 2:
# Pycodestyle

# spin code: pycodestyle
# Execute as 'pycodestyle filename.py' for results


import time


def spin():
    for _ in range( 100 ):
        for ch in '-\\|/':
            print(ch, end='', flush=True)
            time.sleep(0.1)
            print('\b', end='', flush=True)


if __name__ == '__main__':
  spin()
