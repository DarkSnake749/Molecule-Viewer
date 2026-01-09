from panda3d.core import Vec3

def list_to_str(_list) -> str:
    r_str = ""
    for c in _list:
        r_str += c
    return r_str

class Syntax:
    non_split_char = ['"', '(', ')']

    act_def = {
        "molecule": "mol",
        "text": "tex",

        "start-str": '"',
        "end-str": '"',

        "start-arg": "(",
        "end-arg": ")",

        "separator": ",",
    }

class MVReader:
    def __init__(self, file_path):
        self.path = file_path
        self.file_content = self.read_file()
        self.trim_content = self.trim()
        self.token_content = self.tokenize()
        self.parse_content = []
        
        self.molecule = {}
        self.text = {}
    
    # * Utils function
    def custom_split(self, line, skip_ele) -> list[str]:
        split_line = []
        ele = ""
        ignore = False
        
        for c in line:
            if c != skip_ele or ignore:
                if c in Syntax.non_split_char:
                    ignore = not ignore
                ele += c
                continue
            split_line.append(ele)
            ele = ""
        if ele:
            split_line.append(ele)
        return split_line
    
    def remove_comment(self, line) -> list[list]:
        new_parse_line = []
        for c in line:
            if c == '#':
                return new_parse_line
            new_parse_line.append(c)
        return new_parse_line
    
    def remove_spaces(self, token_line, ele=' ') -> str:
        new_line = []
        for token in token_line:
            if not token.startswith(Syntax.act_def["start-arg"]):
                new_line.append(token)
                continue
            new_token = ""
            for c in token:
                if c == ele:
                    continue
                new_token += c
            new_line.append(new_token)
        return new_line

    def contain(self, token) -> bool:
        for c in token:
            if c in Syntax.non_split_char:
                return True
        return False

    def verify_int(self, item_list) -> bool:
        for item in item_list: 
            try:
                int(item)
                continue
            except:
                return False
        return True

    def arguments_to_vec(self, args: str) -> Vec3:
        list_args = list(args)
        list_args.pop(0)
        list_args.pop( len(list_args) - 1 )

        trimmed_args = list_to_str(list_args)
        trim_args_list = trimmed_args.split(Syntax.act_def["separator"])

        arg_num_list = []
        for arg in trim_args_list:
            arg_num_list.append(float(arg))
        
        return Vec3(
            arg_num_list[0],
            arg_num_list[1],
            arg_num_list[2])

    # * Tokenize the scripts
    def read_file(self) -> list[str]:
        with open(self.path, 'r') as file:
            return file.readlines()
    
    def trim(self) -> list[str]:
        """ Remove de \n at the end of each line """
        trim_content = []
        for line in self.file_content:
            line_list = list(line)
            line_list.pop(len(line_list)-1)
            new_line = list_to_str(line_list)
            trim_content.append(new_line)
        return trim_content
    
    def tokenize(self) -> list[list]:
        tokenize_content = []
        for line in self.trim_content:
            new_line = self.custom_split(line, ' ')
            new_line = self.remove_comment(new_line)
            new_line = self.remove_spaces(new_line)

            if new_line:
                tokenize_content.append(new_line)
        return tokenize_content
    
    # * Analyse and parse each token
    def analyze_new_element(self, token_line, nb_argument) -> bool:
        for i, token in enumerate(token_line):
            if i == 0:
                continue
            elif i == 1 and self.contain(token):
                raise NameError(f"The name {token} is not a valid name")
            elif i == 2:
                if (
                    not token.startswith(Syntax.act_def["start-str"]) or 
                    not token.endswith(Syntax.act_def["end-str"])
                ):
                    raise ValueError(f'{token} must start and finish with \' " \'')
            elif i == 3:
                if (
                    not token.startswith(Syntax.act_def["start-arg"]) or 
                    not token.endswith(Syntax.act_def["end-arg"])
                ):
                    raise ValueError(f'{token} must start with "(" and finish with ")"')
                
                token_list = list(token)
                token_list.pop(0)
                token_list.pop( len(token_list) - 1 )
                new_token = list_to_str(token_list)

                argument_list = new_token.split(Syntax.act_def["separator"])
                if len(argument_list) != nb_argument:
                    raise ValueError(f"{token} must contain 3 arguments, there's {len(argument_list)}")

                if not self.verify_int(argument_list):
                    raise ValueError(f"{token} must contain float or integer")

            elif i > 3:
                raise SyntaxError(f"{token}: Can't be an argument since it can only pass {nb_argument} arguments")

    def parse_token(self, token_line, transform_to_vec3: bool) -> list:
        new_token_line = []
        for token in token_line:
            new_token: None
            if token.startswith(Syntax.act_def["start-str"]):
                new_token = eval(token)
                new_token_line.append(new_token)
                continue
            if token.startswith(Syntax.act_def["start-arg"]):
                if transform_to_vec3:
                    new_token = self.arguments_to_vec(token)
                else:
                    new_token = eval(token)
                new_token_line.append(new_token)
                continue
            new_token_line.append(token)
        return new_token_line

    def analyze(self):
        for token_line in self.token_content:
            new_token_line: None
            if token_line[0] == Syntax.act_def["molecule"]:
                self.analyze_new_element(token_line, 3)
                new_token_line = self.parse_token(token_line, transform_to_vec3=True)
            
            elif token_line[0] == Syntax.act_def["text"]:
                self.analyze_new_element(token_line, 4)
                new_token_line = self.parse_token(token_line, transform_to_vec3=False)

            else:
                raise SyntaxError(f"{token_line[0]} is not a valid action")
        
        if new_token_line != None: 
            self.parse_content.append(new_token_line)

    def __str__(self):
        return str(self.file_content)
    
def main():
    l = MVReader("scripts/test.mvs")
    l.analyze()
    print(l.parse_content)

if __name__ == '__main__':
    main()
