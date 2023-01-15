from queue import Queue


# MSG FORMATTER ------------------------------------------------------
def __get_msg(index):
    msg = ''

    match(index):
        case 0:
            msg = '| --------------------- |' + \
                '\n|     ..: QUEUE :..     |' + \
                '\n| Select one operation: |' + \
                '\n| > 1. Add item         |' + \
                '\n| > 2. Poll item        |' + \
                '\n| > 3. Peek item        |' + \
                '\n| > 4. Search item      |' + \
                '\n| > 5. Fill rate        |' + \
                '\n| > 6. Print queue      |' + \
                '\n| > 0. End app.         |' + \
                '\n| --------------------- |'
        case 1:
            msg = '+-+-+-+-+-+-' + \
                '\n+ GOOD BYE -' + \
                '\n+-+-+-+-+-+-'
        case 2:
            msg = '| INVALID INPUT! |'

    if (index < 2):
        return msg
    else:
        hyphens = ('-' * (len(msg) - Queue.MARKER_LEN))
        return ('| {0} |\n{1}\n| {2} |'.format(hyphens, msg, hyphens))
# --------------------------------------------------------------------


def main():
    queue = Queue(10)
    end_app = False

    while not end_app:
        print(__get_msg(0))
        operation = input('_Operation: ')

        result = ''
        match(operation):
            case '0':
                end_app = True
                result = __get_msg(1)
            case '1':
                item = input('_Item: ')
                result = queue.add(item)
            case '2':
                result = queue.poll()
            case '3':
                result = queue.peek()
            case '4':
                item = input('_Item: ')
                result = queue.search(item)
            case '5':
                result = queue.fill_rate()
            case '6':
                result = str(queue)
            case _:
                result = __get_msg(2)
        
        print('\n{0}\n'.format(result))


main()
