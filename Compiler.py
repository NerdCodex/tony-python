class Tokenizer:
    def __init__(self, data):
        self.data = list(data)
        self.token = []
        self.function = []
        self.brace = ''
        self.cbrace = ''
        self.str = ''
        self.function_define = False
        self.pos = 0
        self.line_counter = 0
        self.string = False
        self.call_function = False

    def character(self):
        if self.pos < len(self.data):
            self.pos += 1
        else:
            exit()
    
    def ingnore(self):
        self.character()

    
    def tokens(self):
        tmp = []
        while self.pos < len(self.data):
            if self.data[self.pos] == '{' and self.cbrace == '' and self.function_define == True:
                self.cbrace = 'open'
                self.function.append(''.join(tmp))
                tmp = []
                self.character()
            
            elif ''.join(tmp) == 'define' and self.function_define == False:
                self.function_define = True
                self.character()
                tmp = []
            
            elif self.data[self.pos] == "\n":
                if self.function_define == False:
                    self.character()
                    self.line_counter += 1
                    tmp = []                
                else:
                    self.character()
                    self.line_counter += 1



            elif self.data[self.pos] == "}" and self.cbrace == 'open':
                self.cbrace = ''
                if self.function_define == True:
                    self.function.append(''.join(tmp))
                    self.function_define = False
                    tmp = []
                    self.character()
                else:
                    self.character()
            
            
            elif self.data[self.pos] == "!":
                if ''.join(tmp) in self.function:
                    count = 0
                    while count < len(self.function):
                        if self.function[count] == ''.join(tmp):
                            token = Compiler(data=self.function[count+1], line=self.line_counter)
                            token.Runner()
                            #print(self.function[count+1])
                            tmp = []
                            count += 2
                        else:
                            count += 1
                self.character()
                


            else:
                tmp.append(self.data[self.pos])
                self.character()
        #print(self.function)
                


##############################################################################
###### Tokenizer
##############################################################################


class Compiler:
    def __init__(self, data, line):
        self.data = []
        for x in data:
            self.data.append(x)
        self.line_counter = line
        self.string = ''
        self.brace = ''
        self.tokens = []
        self.node = []
        self.pos = 0
        self.tmp = []
        self.io = False
        self.eval = False
        self.num = ''
        self.digit = "0123456789"
    

    def Character(self):
        if self.pos < len(self.data):
            self.pos += 1
        else:
            exit()
    



    def ignore(self):
        self.tmp = []
        self.Character()


    def tokenizer(self):
        #print(self.data)
        while self.pos < len(self.data):
            if self.data[self.pos] == '.':
                if ''.join(self.tmp) == 'io':
                    self.io = True
                    self.Character()
                    self.tmp = []
                else:
                    self.Character()
            
            elif ''.join(self.tmp) == 'print' and self.io == True:
                self.tokens.append({'id':'print','value':'print'})
                self.ignore()
            
            
            elif ''.join(self.tmp) == 'eval':
                    self.tokens.append({'id':'eval', 'value':'eval'})
                    self.ignore()
            
            elif self.data[self.pos] == '(' and self.string == '' and self.io == True and self.num == '':
                if self.data[self.pos+1] == '"':
                        self.ignore()
                        self.brace = 'open'
                else:
                    self.Character()
            
            elif self.data[self.pos] == ' ' and self.string == '' and self.num == '':
                self.ignore()
            
            elif self.data[self.pos] == "'":
                if self.num == '':
                    self.num = 'num'
                    self.Character()
                elif self.num == 'num':
                    self.tokens.append({'id':'number', 'value':''.join(self.tmp)})
                    self.ignore()
                    self.num = ''

            
            elif self.data[self.pos] == '"' and self.string == '' and self.io == True:
                self.string = 'str'
                self.ignore()
            
            elif self.data[self.pos] == '"' and self.string == 'str':
                if self.data[self.pos+1] == ')':
                        self.tokens.append({'id':'str', 'value':''.join(self.tmp)})
                        self.string = ''
                        self.ignore()
                    
                else:
                    if self.data[self.pos + 1] == '\n':
                        print(f"Line {self.line_counter}\n" + ") is missing")
                        break
            

            elif self.data[self.pos] == ')' and self.num == '':
                    if self.data[self.pos-1] == '"' and self.brace != '' and self.io == True:
                        self.ignore()
                        self.brace = ''
                        self.io == False
                    elif self.num == 'num':
                        self.tokens.append({'id':'number', 'value':''.join(self.tmp)})
                        self.num = ''
                        self.ignore()                    
                    else:
                        self.Character()

           
                     


            else:
                self.tmp.append(self.data[self.pos])
                self.Character()
            
        #print(self.tokens)
    

    def Noder(self):
        self.node = []
        for y in self.tokens:
            if y['id'] == 'print':
                self.node.append(y['value'])
            elif y['id'] == 'eval':
                self.node.append(y['value'])
            elif y['id'] == 'str':
                self.node.append(y['value'])
            elif y['id'] == 'number':
                self.node.append(eval(y['value']))
            else:
                break
    
    def Eval(self):
        counter = 0
        while counter < len(self.node):
            if self.node[counter] == 'print' or 'eval':
                print(self.node[counter+1])
                counter += 2
            else:
                counter += 1



    def Runner(self):
        self.tokenizer()
        self.Noder()
        self.Eval()


##########################################################################
########## Runner
##########################################################################




class Runner:
    def __init__(self, filename):
        self.data = open(filename, 'r').read()

    def run(self):
        tok = Tokenizer(data=self.data)
        tok.tokens()

