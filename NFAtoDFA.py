# Taking Input (value of M) from user

#Taking value of Q:
Q = []
stop = ','
while(stop != '.'):
    stop = input('Enter the states(\'.\' to end): ')
    if stop != '.' and stop not in Q:
        Q.append(stop)
print('List of states(Q): ', end='')
print(Q)
print()


#Taking values of F:
F = []
stop = ','
while(stop != '.'):
    stop = input('Enter the final state(s)(\'.\' to end): ')
    if(stop != '.' and stop not in F):
        if stop in Q:
            F.append(stop)
        else:
            print(f'{stop} is not in the list of states..')
print('List of final state(s)(F): ', end='')
print(F)
print()


#Taking values of sigma:
sigma = ['eps']
stop = ','
while(stop != '.'):
    stop = input('Enter the symbols(other than epsilon, \'.\' to end): ')
    if(stop != '.' and stop not in sigma):
        sigma.append(stop)
print('List of symbols(sigma): ', end='')
print(sigma)
print()


#Taking the value of beginning state(q0):
q0 = ''
while (q0 == ''):
    q = input('Enter the beginning state(q0): ')
    if q in Q:
        q0 = q
    else:
        print(f'{q} is not in the list of states..')
print('Beginning state(q0): ', end='')
print(q0)
print()


#Taking the values of delta function:
table = {}

for i in Q:
    rows = {}
    for j in sigma:
        rows[j] = []
    table[i] = rows

print('Enter the values of transition function (\'.\' to procced to next): ')
for i in Q:
    for j in sigma:
        stop = ','
        while(stop != '.'):
            stop = input(f"delta({i},{j}) = ")
            if(stop != '.' and stop not in table[i][j]):
                if stop in Q:
                    table[i][j].append(stop)
                else:
                    print(f'{stop} is not in the list of states..')
        print()

#print(table)

#All the inputs have been taken


#Finding the corresponding DFA:
print()
print('***** CORRESPONDING DFA *****')
print()
# Finding the epsilon closure:
eps_clos = {}
for i in Q:
    eps_clos[i] = [i]

for i in Q:
    for j in eps_clos[i]:
        for k in table[j]['eps']:
            if k not in eps_clos[i]:
                eps_clos[i].append(k)

#Printing the epsilon closure:
for i in eps_clos:
    print(f"Epsilon closure of '{i}' : {eps_clos[i]}")
print()


#Finding the states of DFA:
Q_dfa = []
Q_dfa.append(eps_clos[q0])

for i in Q_dfa:
    for k in sigma:
        curr = []
        for j in i:
            for l in table[j][k]:
                if l not in curr:
                    curr.append(l)
        a = 1
        for x in Q_dfa:
            p = 0
            for y in curr:
                if y in x:
                    p+=1
            if p == len(curr):
                if len(x) == p:
                    a = 0
        if a == 1 and len(curr) != 0:
            Q_dfa.append(curr)

        #if curr not in Q_dfa and len(curr) != 0:
            

#Printing the states of DFA:
print('States of DFA: ', end='')
print(Q_dfa)
print()


# Sigma of DFA
sigma_dfa = []

for i in sigma:
    if i != 'eps':
        sigma_dfa.append(i)

print('Sigma of DFA :', end='')
print(sigma_dfa)
print()


#Beginning state of DFA:
q0_dfa = eps_clos[q0]
print('Beginning state of DFA:', end='')
print(q0_dfa)
print()


#Final state of DFA:
F_dfa = []
for i in Q_dfa:
    for j in F:
        if j in i:
            F_dfa.append(i)

print('List of final state of DFA:', end='')
print(F_dfa)
print('')


#Finding the transition state table for DFA:
table_dfa = {}

for i in range(len(Q_dfa)):
    rows_dfa = {}
    for j in sigma_dfa:
        rows_dfa[j] = []
    table_dfa[i] = rows_dfa



for i,m in zip(Q_dfa,range(len(Q_dfa))):
    for k in sigma_dfa:
        curr = []
        for j in i:
            for l in table[j][k]:
                if l not in curr:
                    curr.append(l)
        table_dfa[m][k] = curr


#Printing the transition state table for DFA:
print()
for i in range(-1, len(Q_dfa)):
    if i==-1:
        print("{:<25}".format(str('States')), end = '')
    else:
        print("{:<25}".format(str(Q_dfa[i])), end= '')
    for j in sigma_dfa:
        if i==-1:
            print("{:<25}".format(str(j)), end = '')
        else:
            print("{:<25}".format(str(table_dfa[i][j])), end = '')
    print()

            
