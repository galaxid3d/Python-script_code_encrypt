# 30.08.2023 by galaxid3d
# encrypt (without recovery) file/string code, replace all symbols with special (save reserved keywords)

# special symbols replacers - you can edit this
SYMBOLS_REPLACERS = {"upper": 'A', "lower": 'a', "number": '?', "other": '#'}

# END OF CONSTANTS SECTION

# global keywords for all code languages
GLOBAL_KEYWORDS = [" ", "_", "-", "+", "*", "/", "=", "'", '"', "!", "@", "$", "%", "^", "&", "(", ")", "{", "}",
                   "[", "]", ":", ";", "<", ">", ",", ".", "~", "\\", "|", "\t", "\n"]

# Delphi keywords
DELPHI_KEYWORDS = ["absolute", "abstract", "and", "array", "as", "asm", "assembler", "automated", "begin", "case",
                   "cdecl", "class", "const", "constructor", "destructor", "dispid", "dispinterface", "div", "do",
                   "downto", "dynamic", "else", "end", "except", "export", "exports", "external", "far", "file",
                   "finalization", "finally", "for", "forward", "function", "goto", "if", "implementation",
                   "implements", "in", "index", "inherited", "initialization", "inline", "interface", "is", "label",
                   "library", "message", "mod", "name", "near", "nil", "not", "object", "of", "on", "or", "out",
                   "overload", "override", "package", "packed", "pascal", "private", "procedure", "program", "property",
                   "protected", "public", "published", "raise", "record", "register", "reintroduce", "repeat",
                   "resourcestring", "safecall", "set", "shl", "shr", "stdcall", "string", "then", "threadvar", "to",
                   "try", "type", "unit", "until", "uses", "var", "virtual", "while", "with", "xor"]
DELPHI_FILE_TYPES = ["*.pas"]
DELPHI_FILE_CODEC = "cp1251"

# Java keywords
JAVA_KEYWORDS = ["abstract", "assert", "boolean", "break", "byte", "case", "catch", "char", "class", "const", "continue",
                 "default", "do", "double", "else", "enum", "extends", "final", "finally", "float", "for", "goto", "if",
                 "implements", "import", "instanceof", "int", "interface", "long", "native", "new", "package", "private",
                 "protected", "public", "return", "short", "static", "super", "switch", "synchronized", "this", "throw",
                 "throws", "transient", "try", "void", "volatile", "while"]
JAVA_FILE_TYPES = ["*.java"]
JAVA_FILE_CODEC = "utf-8"

# MAXScript keywords
MAXSCRIPT_KEYWORDS = ["about", "and", "animate", "as", "at", "attributes", "by", "case", "catch", "collect", "continue",
                      "coordsys", "do", "else", "exit", "false", "fn", "for", "from", "function", "global", "if", "in",
                      "local", "macroscript", "mapped", "max", "not", "of", "off", "on", "or", "parameters",
                      "persistent", "plugin", "rcmenu", "return", "rollout", "set", "struct", "then", "throw", "to",
                      "tool", "true", "try", "undefined", "undo", "utility", "when", "where", "while", "with"]
MAXSCRIPT_FILE_TYPES = ["*.ms", "*.mcr"]
MAXSCRIPT_FILE_CODEC = "utf-8"

# Python keywords
PYTHON_KEYWORDS = ["False", "None", "True", "and", "as", "assert", "async", "await", "break", "class", "continue",
                   "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import", "in",
                   "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"]
PYTHON_FILE_TYPES = ["*.py"]
PYTHON_FILE_CODEC = "utf-8"

def convert_code_word_to_encrypt(code_word, keywords):
    if code_word in keywords:
        return code_word
    result = ""
    for symbol in code_word:
        if symbol.isupper():
            result += SYMBOLS_REPLACERS["upper"] if SYMBOLS_REPLACERS["upper"] else SYMBOLS_REPLACERS["other"]
        elif symbol.islower():
            result += SYMBOLS_REPLACERS["lower"] if SYMBOLS_REPLACERS["lower"] else SYMBOLS_REPLACERS["other"]
        elif symbol.isdigit():
            result += SYMBOLS_REPLACERS["number"] if SYMBOLS_REPLACERS["number"] else SYMBOLS_REPLACERS["other"]
        else:
            result += SYMBOLS_REPLACERS["other"]
    return result

def convert_code_string_to_encrypt(code_string, keywords):
    result = []
    code_string_lst = code_string.split(" ")

    for word in code_string_lst:
        current_word = ""
        word_tmp_str = ""
        if word in keywords:
            current_word = word
        else:
            for symbol in word:
                if symbol in keywords:
                    current_word += convert_code_word_to_encrypt(word_tmp_str, keywords) + symbol
                    word_tmp_str = ""
                else:
                    word_tmp_str += symbol
            current_word += convert_code_word_to_encrypt(word_tmp_str, keywords)
        result.append(current_word)

    return " ".join(result)

# user select keywords for reserved
user_select_keywords = GLOBAL_KEYWORDS
user_select_file_types = []
user_select_file_codec = ""
print("Выбирите для какого языка программирования "
                   "зарезервировать ключевые слова:\n\t1. Delphi\n\t2. Java\n\t3. MAXScript\n\t4. Python")
user_input = input("Ввод: ")
if user_input == "1":
    user_select_keywords += DELPHI_KEYWORDS
    user_select_file_types = DELPHI_FILE_TYPES
    user_select_file_codec = DELPHI_FILE_CODEC
elif user_input == "2":
    user_select_keywords += JAVA_KEYWORDS
    user_select_file_types = JAVA_FILE_TYPES
    user_select_file_codec = JAVA_FILE_CODEC
elif user_input == "3":
    user_select_keywords += MAXSCRIPT_KEYWORDS
    user_select_file_types = MAXSCRIPT_FILE_TYPES
    user_select_file_codec = MAXSCRIPT_FILE_CODEC
elif user_input == "4":
    user_select_keywords += PYTHON_KEYWORDS
    user_select_file_types = PYTHON_FILE_TYPES
    user_select_file_codec = PYTHON_FILE_CODEC

# original string line for encrypting
print("Выберите один из вариантов того, что необходимо закодировать:\n\t1. Текстова строка\n\t2. Файл с кодом script.txt\n\t3. Папка с файлами scripts")
script_code_line = input("Ввод: ")
if script_code_line == "1":
    script_code_line = input("Введите строку: ")

    # string of result encrypting
    script_code_line_encrypt = convert_code_string_to_encrypt(script_code_line, user_select_keywords)

    print(script_code_line)
    print(script_code_line_encrypt)
    input("Для завершения нажмите любую кнопку...")
elif script_code_line == "2":
    import os.path
    if os.path.exists("script.txt"):
        try:
            script_file_encrypt = open("script_encrypt.txt", mode="w", encoding=user_select_file_codec)
            with open("script.txt", mode="r", encoding=user_select_file_codec) as script_file:
                for script_code_line in script_file:
                    script_code_line_encrypt = convert_code_string_to_encrypt(script_code_line, user_select_keywords)
                    script_file_encrypt.write(script_code_line_encrypt)
        finally:
            script_file_encrypt.close()
elif script_code_line == "3":
    import os
    if os.path.exists("scripts"):
        if not os.path.isdir("scripts_encrypt"):
            os.mkdir("scripts_encrypt")
        from pathlib import Path
        for file_type in user_select_file_types:
            for file_with_code in Path("scripts/").rglob(file_type):
                # make directories
                if "\\" in str(file_with_code):
                    new_path = "scripts_encrypt"+str(file_with_code)[7:str(file_with_code).rfind("\\")]
                    if not os.path.isdir(new_path):
                        os.makedirs(new_path)
                try:
                    script_file_encrypt = open("scripts_encrypt"+str(file_with_code)[7:], mode='w', encoding=user_select_file_codec)
                    with open(str(file_with_code), mode="r", encoding=user_select_file_codec) as script_file:
                        for script_code_line in script_file:
                            script_code_line_encrypt = convert_code_string_to_encrypt(script_code_line,
                                                                                      user_select_keywords)
                            script_file_encrypt.write(script_code_line_encrypt)
                finally:
                    script_file_encrypt.close()
