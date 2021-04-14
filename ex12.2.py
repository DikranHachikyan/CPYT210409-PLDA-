def new_file():
    return 'create a new file'

def open_file():
    return 'open file ...'

def save_file():
    return 'save'

def quit_app():
    print('Quit Editor')
    quit()

if __name__ == '__main__':
    
    actions = {
        'n': new_file,
        'p': open_file,
        's': save_file,
        'q': quit_app
    }

    ch = input('Command (n-new, p-open, s-save, q-quit):')
    
    if ch in actions:
        res = actions[ch]()
        print(f'action:{res}')
    else:
        print(f'Unknown Command: {ch}')

    print('--- ---')    