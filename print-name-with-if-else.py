users_name = input("type your name")
trimmed_users_name = users_name.strip()
if len(trimmed_users_name) > 1:
    print (trimmed_users_name)
else:
    print ("too short name")

