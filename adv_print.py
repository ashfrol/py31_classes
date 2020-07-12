

def adv_print(*args, **kwargs):
    sep = kwargs['sep']
    end = kwargs['end']
    start = ''
    for item in kwargs.items():
        if 'start' in item:
            start = kwargs['start']
        if 'max_line' in item:
            max_line = kwargs['max_line']
        else:
            max_line = False
        if 'in_file' in item:
            in_file = kwargs['in_file']
        else:
            in_file = False

    text_list = [start]
    [text_list.append(item) for item in args]
    text_list.append(end)
    final_text = sep.join(text_list)
    print(text_list)
    if max_line:
        for i in range(0, len(final_text), max_line):
            print(final_text[i:i+max_line])
    if in_file:
        filename = f'{final_text.strip()[:5]}.txt'
        with open(filename, 'w', encoding='utf-8') as file_write:
            [file_write.write(line) for line in final_text]


adv_print('Hello', 'world', sep=' ', end='\n', start='Hi', max_line=10)