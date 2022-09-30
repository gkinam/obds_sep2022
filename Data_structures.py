# Generating a list of fellow trainees
participants = ['Li-Hsin', 'Nicole', 'Susann', 'Matt', 'Christina', 'Emily', 'Yu', 'Ayesha', 'Judy', 'Felix', 'Dan']

# Copying the list of participants
participants_2 = participants
participants_3 = participants.copy()
participants_3

#Appending a list
participants.append('Andrea')
participants.append('David')
participants_3

#Indexing a list
participants[2]
participants[4]
participants[2:5:2]

#Sorting a list
participants.sort()
participants
participants[2:5]

#Task 7
participants[2][:2]

#Converting a list to a dictionary - iterates over keys, not values
participants_dic = {}
for name in participants:
    if name == 'David' or name == 'Andrea':
        participants_dic[name] = 'trainer'
    else:
        participants_dic[name] = 'trainee'
    print(participants_dic)

#Task 9
# dictionary[name] command also gives the value :)
for name in participants_dic.keys():
    if participants_dic.get(name) == 'trainee':  #dictionary name.get command gives the value of that key
        print(name)
    else:
        pass

#Tuple
participants_tup = ('Li-Hsin', 'Nicole', 'Susann', 'Matt', 'Christina', 'Emily', 'Yu', 'Ayesha', 'Judy', 'Felix', 'Dan')
participants_tup_2 = participants_tup
participants_tup_3 = participants_tup.copy()

participants_tup[2]
participants_tup[4]
participants_tup[2:5:2]

participants_tup.sort()

participants_tup[2][:2]

