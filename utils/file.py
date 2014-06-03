import os


class File(object):

    @staticmethod
    def write_text_to_file(path, content):
        fp = open(path, 'w')
        fp.write(content)
        fp.close()

    @staticmethod
    def append_text_to_file(path, content):
        fp = open(path, 'a')
        fp.write(content)
        fp.write('\n')
        fp.close()

    @staticmethod
    def exist(path):
        return os.path.exists(path)

    @staticmethod
    def makedir(path):
        if not File.exist(path):
            os.makedirs(path)