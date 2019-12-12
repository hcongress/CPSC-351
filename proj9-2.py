import argparse

#Hunter Congress
#proi9-2
#python: 3.6.8
def simulate(DFA,w):
    currentState = DFA[3]

    for symbol in w:
        if currentState not in DFA[0] or symbol not in DFA[1]:
            return 'symbol or state not found'
        else:
            for nextState in DFA[2]:
                if nextState[0] == currentState and nextState[1] == symbol:
                    currentState = nextState[2]
                    break
                    
    if currentState in DFA[4]:
        return 'ACCEPT'
    else:
        return 'REJECT'



ap = argparse.ArgumentParser()

ap.add_argument(
    'file',
    type=str,
    help='Please specify the file'
)

args = ap.parse_args()

with open(args.file) as fp:
    line=fp.readline()
    line = line.strip('\n')
    states = line.split(",")
    
    line = fp.readline()
    line = line.strip('\n')
    symbols = line.split(',')

    line=fp.readline()
    line = line.strip('\n')
    l = line.split(",")
    transitions = []
    for state in l:
        transitions.append(state.split('-'))


    
    line=fp.readline()
    startState = line.strip('\n')

    line= fp.readline()
    line.strip('\n')
    acceptState = line.split(',')

    DFA = [states,symbols,transitions,startState,acceptState]


while(True):
    w= input("Enter string: ")
    results = simulate(DFA,w)
    print(results)


