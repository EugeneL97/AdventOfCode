# There are connections x-y
    # x-y are connected through lan
    # x-z could also be connected together and thus
        # x-y-z
    # These aren't directonal connections
    # Groups these into sets of 3
        # We need to start with a hash map first
        # Only look at lists with connections that start with t
        # We will store the initial connection as a 'key' and map its other connections as 'values'
        # Loop through the values, and after every 3 iterations, section that set off and move onto the next until we've exhausted it
        # They can only be of size 3

    # Find the groups that start with t
    # Sum the total of groups of three, that have a connection that starts with t

with open('input.txt', 'r') as f:
    connections = [line.strip().split('-') for line in f]
    #print(connections)

three_way_connections = set()
dict_for_t = {}
# for connection in connections:
#     if connection[0][0] == 't':
#         dict_for_t[connection[0]] = connection[1]
#     elif connection[1][0] == 't':
#         dict_for_t[connection[1]] = connection[0]

for connection in connections:
    dict_for_t[connection[0]] = connection[1]

for key,values in dict_for_t.items():
    print(key,values)
print(dict_for_t)
print(len(three_way_connections))