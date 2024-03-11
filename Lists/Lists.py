"""
List are a collection of data
"""

my_list = [10, 32, 13, 48, 5]

people_list = ['Diego', 'Benjamin', 'Marcos']
print(people_list[1])

# We can get the last element using negative index
# No matter how big is the list, take a look on the
# example below. Pay attention, the index, when u
# use a negative index, starts with 1, in this case
# minus 1 (-1)
print(people_list[-3])

# We can use function LEN to verify the size of a list
print(len(people_list))

# Other way to print an interval of data is using :
# take a look
print(people_list[0:2])

# The print will start at the element 0
# will print the first name (idx 0), the second (1) but the last
# one will not be printed because is not inclusive

"""
Insert and Delete in a list
"""

# We use APPEND to INCLUDE in the list at the end of the list
people_list.append('Albino')
print(people_list)

# Or we can ADD in a specific index some information as we can use
# the code below with INSERT

people_list.insert(0,'Lenice')
print(people_list)

# But if we do not want to ADD some data, we can remove this data with
# REMOVE function, to remove an specific data or we can just use POP function
# to delete using de INDEX. See the code.

people_list.remove('Diego')
print(people_list)

people_list.pop(-1)
print(people_list)

# We can SORT an array (list), for example

people_list.sort()
print(people_list)

my_list.sort()
print(my_list)


"""
                [[[[FUNÇÕES DE ARRAYS E VETORES]]]]

.append()                       -> adiciona um elemento ao final da lista
.extend()                       -> adiciona os elementos do iterável ao final da lista
.insert(index, element)         -> insere um elemento em uma posicação específica 
.remove(element)                -> remove a primeira ocorrência do elemento da lista
.pop(index)                     -> remove e retorna o elemento na posição específica 
                               (ou o último caso nenhum índice seja especificado)

.index(element)                 -> retorna o índice da primeira ocorrência do elemento especificada
.count(element)                 -> retorna o número de ocorrência do elemento especificado
.sort(key=none, reverse=false)  -> ordena os elementos da lista
.reverse()                      -> inverte a ordem dos elementos na lista


Exemplos: 

people_list = ['Diego', 'Benjamin', 'Marcos']

APPEND
    people_list.append('Maria')
    print(people_list)

EXTEND
    new_people = ['Luisa', 'Carla']
    people_list.extend(new_people)
    print(people_list)

INSERT
    people_list.insert(1, 'Felipe')
    print(people_list)
    
REMOVE
    people_list.remove('Benjamin')
    print(people_list)
    
POP
    removed_person = people_list.pop(2)
    print(removed_person)  # Output: 'Marcos'
    print(people_list)
    
INDEX
    index_of_felipe = people_list.index('Felipe')
    print(index_of_felipe)

COUNT
    count_of_diego = people_list.count('Diego')
    print(count_of_diego)
    
SORT
    people_list.sort()
    print(people_list)
    
REVERSE
    people_list.reverse()
    print(people_list)
    
====================================================
Exemplos com números

numbers = [5, 2, 8, 1, 6]

APPEND
    numbers.append(10)
    print(numbers)
    
EXTEND
    new_numbers = [7, 3]
    numbers.extend(new_numbers)
    print(numbers)
    
INSERT
    numbers.insert(2, 4)
    print(numbers)

REMOVE
    numbers.remove(8)
    print(numbers)

POP
    removed_number = numbers.pop(3)
    print(removed_number)  # Output: 1
    print(numbers)
    
INDEX
    index_of_six = numbers.index(6)
    print(index_of_six)

COUNT
    count_of_three = numbers.count(3)
    print(count_of_three)

SORT
    numbers.sort()
    print(numbers)

REVERSE
    numbers.reverse()
    print(numbers) 

"""

