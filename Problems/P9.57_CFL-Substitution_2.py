# Problem 9.57, Page 246 — CFL-Substitution
# Label: exr:cfl-substitution
# An Introduction to the Analysis of Algorithms (4th Edition)

import random

# ">" corresponds to an input state, the following integers correspond to a
# transition based on 0, 1 input, the final number is a State Number.
# "*" corresponds to a final state
def read_transition_file():
    transition_table = open("transition.txt", "r")
    lines = transition_table.readlines()
    transition_table.close()

    state_list = []
    table = {}

    for line in lines:
        state_list.append(line.rstrip('\n').split('|'))

    for entry in state_list:
        for x in range(1, 3):
            entry[x] = 'q' + entry[x]
        table['q' + entry[3]] = entry

    return table

def print_table(t_table):
    for item in t_table:
        if t_table.get(item)[0] == ">":
            print("%s|  %s %s : %s" % (item, t_table.get(item)[0], t_table.get(item)[1], t_table.get(item)[2]))
        elif t_table.get(item)[0] == "*":
            print("%s|  %s %s : %s" % (item, t_table.get(item)[0], t_table.get(item)[1], t_table.get(item)[2]))
        else:
            print("%s|    %s : %s" % (item, t_table.get(item)[1], t_table.get(item)[2]))

def distinguishable(test_group, final):

    while test_group:
        test_a = {}
        sample_state = random.choice(list(test_group.keys()))
        test_a[sample_state] = test_group.pop(sample_state)
        poppable_states = []

        for item in test_a:
            for states in test_group:
                if test_a[item][1] == test_group[states][1] and test_a[item][2] == test_group[states][2]:
                    print("states are indistinguishable:")
                    print(test_a[item])
                    print(test_group[states])

                    poppable_states.append(states)
                    for entry in test_group:
                        if test_group.get(entry)[1] == states:
                            test_group[entry][1] = item
                        if test_group.get(entry)[2] == states:
                            test_group[entry][2] = item

            for pops in poppable_states:
                print("Popping indistinguishable state: %s" % (pops))
                test_group.pop(pops)
        final[item] = test_a.pop(item)

    poppable_entries = []
    for state in final:
        for entry in final:
            if state != entry:
                if final[state][1] == entry and final[entry][1] == state and final[entry][2] == final[state][2]:
                    if state not in poppable_entries:
                        poppable_entries.append(entry)
                        if final[state][1] == entry:
                            final[state][1] = state
                        if final[state][2] == entry:
                            final[state][2] = state
                if final[state][2] == entry and final[entry][2] == state and final[entry][1] == final[state][1]:
                    if state not in poppable_entries:
                        poppable_entries.append(entry)

    for pops in poppable_entries:
        print("Popping indistinguishable state: %s" % (pops))
        final.pop(pops)

    return final

t_table = read_transition_file()
print_table(t_table)

final = {}
non_final = {}

for items in t_table:
    if t_table.get(items)[0] == "*":
        final[items] = t_table.get(items)
    else:
        non_final[items] = t_table.get(items)

dfa_min = distinguishable(non_final, final)

print_table(dfa_min)
