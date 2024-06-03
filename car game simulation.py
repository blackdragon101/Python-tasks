help = input('Enter help ')
if help == 'HELP' or 'help':
    print('''
    start - to start the car
    stop - to stop the car
    quit - to quit the game ''')
command = ''
started = False
while True:
        command = input('Enter the key ')
        if command == 'start':
            if started:
                print('car already started')
            else:
                started = True
                print('Car started')
        elif command == 'stop':
            if not started:
                print('car already stopped ')
            else:
                started = False
                print('Car stopped')
        elif command == 'quit':
             exit()
        else:
             print("I don't understand that...")
else:
    print("I don't understand that..." )


