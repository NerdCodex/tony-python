class Lexer:
    def __init__(self, data):
        self.tmp = []
        self.data = list(data)
        self.brace = ''
        self.cbrace  = ''
        self.function = []
        self.func_name = ''
        self.line_counter = 0
        self.pos = 0
        self.tokens = []
        self.io = False
        self.string = ''
        self.define_fun = False
        self.call_func = False


    def Character(self):
        #print(self.data)
        if self.pos < len(self.data):
            self.pos += 1
        else:
            exit()
        
    
    def ignore(self):
        self.tmp = []
        self.Character()
    

    def Function(self):
        while self.pos < len(self.data):
            if ''.join(self.tmp) == 'define':
                self.tmp = []
                self.define_fun = True
                self.Character()
            
            elif self.data[self.pos] == '{' and self.define_fun == True and self.cbrace == '':
                self.cbrace = 'open'
                self.func_name += str(''.join(self.tmp))
                self.ignore()
            
            elif self.data[self.pos] == '\n':
                if self.define_fun == True and self.cbrace == 'open':
                    self.line_counter += 1
                    self.Character()
                else:
                    self.line_counter += 1
                    self.ignore()
            

            elif self.data[self.pos] == ' ' and self.define_fun == True:
                self.Character()
            

            elif ''.join(self.tmp) == '\t' and self.cbrace == 'open':
                if self.define_fun == True:
                    self.ignore()
                else:
                    self.ignore()
        
        
            elif self.data[self.pos] == '}' and self.cbrace == 'open':
                for x in self.tmp:
                    self.function.append(x)
                self.cbrace = ''
                self.define_fun = False
                self.ignore()


            elif self.data[self.pos] == '!' and self.call_func == False:
                if self.cbrace == '':
                    self.call_func = True
                    self.ignore()
                else:
                    self.ignore()
                    self.call_func = False
            
            elif ''.join(self.tmp) in self.func_name and self.call_func == True:
                print(self.func_name)
                token = Tokenizer(data=self.function, line=self.line_counter)
                token.Runner()    
                self.ignore()
                self.func_name = ''
                self.call_func = False
                self.func_name = ''
                self.function = []
            


            else:
                self.tmp.append(self.data[self.pos])
                self.Character()
            
            
           

###########################################################################################
###########  Tokenizer class
###########################################################################################

class Tokenizer:
    def __init__(self, data, line):
        self.data = data
        self.line_counter = line
        self.string = ''
        self.brace = ''
        self.tokens = []
        self.node = []
        self.pos = 0
        self.tmp = []
        self.io = False
    

    def Character(self):
        if self.pos < len(self.data):
            self.pos += 1
        else:
            exit()
    



    def ignore(self):
        self.tmp = []
        self.Character()


    def tokenizer(self):
        print(self.data)
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
            
            elif self.data[self.pos] == '(' and self.string == '' and self.io == True:
                if self.data[self.pos+1] == '"':
                        self.ignore()
                        self.brace = 'open'
                else:
                    self.Character()
            
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
            

            elif self.data[self.pos] == ')':
                    if self.data[self.pos-1] == '"' and self.brace != '' and self.io == True:
                        self.ignore()
                        self.brace = ''
                        self.io == False                    
                    else:
                        self.Character()
    

                
            else:
                self.tmp.append(self.data[self.pos])
                self.Character()
            
        print(self.tokens)
    

    def Noder(self):
        self.node = []
        for y in self.tokens:
            if y['id'] == 'print':
                self.node.append(y['value'])
            elif y['id'] == 'str':
                self.node.append(y['value'])
            else:
                break
    
    def Eval(self):
        counter = 0
        while counter < len(self.node):
            if self.node[counter] == 'print':
                print(self.node[counter+1])
                counter += 2
            else:
                counter += 1



    def Runner(self):
        self.tokenizer()
        self.Noder()
        self.Eval()








#################################################################################################
##########   Class runner
#################################################################################################


class Run:
    def __init__(self):
        file = open('new.io', 'r').read()
        self.lexer = Lexer(file)
    
    def run(self):
        self.lexer.Function()



Run().run()
