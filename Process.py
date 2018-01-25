from Users import Users


def processUser(name,todayMonth,todayYear):
    usersList = []
    print(todayMonth)
    print(todayYear)
    print(name)
    user_file = open('file/users.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        if list[0]==name and int(list[4])==todayMonth and int(list[5])==todayYear:
            s = Users(list[0],list[1],list[2],list[3],list[4],list[5])
            usersList.append(s)
    return usersList

def processTransaction(name, month,save):
    s_file = open('file/saving.txt', 'r')
    total = 0
    for saving in s_file:
        list = saving.split(',')

        if list[0] == name and list[1] == month and list[2] == save :
            total += float(list[3])
    return total


