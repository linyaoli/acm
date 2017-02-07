import collections

class SimpleRedis:
    # @param size, an integer
    def __init__(self, size):
        # The maximum size of the in-mem database cache.
        self.MAX_SIZE = size
        # An ordered dictionary to mimic a database cache (LRU).
        self.cache = collections.OrderedDict()
        # A command stack to temporarily save the commands of each transaction.
        self.cmd_cache = []
        # A cache to save the total count of each number.
        self.freq_cache = collections.OrderedDict()

    # @param key, a string
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # last_value is used to update the count of changed value.
        last_value = None
        if key in self.cache.keys():
            last_value = self.cache[key]

        try:
            del self.cache[key]
        except:
            # if exceeds the maximum size, pop the least recently used value.
            if len(self.cache) == self.MAX_SIZE:
                self.cache.popitem(last = False)


        self.cache[key] = value
        self.update(value, 1, last_value)


    # @param key, a string
    # @return an integer
    def get(self, key):

        try:
            tmp = self.cache[key]
            del self.cache[key]
            self.cache[key] = tmp
        except:
            return 'NULL'

        return tmp

    # @param key, a string
    # @return
    def unset(self, key):
        try:
            self.update(self.cache[key], 2)
            del self.cache[key]
        except:
            return

    # @param value, an integer
    # @return count, an integer
    def numequalto(self, value):
        count = 0
        try:
            return self.freq_cache[value]
        except:
            return 0

    # an interpreter to deal with input commands.
    # @param input, a string
    # @return
    def cmd(self, input=""):
        commands = input.split()

        if commands[0] in ["SET", "set"]:
            if len(commands) == 3 and not commands[1].isdigit() and commands[2].isdigit():
                if self.cmd_cache != []:
                    self.cmd_cache[-1].append([commands[0], commands[1], commands[2], self.get(commands[1])])
                return self.set(commands[1], int(commands[2]))
            else:
                return self.error(input)

        elif commands[0] in ["GET", "get"]:
            if len(commands) == 2 and not commands[1].isdigit():
                return self.get(commands[1])
            else:
                return self.error(input)

        elif commands[0] in ["UNSET", "unset"]:
            if len(commands) == 2 and not commands[1].isdigit():
                if self.cmd_cache != []:
                    self.cmd_cache[-1].append([commands[0], commands[1], self.get(commands[1])])
                return self.unset(commands[1])
            else:
                return self.error(input)

        elif commands[0] in ["NUMEQUALTO", "numequalto"]:
            if len(commands) == 2 and commands[1].isdigit():
                return self.numequalto(int(commands[1]))
            else:
                return self.error(input)

        elif commands[0] in ["END", "end"]:
            if len(commands) == 1:
                return 'END'

        elif commands[0] in ["BEGIN", "begin"]:
            if len(commands) == 1:
                self.cmd_cache.append([])
            else:
                return self.error(input)

        elif commands[0] in ["COMMIT", "commit"]:
            if len(commands) == 1:
                while self.cmd_cache != []:
                    self.cmd_cache.pop()
            else:
                return self.error(input)

        elif commands[0] in ["ROLLBACK", "rollback"]:
            if len(commands) == 1:
                if len(self.cmd_cache) == 0:
                    return 'NO TRANSACTION'
                cmds = self.cmd_cache.pop()
                for item in cmds:
                    if item[0] in ["SET", "set"]:
                        if item[-1] == 'NULL':
                            self.unset(item[1])
                        else:
                            self.set(item[1], int(item[-1]))

                    elif item[0] in ["UNSET", "unset"]:
                        self.set(item[1], int(item[2]))
        else:
            return self.error(input)
    # Update the total count of numbers.
    # @param value
    # @param mode (1=set, 2=unset)
    # @return nothing
    def update(self, value, mode, last_value=None):
        if mode == 1:
            if last_value:
                self.freq_cache[last_value] -= 1
                if self.freq_cache[last_value] == 0:
                    del self.freq_cache[last_value]

            if value in self.freq_cache.keys():
                self.freq_cache[value] += 1
            else:
                self.freq_cache[value] = 1

        elif mode == 2:
            if value in self.freq_cache.keys():
                self.freq_cache[value] -= 1

            if self.freq_cache[value] == 0:
                del self.freq_cache[value]
        else:
            # illegal mode, discard.
            pass

    def error(self, input):
        return "ILLEGAL COMMAND : " + input
