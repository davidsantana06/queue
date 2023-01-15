class Queue:
    # CONSTANT -------------
    MARKER_LEN = len('|  |')
    # ----------------------

    # CONSTRUCTOR -----------
    def __init__(self, size):
        self.__queue = []
        self.__size = size
    # -----------------------

    # AUXILIARY METHODS -------------------------
    def is_full(self):
        return (len(self.__queue) == self.__size)

    def is_empty(self):
        return (len(self.__queue) == 0)
    # -------------------------------------------

    # ADD --------------------------------
    def add(self, item):
        result = ''

        if (not self.is_full()):
            self.__queue.append(item)
            result = self.__get_msg(7, '')
        else:
            result = self.__get_msg(5, '')

        return result
    # ------------------------------------

    # POLL --------------------------------------
    def poll(self):
        result = ''

        if (not self.is_empty()):
            poll_item = self.__queue.pop(0)
            result = self.__get_msg(0, poll_item)
        else:
            result = self.__get_msg(6, '')

        return result
    # -------------------------------------------

    # PEEK --------------------------------------
    def peek(self):
        result = ''

        if (not self.is_empty()):
            peek_item = self.__queue[0]
            result = self.__get_msg(1, peek_item)
        else:
            result = self.__get_msg(6, '')

        return result
    # -------------------------------------------

    # SEARCH -----------------------------------------
    def search(self, item):
        result = ''

        if (not self.is_empty()):
            item_index = ''

            for index in range(len(self.__queue)):
                if (self.__queue[index] == item):
                    item_index = index
                    break

            if (item_index != ''):
                result = self.__get_msg(2, item_index)
            else:
                result = self.__get_msg(8, '')
        else:
            result = self.__get_msg(6, '')

        return result
    # ------------------------------------------------

    # FILL RATE ------------------------------------------------------
    def fill_rate(self):
        fill_rate = '{0} / {1}'.format(len(self.__queue), self.__size)
        return self.__get_msg(3, fill_rate)
    # ----------------------------------------------------------------

    # TO STRING --------------------------------------------
    def __str__(self):
        items = '('

        if (not self.is_empty()):
            for index in range(len(self.__queue)):
                if (index + 1) < len(self.__queue):
                    items += str(self.__queue[index]) + ', '
                else:
                    items += str(self.__queue[index])

        return self.__get_msg(4, (items + ')'))
    # ------------------------------------------------------

    # MSG FORMATTER --------------------------------------------------
    def __get_msg(self, id, item):
        msg = ''

        if (item != ''):
            match (id):
                case 0:
                    msg = '| POLL: {0} |'.format(item)
                case 1:
                    msg = '| PEEK: {0} |'.format(item)
                case 2:
                    msg = '| ITEM IS IN INDEX {0} |'.format(item)
                case 3:
                    msg = '| FILL RATE: {0} |'.format(item)
                case 4:
                    msg = '| QUEUE: {0} |'.format(item)
        else:
            match (id):
                case 5:
                    msg = '| QUEUE IS FULL! |'
                case 6:
                    msg = '| QUEUE IS EMPTY! |'
                case 7:
                    msg = '| ITEM SUCCESSFULLY ADDED! |'
                case 8:
                    msg = '| ITEM IS NOT IN QUEUE! |'

        hyphens = ('-' * (len(msg) - self.MARKER_LEN))
        return ('| {0} |\n{1}\n| {2} |'.format(hyphens, msg, hyphens))
    # ----------------------------------------------------------------
