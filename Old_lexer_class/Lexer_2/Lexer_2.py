class lexer:
    def __init__(self, data):
        self.data = data
        self.tokens = []
        self.line_counter = 0
        self.char = ""

    def tokenizer(self):
        tmp_num = []
        tmp = []
        temp_id = ''
        temp_exp = ''
        temp_brace = ''
        for x in self.data:
            if x == '(' and temp_brace != 'brace':
                tmp = []
                temp_brace = 'brace'


            elif x == ')' and temp_brace == 'brace' and temp_id != 'string' and temp_exp == '':
                tmp = []
                temp_brace = ''


            elif x == '"' and temp_id != 'string' and temp_brace == 'brace':
                tmp = []
                temp_id = 'string'

            elif x == '"' and temp_id == 'string' and temp_brace == 'brace':
                self.tokens.append({'id':'string', 'value':''.join(tmp)})
                tmp = []
                temp_id = ''

            elif ''.join(tmp) == 'io.println' and temp_id != 'string':
                self.tokens.append({'id':'print_label', 'value':''.join(tmp)})
                tmp = []

            elif ''.join(tmp) == 'io.eval.println' and temp_id != 'string':
                self.tokens.append({'id':'eval_label', 'value':''.join(tmp)})
                tmp = []

            elif ',' == x and temp_brace == 'brace' and temp_id != 'string':
                    temp_exp = 'num'
                    tmp = []
                    print("Done")

            elif x == ')' and temp_brace == 'brace' and temp_id != 'string' and temp_exp == 'num':
                self.tokens.append({'id':'number', 'value':''.join(tmp)})
                tmp = []
                temp_exp = ''
                temp_brace = ''
                temp_num = ''

            elif x == "'" and temp_brace == 'brace' and temp_exp == '':
                tmp = []
                temp_exp = 'num'

            elif x == "'" and temp_brace == 'brace' and temp_exp == 'num':
                self.tokens.append({'id':'number', 'value':''.join(tmp)})
                tmp = []
                temp_exp = ''

            #elif x == '(' or ')' and temp_id == 'string' or temp_brace == 'brace':



            elif ' ' == x and temp_id != 'string':
                continue

            elif '\n' == x and temp_id != 'string' and temp_brace != 'brace':
                self.line_counter += 1


            else:
                tmp.append(x)
        return self.tokens


class Node:
    def __init__(self, tokens):
        self.tokens = tokens
        self.node = []

    def noder(self):
        for x in self.tokens:
            if x['id'] == 'print_label':
                self.node.append(x['value'])
            elif x['id'] == 'number':
                self.node.append(eval(x['value']))
            elif x['id'] == 'string':
                self.node.append(str(x['value']))
            elif x['id'] == 'eval_label':
                self.node.append(x['value'])

        return self.node


class Compiler:
    def __init__(self, node):
        self.node = node
        self.keyword = ['io.println', 'io.eval.println']

    def Compile(self):
        print(self.node)
        counter = 0
        while counter < len(self.node):
            if self.node[counter] == 'io.println':
                if type(self.node[counter+1]) == str and type(self.node[counter+2]) == int or type(self.node[counter+2]) == float:
                    print(self.node[counter+1], self.node[counter+2])
                    counter += 1
                elif type(self.node[counter+1]) == str and type(self.node[counter+2]) != int:
                    print(self.node[counter+1])
                    counter += 1

            elif self.node[counter] == 'io.eval.println':
                if type(self.node[counter+1]) == int or type(self.node[counter+1]) == float or None:
                    print(self.node[counter+1])
                    counter += 1
                else:
                    print('io.eval.println', self.node[counter+1])
                    counter += 1

            else:
                counter += 1
