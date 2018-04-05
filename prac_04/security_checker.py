usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye' ,'swei45' ,'BaseInterpreterInterface' ,'BaseStdIn',
'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


while True:
    user_input = input("Please enter your user name: ")

    if user_input in usernames:
        print("Access granted")
        break

    else:
        print("Access denied")

