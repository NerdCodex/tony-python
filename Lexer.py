class lexer:
    def __init__(self, data):
        self.data = data
        self.keyword = []
        self.string = []
        self.char = ""

    def tokenizer(self):
        tmp = []
        temp_id = ''
        for x in self.data:
            if x == '"' and temp_id == '':
                temp_id = 'string'
                tmp = []

            elif x == '"' and temp_id == 'string':
                self.keyword.append({'string': ''.join(tmp)})
                temp_id = ''
                tmp = []

            elif ''.join(tmp) == 'io.buffer.println':
                self.keyword.append({'label': ''.join(tmp)})
                tmp = []

            elif '\n' == x:
                continue

            elif x == ' ' and temp_id != 'string':
                continue

            else:
                tmp.append(x)

        return self.keyword

    def Parser(self):
        self.node = []
        for x in self.keyword:
            for y in x:
                if y == 'label':
                    self.node.append(x['label'])
                elif y == 'string':
                    self.node.append(x['string'])
        return self.node



class Compiler:
    def __init__(self, node):
        self.node = node

    def Eval(self):
        counter = 0
        while counter < len(self.node):
            if self.node[counter] == 'io.buffer.println':
                print(self.node[counter+1])
                counter += 1
            else:
                counter += 1
