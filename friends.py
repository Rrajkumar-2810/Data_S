users = [ {'id':0, 'name':'Ram'}, {'id':1, 'name':'Shyam'}, {'id':2, 'name':'Mohan'}, {'id':3, 'name':'Sita'}]
print(users[2]['name'])
print(users[2]['id'])

friendship_pairs = [(0,1),(2,1),(1,3),(0,3)]
friendship = {user['id']: [] for user in users}
for i,j in friendship_pairs:
    friendship[i].append(j)
    friendship[j].append(i)
print(friendship) # finding the who is who's friend 


def num_of_friends(user):
    user_id = user['id']
    lst = friendship[user_id]
    return len(lst) # finding the total number of people connected to each person


lst1 = [num_of_friends(user) for user in users]
print(lst1)
total_connections = sum(lst1)
avg_connections1 = total_connections/len(users)
avg_connections2 = total_connections/len(lst1)
print(avg_connections1) # Finding the total no. of connections of a persona individually and then finding the average of it... 
print(avg_connections2)

number_of_friends_by_id = [(user['id'], num_of_friends(user)) for user in users]
print(number_of_friends_by_id) # printing the person's no. of friends in a tuple within a list...
