import requests
import datetime
import os
def invsearch(invite):
    response = requests.get('https://discord.com/api/v9/invites/'+invite).json()
    id = response['inviter']['id']
    response = requests.post('https://lookupguru.herokuapp.com/lookup', json={'input': id, 'input': id, 'result': None,}).json()
    username = response['data']['username']
    tag = response['data']['discriminator']
    creationdate = response['data']['created_at']/1000
    print("Username: " + username + "#" + tag + "\nID: " + id + "\nCreation Date: " + datetime.datetime.fromtimestamp(creationdate).strftime('%Y-%m-%d'))
def main():
    os.system("cls & Title Discord Invite Resolver & mode 50,10")
    option = input("Invite Code: ")
    invsearch(option)
if __name__ == "__main__":
    main()