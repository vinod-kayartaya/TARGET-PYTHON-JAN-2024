from threading import Thread, Lock
from time import sleep

the_lock = Lock()


def write_char_count(file, sentence):
    chars = []
    chars += sentence
    chars = set(chars)
    with the_lock:
        for each_char in chars:
            print(f'[{sentence}] {each_char} --> {sentence.count(each_char)}', file=file)
            sleep(0.1)


if __name__ == '__main__':
    with open('summary.txt', mode='w') as f1:
        t1 = Thread(target=write_char_count, args=(f1, 'vinod kumar'))
        t2 = Thread(target=write_char_count, args=(f1, 'ananatha kumara'))

        t1.start()
        t2.start()

        # wait until t1 and t2 finish their tasks
        t1.join()
        t2.join()

    print('files is updated')
