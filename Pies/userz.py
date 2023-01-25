current_users=['george','john','alina','christy','rick']

new_users=['pete'.lower(),'Christy'.lower(),'pamela'.lower(),'margie'.lower(),'bob'.lower(),'Rick'.lower()]


for u in new_users:
    if u in current_users:
        print("Enter a new username, this one is taken.")
    else:
        print("Username available.")
