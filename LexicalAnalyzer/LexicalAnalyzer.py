import string

#input
kalimat = input('Masukkan Token : ')
input_string = kalimat.lower()+'#'

#initialization
listalphabet = list(string.ascii_lowercase)
listState = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',
              'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20',
              'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30',
              'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40',
              'q41', 'q42', 'q43', 'q44', 'q45']

tabelTransisi = {}

for state in listState:
    for alphabet in listalphabet:
        tabelTransisi[(state, alphabet)] = 'error'
    tabelTransisi[(state, '#')] = 'error'
    tabelTransisi[(state, ' ')] = 'error'

# space before input string
tabelTransisi['q0', ' '] = 'q0'

#update the transition table for the following token : pakdhe
tabelTransisi[('q0', 'p')] = 'q1'
tabelTransisi[('q1', 'a')] = 'q2'
tabelTransisi[('q2', 'k')] = 'q3'
tabelTransisi[('q3', 'd')] = 'q4'
tabelTransisi[('q4', 'h')] = 'q5'
tabelTransisi[('q5', 'e')] = 'q44'
tabelTransisi[('q44', '#')] = 'acc'
tabelTransisi[('q44', ' ')] = 'q45'
tabelTransisi[('q45', '#')] = 'acc'

#update the transition table for the following token : latar
tabelTransisi[('q0', 'l')] = 'q6'
tabelTransisi[('q6', 'a')] = 'q7'
tabelTransisi[('q7', 't')] = 'q8'
tabelTransisi[('q8', 'a')] = 'q9'
tabelTransisi[('q9', 'r')] = 'q44'
tabelTransisi[('q44', '#')] = 'acc'
tabelTransisi[('q44', ' ')] = 'q45'
tabelTransisi[('q45', '#')] = 'acc'

#update the transition table for the following token : telo
tabelTransisi[('q0', 't')] = 'q10'
tabelTransisi[('q10', 'e')] = 'q11'
tabelTransisi[('q11', 'l')] = 'q12'
tabelTransisi[('q12', 'o')] = 'q44'
tabelTransisi[('q44', '#')] = 'acc'
tabelTransisi[('q44', ' ')] = 'q45'
tabelTransisi[('q45', '#')] = 'acc'

# update the transition table for the following token: klambi
tabelTransisi[('q0', 'k')] = 'q13'
tabelTransisi[('q13', 'l')] = 'q14'
tabelTransisi[('q14', 'a')] = 'q15'
tabelTransisi[('q15', 'm')] = 'q16'
tabelTransisi[('q16', 'b')] = 'q17'
tabelTransisi[('q17', 'i')] = 'q44'
tabelTransisi[('q44', '#')] = 'acc'
tabelTransisi[('q44', ' ')] = 'q45'
tabelTransisi[('q45', '#')] = 'acc'

# update the transition table for the following token: godhong
tabelTransisi[('q0', 'g')] = 'q20'
tabelTransisi[('q20', 'o')] = 'q21'
tabelTransisi[('q21', 'd')] = 'q22'
tabelTransisi[('q22', 'h')] = 'q23'
tabelTransisi[('q23', 'o')] = 'q24'
tabelTransisi[('q24', 'n')] = 'q25'
tabelTransisi[('q25', 'g')] = 'q44'
tabelTransisi[('q44', '#')] = 'acc'
tabelTransisi[('q44', ' ')] = 'q45'
tabelTransisi[('q45', '#')] = 'acc'

# update the transition table for the following token: budhe
tabelTransisi[('q0', 'b')] = 'q18'
tabelTransisi[('q18', 'u')] = 'q19'
tabelTransisi[('q19', 'd')] = 'q4'
tabelTransisi[('q4', 'h')] = 'q5'
tabelTransisi[('q5', 'e')] = 'q44'
tabelTransisi[('q44', '#')] = 'acc'
tabelTransisi[('q44', ' ')] = 'q45'
tabelTransisi[('q45', '#')] = 'acc'

#update the transition table for the following token : ngetok
tabelTransisi[('q0', 'n')] = 'q26'
tabelTransisi[('q26', 'g')] = 'q27'
tabelTransisi[('q27', 'e')] = 'q28'
tabelTransisi[('q28', 't')] = 'q29'
tabelTransisi[('q29', 'o')] = 'q30'
tabelTransisi[('q30', 'k')] = 'q44'
tabelTransisi[('q44', '#')] = 'acc'
tabelTransisi[('q44', ' ')] = 'q45'
tabelTransisi[('q45', '#')] = 'acc'

#update the transition table for the following token : ngumbahi
tabelTransisi[('q0', 'n')] = 'q26'
tabelTransisi[('q26', 'g')] = 'q27'
tabelTransisi[('q27', 'u')] = 'q31'
tabelTransisi[('q31', 'm')] = 'q32'
tabelTransisi[('q32', 'b')] = 'q33'
tabelTransisi[('q33', 'a')] = 'q34'
tabelTransisi[('q34', 'h')] = 'q35'
tabelTransisi[('q35', 'i')] = 'q44'
tabelTransisi[('q44', '#')] = 'acc'
tabelTransisi[('q44', ' ')] = 'q45'
tabelTransisi[('q45', '#')] = 'acc'

# update the transition table for the following token: dhahar
tabelTransisi[('q0', 'd')] = 'q39'
tabelTransisi[('q39', 'h')] = 'q40'
tabelTransisi[('q40', 'a')] = 'q41'
tabelTransisi[('q41', 'h')] = 'q42'
tabelTransisi[('q42', 'a')] = 'q43'
tabelTransisi[('q43', 'r')] = 'q44'
tabelTransisi[('q44', '#')] = 'acc'
tabelTransisi[('q44', ' ')] = 'q45'
tabelTransisi[('q45', '#')] = 'acc'

# update the transition table for the following token: nyapu
tabelTransisi[('q0', 'n')] = 'q26'
tabelTransisi[('q26', 'y')] = 'q36'
tabelTransisi[('q36', 'a')] = 'q37'
tabelTransisi[('q37', 'p')] = 'q38'
tabelTransisi[('q38', 'u')] = 'q44'
tabelTransisi[('q44', '#')] = 'acc'
tabelTransisi[('q44', ' ')] = 'q45'
tabelTransisi[('q45', '#')] = 'acc'

# transition for new token
tabelTransisi[('q45', 'p')] = 'q1'
tabelTransisi[('q45', 'k')] = 'q13'
tabelTransisi[('q45', 'g')] = 'q20'
tabelTransisi[('q45', 'b')] = 'q18'
tabelTransisi[('q45', 'n')] = 'q26'
tabelTransisi[('q45', 'd')] = 'q39'
tabelTransisi[('q45', 'l')] = 'q6'
tabelTransisi[('q45', 't')] = 'q10'

# analisis lexical
idx = 0
state = 'q0'
token = ''
while state != 'acc':
    char = input_string[idx]
    token += char
    state = tabelTransisi[(state, char)]
    if state == 'q44':
        print('Token Saat Ini : ', token, ', valid')
        token = ''
    if state == 'error':
        print('Error, input token tidak valid')
        break;
    idx = idx + 1


# conclusion
if state == 'acc':
    print('Semua token yang diinput : ', kalimat, ', valid')
