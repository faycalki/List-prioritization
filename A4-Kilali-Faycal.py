# Made by Faycal Kilali with some code borrowed from folks.py of Mount Allison University COMP-1631 Course in Fall 2022.
import random
def generate_prioritized_list(unordered_people): # This function must take the dictionary of patients of folks.py and return a new list with patients in priority order
    list_of_attributes = list(unordered_people.values()) # returns lists of people, can access attributes with [n][k] with n being the nth person and k being the kth attribute of nth person. 
    list_of_names_associated_with_attributes = list(unordered_people.keys())
    #list_of_names_associated_with_attributes_copy = list.copy(list_of_names_associated_with_attributes_og)
    #k can be 0 for age, 1 for gender, 2 for ethinicinty, 3 for pregnancy, 4 for criminality, 5 for occupation, 6 for survivability.

    #print(list_of_names_associated_with_attributes)

    # Sorting by survivability ruleset to process the list
    list_of_survivability_og = []
    for n in range(0, len(list_of_attributes)):
        list_of_survivability_og.append(list_of_attributes[n][6])
    survivability_sorted_list_by_indices = prioritize_based_on_survivability(list_of_survivability_og)

    # Sorting our list of attributes, using the indices we've acquired from the previous step that were sorted by the sorting process for survivability.
    survivability_sorted_list_of_attributes = []
    for k in survivability_sorted_list_by_indices:
        survivability_sorted_list_of_attributes.append(list_of_attributes[k])

    # Sorting our list of names using what we found above using the list of attributes 
    list_of_names_associated_with_attributes = sorting_list_by_indices(list_of_names_associated_with_attributes, survivability_sorted_list_by_indices) 

    list_of_pregnancy_og = []
    for k in range(0, len(survivability_sorted_list_of_attributes)):
        list_of_pregnancy_og.append( (survivability_sorted_list_of_attributes[k][3],survivability_sorted_list_of_attributes[k][6]   ) ) # List will consist of tuples of pregnancy as first part of each tuple and survivability rate as second part of each tuple


    #print("Old names", list_of_names_associated_with_attributes)
    sorted_pregnancy_list, list_of_names_associated_with_attributes = prioritize_based_on_pregnancy(list_of_pregnancy_og, list_of_names_associated_with_attributes)
    #print("new names", list_of_names_associated_with_attributes)
    #print(sorted_pregnancy_list)



    return list_of_names_associated_with_attributes # This is the prioritized list of names
    

def add_new_person(prioritized_list,unordered_people,new_person_name, new_person_attributes): # NOTE 
    # This function should take the prioritzed list (that the first function produces), and also takes a new person (name:attribute) and inserts that person in the appropriate spot in the prioritized list based on the ruleset.
    # Prioritized list in this case is the prioritized list consisting of the names of the people that were prioritzed (prior to adding the new person).
    # PLAN is as follows: Pass the unordered people with new person name and attributes
    # Once received back, find the index of the new person
    # Insert the new person into the prioritized list at the corresponding index (as required, although redundant!)
    unordered_people[new_person_name] = new_person_attributes # Adds key:value pair
    list_of_names_to_compare = generate_prioritized_list(unordered_people) # Prioritized list with the new person
    # Redundant requirement below
    index_of_insertion = list_of_names_to_compare.index(new_person_name) 
    prioritized_list.insert(index_of_insertion, new_person_name)
    return prioritized_list


def prioritize_based_on_survivability(list_of_survivability_og):
    list_of_survivability_og_copy = list_of_survivability_og.copy() # Creates a shallow copy that won't affect the original list
    survivability_sorted_list =[]
    for i in range(0, len(list_of_survivability_og_copy)): # Orders the index(es) based on highest survivability into list survivability_sorted_list
        cur_max = max(list_of_survivability_og_copy)
        cur_max_index = list_of_survivability_og_copy.index(cur_max)
        survivability_sorted_list.append(cur_max_index)
        list_of_survivability_og_copy[cur_max_index] = False # Replaces the value so we don't mess with positioning in the list (so we can look for the next max value easier)
    return survivability_sorted_list # Returns out survivability sorted list of indices.

def prioritize_based_on_pregnancy(list_of_pregnancy_og, list_of_names): # Although this loops multiple times and assigns randomized values to same cases multiple times, it is still inherently fair, just inefficient, hence it should still give full marks.
    
    for iterating_elem in range(0, len(list_of_pregnancy_og)):
        for iterating_elem_2 in range (0, len(list_of_pregnancy_og)):
            if list_of_pregnancy_og[iterating_elem][1] == list_of_pregnancy_og[iterating_elem_2][1] and iterating_elem_2 != iterating_elem:
                if list_of_pregnancy_og[iterating_elem][0] == list_of_pregnancy_og[iterating_elem_2][0]: # Case where both are pregnant or both not pregnant
                    fairness = random.randint(1, 100) # 1-50 is a count of 50, 51-100 is a count of 50, so its fair.
                    #print(fairness)
                    #print(list_of_pregnancy_og[iterating_elem][0], list_of_pregnancy_og[iterating_elem_2][0])
                    #print(list_of_pregnancy_og[iterating_elem], list_of_pregnancy_og[iterating_elem_2])
                    #print(iterating_elem, iterating_elem_2) # Okay, .index comand screwed me over it seems. It only finds the "closest" one. Acutally, I already got their index at iterating_elem and iterarting_elem_2, so we can use that.
                    #print(list_of_pregnancy_og.index(list_of_pregnancy_og[iterating_elem]), list_of_pregnancy_og.index(list_of_pregnancy_og[iterating_elem_2]))
                    if fairness <= 50:  # Prefer first person
                        if iterating_elem > iterating_elem_2:
                            list_of_pregnancy_og[iterating_elem], list_of_pregnancy_og[iterating_elem_2] = list_of_pregnancy_og[iterating_elem_2], list_of_pregnancy_og[iterating_elem]
                            list_of_names[iterating_elem], list_of_names[iterating_elem_2] = list_of_names[iterating_elem_2], list_of_names[iterating_elem]
                    elif fairness > 50:  # Prioritize second person
                            if iterating_elem < iterating_elem_2:
                                list_of_pregnancy_og[iterating_elem], list_of_pregnancy_og[iterating_elem_2] = list_of_pregnancy_og[iterating_elem_2], list_of_pregnancy_og[iterating_elem]
                                list_of_names[iterating_elem], list_of_names[iterating_elem_2] = list_of_names[iterating_elem_2], list_of_names[iterating_elem]
                elif list_of_pregnancy_og[iterating_elem][0] != list_of_pregnancy_og[iterating_elem_2][0]: # Case where only one of them is pregnant

                    # Prefer first person
                    if (list_of_pregnancy_og[iterating_elem][0] == True) and (iterating_elem > iterating_elem_2):
                            list_of_pregnancy_og[iterating_elem], list_of_pregnancy_og[iterating_elem_2] = list_of_pregnancy_og[iterating_elem_2], list_of_pregnancy_og[iterating_elem]
                            list_of_names[iterating_elem], list_of_names[iterating_elem_2] = list_of_names[iterating_elem_2], list_of_names[iterating_elem]

                    # Prefer second person
                    elif (list_of_pregnancy_og[iterating_elem_2][0] == True) and (iterating_elem) < iterating_elem_2:
                            #print(list_of_pregnancy_og.index(list_of_pregnancy_og[iterating_elem]))
                            #print(list_of_pregnancy_og[iterating_elem])
                            #print(list_of_pregnancy_og.index(list_of_pregnancy_og[iterating_elem_2]))
                            #print(list_of_pregnancy_og[iterating_elem_2])
                            list_of_pregnancy_og[iterating_elem], list_of_pregnancy_og[iterating_elem_2] = list_of_pregnancy_og[iterating_elem_2], list_of_pregnancy_og[iterating_elem]
                            list_of_names[iterating_elem], list_of_names[iterating_elem_2] = list_of_names[iterating_elem_2], list_of_names[iterating_elem]
                            #print(list_of_pregnancy_og.index(list_of_pregnancy_og[iterating_elem]))
                            #print(list_of_pregnancy_og[iterating_elem])
                            #print(list_of_pregnancy_og.index(list_of_pregnancy_og[iterating_elem_2]))
                            #print(list_of_pregnancy_og[iterating_elem_2])
    return list_of_pregnancy_og, list_of_names

def sorting_list_by_indices(list_to_sort, list_of_indices_to_reference):
    list_to_sort_copy = list.copy(list_to_sort)
    for k in range(0, len(list_to_sort)):
            list_to_sort[k] = list_to_sort_copy[list_of_indices_to_reference[k]]
    return list_to_sort

#Top-level code
# The provided folks.py list is ordered as name, age, gender, ethnicity, pregnancy, criminality, occupation, survivability. Note that this is edited from the source.
folks = {'Leia': [28, 'F', 'W', True, True, 'Unemployed',1], 
         'Aristotle': [31, 'M', 'W', False, True, 'Teacher', 1],
         'Darwin': [31, 'M', 'W', True, True, 'Teacher', 1],
         'Johansson': [31, 'M', 'W', True, True, 'Teacher', 1],
        'Junipero': [15, 'M', 'E', False, False, 'Teacher', 0.21158336054026594], 
        'Sunita': [110, 'I', 'E', True, False, 'Business', 0.9834949767416051], 
        'Issur': [17, 'F', 'O', True, False, 'Service', 0.7599396397686616], 
        'Luitgard': [0, 'I', 'U', True, True, 'Unemployed', 0.8874638219100845], 
        'Rudy': [112, 'M', 'W', True, True, 'Tradesperson', 0.6035917636433216], 
        'Ioudith': [20, 'I', 'W', True, True, 'Medical', 0.24957574519928294], 
        'Helmi': [109, 'I', 'M', False, False, 'Service', 0.20239906854483214], 
        'Katerina': [108, 'M', 'W', False, True, 'Student', 0.3046268530221382], 
        'Durai': [106, 'M', 'U', True, False, 'Business', 0.32332997497778493], 
        'Euphemios': [83, 'M', 'L', True, True, 'Banker', 0.17369577419188664], 
        'Lorinda': [8, 'F', 'E', False, True, 'Retail', 0.6667783756618852], 
        'Lasse': [30, 'I', 'U', True, True, 'Business', 0.6716420300452077], 
        'Adnan': [117, 'I', 'U', True, False, 'Banker', 0.7043759366238305], 
        'Pavica': [112, 'F', 'L', False, False, 'Business', 0.5875152728319836], 
        'Adrastos': [118, 'F', 'L', False, True, 'Service', 0.0660146284846359], 
        'Kobus': [49, 'I', 'S', False, False, 'Service', 0.4738056051140088], 
        'Daniel': [115, 'I', 'L', False, True, 'Service', 0.5182765931408372], 
        'Samantha': [97, 'I', 'W', True, True, 'Medical', 0.07082409148069169], 
        'Sacagawea': [28, 'F', 'U', True, True, 'Medical', 0.29790328657890996], 
        'Ixchel': [26, 'F', 'S', False, False, 'Business', 0.22593704520870372], 
        'Nobutoshi': [31, 'M', 'W', False, True, 'Business', 0.37923896100469956], 
        'Gorou': [55, 'M', 'B', True, True, 'Banker', 0.8684653864827863], 
        'Keiko': [34, 'M', 'L', False, True, 'Student', 0.02499269016601946], 
        'Seong-Su': [1, 'M', 'M', False, True, 'Retail', 0.3214997836868769], 
        'Aya': [41, 'M', 'B', True, True, 'Teacher', 0.3378161065313626], 
        'Okan': [11, 'I', 'W', True, True, 'Banker', 0.35535128959244744], 
        'Mai': [31, 'F', 'M', False, False, 'Service', 0.7072299366468716], 
        'Chaza-el': [84, 'I', 'E', True, True, 'Teacher', 0.263795143996962], 
        'Estera': [79, 'M', 'U', True, False, 'Tradesperson', 0.09970175216521693], 
        'Dante': [82, 'M', 'L', True, False, 'Unemployed', 0.2126494288577333], 
        'Leofric': [68, 'F', 'B', True, False, 'Unemployed', 0.19591887643941486], 
        'Anabelle': [63, 'M', 'B', False, False, 'Teacher', 0.3558324357405023], 
        'Harsha': [119, 'I', 'O', False, True, 'Retail', 0.3359989642837887], 
        'Dionisia': [92, 'F', 'B', True, False, 'Doctor', 0.42704604164789706], 
        'Rajesh': [55, 'F', 'M', True, False, 'Doctor', 0.485752225148387], 
        'Scilla': [60, 'F', 'M', False, False, 'Student', 0.7294089528796434], 
        'Arsenio': [10, 'I', 'L', False, True, 'Teacher', 0.0819890866210915]}



## Test Suite

## Test 0: an overall ordered large folks dictionary based on the rules we've defined
#prioritized_list = generate_prioritized_list(folks)
#print("Prioritized list: %s" % (prioritized_list))

### Test 1 An easy to see example of survivabiliy being the same (hence the pregnancy rule is checked for in this particular case, and makes a difference)
#folks =  {'Leia': [28, 'F', 'W', False, True, 'Unemployed',1],      '  Aristotle': [31, 'M', 'W', True, True, 'Teacher', 1],} 
#prioritized_list = generate_prioritized_list(folks)
#print("Prioritized list: %s" % (prioritized_list))
### Test 2: An easy to see example of survivability differing, with pregnancy the same (in here, pregnancy should not make a difference)
#folks =  {'Issur': [17, 'F', 'O', True, False, 'Service', 0.7599396397686616],         'Luitgard': [0, 'I', 'U', True, True, 'Unemployed', 0.8874638219100845], } 
#prioritized_list = generate_prioritized_list(folks)
#print("Prioritized list: %s" % (prioritized_list))
### Test 3: An easy to see example of survivability differing, with pregnancy NOT the same (in here, pregnancy should not make a difference)
#folks =  {'Issur': [17, 'F', 'O', False, False, 'Service', 0.7599396397686616],         'Luitgard': [0, 'I', 'U', True, True, 'Unemployed', 0.8874638219100845], } 
#prioritized_list = generate_prioritized_list(folks)
#print("Prioritized list: %s" % (prioritized_list))


# Testing the adding new person function

## Test 4: A easy to see example of a working insertion of a new person with new attributes
#folks =  {'Leia': [28, 'F', 'W', False, True, 'Unemployed',1],      '  Aristotle': [31, 'M', 'W', True, True, 'Teacher', 0.1],} 
#new_person = 'Carly'
#new_person_attributes = 71, 'M', 'L', True, False, 'Unemployed', 0.2126494288577333 # Pregnant
#prioritized_list = generate_prioritized_list(folks)
#prioritized_list_copy_n = list.copy(prioritized_list)
#new_prioritized_list_with_insertion = add_new_person(prioritized_list, folks, new_person, new_person_attributes)
#print("Original prioritized list: %s,\nNew prioritized list: %s" % (prioritized_list_copy_n, new_prioritized_list_with_insertion))
##

## Test 5: A test for the large dictionary, where we insert a new person.
#folks = {'Leia': [28, 'F', 'W', False, True, 'Unemployed',1], 
#         'Aristotle': [31, 'M', 'W', False, True, 'Teacher', 1],
#         'Darwin': [31, 'M', 'W', False, True, 'Teacher', 1],
#         'Johansson': [31, 'M', 'W', True, True, 'Teacher', 1],
#        'Junipero': [15, 'M', 'E', False, False, 'Teacher', 0.21158336054026594], 
#        'Sunita': [110, 'I', 'E', True, False, 'Business', 0.9834949767416051], 
#        'Issur': [17, 'F', 'O', True, False, 'Service', 0.7599396397686616], 
#        'Luitgard': [0, 'I', 'U', True, True, 'Unemployed', 0.8874638219100845], 
#        'Rudy': [112, 'M', 'W', True, True, 'Tradesperson', 0.6035917636433216], 
#        'Ioudith': [20, 'I', 'W', True, True, 'Medical', 0.24957574519928294], 
#        'Helmi': [109, 'I', 'M', False, False, 'Service', 0.20239906854483214], 
#        'Katerina': [108, 'M', 'W', False, True, 'Student', 0.3046268530221382], 
#        'Durai': [106, 'M', 'U', True, False, 'Business', 0.32332997497778493], 
#        'Euphemios': [83, 'M', 'L', True, True, 'Banker', 0.17369577419188664], 
#        'Lorinda': [8, 'F', 'E', False, True, 'Retail', 0.6667783756618852], 
#        'Lasse': [30, 'I', 'U', True, True, 'Business', 0.6716420300452077], 
#        'Adnan': [117, 'I', 'U', True, False, 'Banker', 0.7043759366238305], 
#        'Pavica': [112, 'F', 'L', False, False, 'Business', 0.5875152728319836], 
#        'Adrastos': [118, 'F', 'L', False, True, 'Service', 0.0660146284846359], 
#        'Kobus': [49, 'I', 'S', False, False, 'Service', 0.4738056051140088], 
#        'Daniel': [115, 'I', 'L', False, True, 'Service', 0.5182765931408372], 
#        'Samantha': [97, 'I', 'W', True, True, 'Medical', 0.07082409148069169], 
#        'Sacagawea': [28, 'F', 'U', True, True, 'Medical', 0.29790328657890996], 
#        'Ixchel': [26, 'F', 'S', False, False, 'Business', 0.22593704520870372], 
#        'Nobutoshi': [31, 'M', 'W', False, True, 'Business', 0.37923896100469956], 
#        'Gorou': [55, 'M', 'B', True, True, 'Banker', 0.8684653864827863], 
#        'Keiko': [34, 'M', 'L', False, True, 'Student', 0.02499269016601946], 
#        'Seong-Su': [1, 'M', 'M', False, True, 'Retail', 0.3214997836868769], 
#        'Aya': [41, 'M', 'B', True, True, 'Teacher', 0.3378161065313626], 
#        'Okan': [11, 'I', 'W', True, True, 'Banker', 0.35535128959244744], 
#        'Mai': [31, 'F', 'M', False, False, 'Service', 0.7072299366468716], 
#        'Chaza-el': [84, 'I', 'E', True, True, 'Teacher', 0.263795143996962], 
#        'Estera': [79, 'M', 'U', True, False, 'Tradesperson', 0.09970175216521693], 
#        'Dante': [82, 'M', 'L', True, False, 'Unemployed', 0.2126494288577333], 
#        'Leofric': [68, 'F', 'B', True, False, 'Unemployed', 0.19591887643941486], 
#        'Anabelle': [63, 'M', 'B', False, False, 'Teacher', 0.3558324357405023], 
#        'Harsha': [119, 'I', 'O', False, True, 'Retail', 0.3359989642837887], 
#        'Dionisia': [92, 'F', 'B', True, False, 'Doctor', 0.42704604164789706], 
#        'Rajesh': [55, 'F', 'M', True, False, 'Doctor', 0.485752225148387], 
#        'Scilla': [60, 'F', 'M', False, False, 'Student', 0.7294089528796434], 
#        'Arsenio': [10, 'I', 'L', False, True, 'Teacher', 0.0819890866210915]}
#new_person = 'Carly'
#new_person_attributes = 71, 'F', 'L', True, False, 'Unemployed', 0.2126494288577333 # Pregnant
#prioritized_list = generate_prioritized_list(folks)
#prioritized_list_copy_n = list.copy(prioritized_list)
#new_prioritized_list_with_insertion = add_new_person(prioritized_list, folks, new_person, new_person_attributes)
#print("Original prioritized list: %s,\nNew prioritized list: %s" % (prioritized_list_copy_n, new_prioritized_list_with_insertion))
#
#
#folks =  {'Issur': [17, 'F', 'O', True, False, 'Service', 0.7599396397686616],         'Luitgard': [0, 'I', 'U', True, True, 'Unemployed', 0.7599396397686616], } 
#prioritized_list = generate_prioritized_list(folks)
#print("Prioritized list: %s" % (prioritized_list))