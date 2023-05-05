import sys
import os.path


class BinSearch:

    def __init__(self, path):
        self.short_path = path
        self.long_path = self._get_full_path()
        self.file_size = self._get_file_size()

        if self._file_exists:
            self.file = self._create_file_object()
        else:
            self.file = None
            print("File does not exist!")

    def _get_full_path(self):
        return os.path.abspath(self.short_path)

    def _file_exists(self):
        return os.path.isfile(self.long_path)

    def _get_file_size(self):
        try:
            return os.path.getsize(self.long_path)
        except OSError:
            pass

    def _create_file_object(self):
        try:
            return open(self.long_path, "rt")
        except OSError:
            pass

    def close_file(self):
        '''If the file is open, close it.'''
        if self.file:
            self.file.close()

    def read_next_line_from(self, offset=0):
        '''Return the next whole line from offset. Offset is number of
        bytes from begginning of the file. Default is zero.'''
        if offset == 0:
            self.file.seek(offset)
            return self.file.readline(), 0
        else:
            self.file.seek(offset)
            self.file.readline()
            line_start = self.file.tell()
            return self.file.readline(), line_start

    def read_line_from(self, offset=0):
        '''Return the rest of line from offset. Offset is number of 
        bytes from begginning of the file. Default is zero.'''
        self.file.seek(offset)
        return self.file.readline()

    def split_line(self, line, separator):
        '''Return line if separator is empty string, else split line by
        separator. Result is returned without newline.'''
        line = line[:-1]
        if separator == '':
            return [line]
        else:
            return line.split(separator)

    def _calculate_middle(self, middle, upper_limit, lower_limit):
        new_middle = (upper_limit + lower_limit) // 2
        if middle == new_middle:
            return new_middle - 1
        else:
            return new_middle

    def find_exact(self, pattern, separator='', field=0):
        '''Returns tuple with line containing pattern and its position
        in file. Pattern must match entire field, but nothing more.'''

        upper_limit = self.file_size
        lower_limit = 0
        limit_gap = upper_limit - lower_limit
        middle = upper_limit // 2

        test = 0  # dbg

        while limit_gap > 0:
            line, line_start = self.read_next_line_from(middle)
            fields = self.split_line(line, separator)
            test += 1  # dbg

            if fields[field] == pattern:
                print(test)  # dbg
                return line, line_start
            elif fields[field] > pattern:
                upper_limit = line_start
                limit_gap = upper_limit - lower_limit
                middle = self._calculate_middle(
                    middle, upper_limit, lower_limit)
            else:
                lower_limit = line_start
                limit_gap = upper_limit - lower_limit
                middle = (upper_limit + lower_limit) // 2
        else:
            return None, line_start


# testing script
if __name__ == "__main__":
    f = BinSearch("/home/vasil/dict-english")
    # print(f.read_next_line_from(f.file_size // 2))
    result = f.find_exact("AAA")
    print(result[0], end='')
    print(result[1])

    f.close_file()
