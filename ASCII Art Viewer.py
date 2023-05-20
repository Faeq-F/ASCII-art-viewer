import sys
sys.path.insert(1, './Resources/Components')

from HomePage import HomePage

if __name__ == '__main__':
    main = HomePage()
    main.window.mainloop() #Display the home page