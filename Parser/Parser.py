#input
sentence = input('Masukkan kalimat : ')
tokens = sentence.lower().split()
tokens.append('EOS')

#symbol
non_terminals = ['S','NN','VB']
terminals = ['pakdhe','budhe','klambi','telo','latar','ngetok','nyapu','ngumbahi','dhahar','godhong']

#parse table
parse_table ={}

parse_table[('S', 'pakdhe')] = ['NN','VB','NN']
parse_table[('S', 'budhe')] = ['NN','VB','NN']
parse_table[('S', 'klambi')] = ['NN','VB','NN']
parse_table[('S', 'telo')] = ['NN','VB','NN']
parse_table[('S', 'latar')] = ['NN','VB','NN']
parse_table[('S', 'godhong')] = ['NN','VB','NN']
parse_table[('S', 'nyapu')] = ['error']
parse_table[('S', 'ngumbahi')] = ['error']
parse_table[('S', 'dhahar')] = ['error']
parse_table[('S', 'ngetok')] = ['error']
parse_table[('S', 'EOS')] = ['error']

parse_table[('NN', 'pakdhe')] = ['pakdhe']
parse_table[('NN', 'budhe')] = ['budhe']
parse_table[('NN', 'klambi')] = ['klambi']
parse_table[('NN', 'telo')] = ['telo']
parse_table[('NN', 'latar')] = ['latar']
parse_table[('NN', 'godhong')] = ['godhong']
parse_table[('NN', 'nyapu')] = ['error']
parse_table[('NN', 'ngumbahi')] = ['error']
parse_table[('NN', 'dhahar')] = ['error']
parse_table[('NN', 'ngetok')] = ['error']
parse_table[('NN', 'EOS')] = ['error']

parse_table[('VB', 'pakdhe')] = ['error']
parse_table[('VB', 'budhe')] = ['error']
parse_table[('VB', 'klambi')] = ['error']
parse_table[('VB', 'telo')] = ['error']
parse_table[('VB', 'latar')] = ['error']
parse_table[('VB', 'godhong')] = ['error']
parse_table[('VB', 'nyapu')] = ['nyapu']
parse_table[('VB', 'ngumbahi')] = ['ngumbahi']
parse_table[('VB', 'dhahar')] = ['dhahar']
parse_table[('VB', 'ngetok')] = ['ngetok']
parse_table[('NN', 'EOS')] = ['error']

# stack initialization
stack = []
stack.append('#')
stack.append('S')

# input reading initialization
idx_token = 0
symbol = tokens[idx_token]

# parsing process
while (len(stack) > 0):
    top = stack [len(stack) - 1]
    print('Top = ', top)
    print('Symbol = ', symbol)
    if top in terminals:
        print('Top adalah simbol terminal')
        if top == symbol:
            stack.pop()
            idx_token = idx_token + 1
            symbol = tokens[idx_token]
            if symbol == 'EOS':
                print('Isi stack: ', stack)
                stack.pop()

        else:
            print('error')
            break;
    elif top in non_terminals:
        print('Top adalah simbol non-terminal')
        if parse_table[(top, symbol)][0] != 'error':
            stack.pop()
            symbols_to_be_pushed = parse_table[(top, symbol)]
            for i in range(len(symbols_to_be_pushed)-1,-1,-1):
                stack.append(symbols_to_be_pushed[i])
        else:
            print('Error')
            break;
    else:
        print('Error')
        break;
    print('Isi stack: ', stack)
    print()

# conclusion
print()
if symbol == 'EOS' and len(stack) == 0:
    print('Input string ', sentence, ' diterima, sesuai Grammar')
else:
    print('Error, input string: ', sentence, ', tidak diterima, tidak sesuai Grammar')

