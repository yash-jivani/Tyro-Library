import time

class Library:

    def __init__(self,lstOfBook,LibName,allBook):
        self.LibName = LibName
        self.lstOfBook = lstOfBook
        self.lendedBook = []
        self.allBook = allBook
        self.collection = set(allBook)
        
    def libCollection(self):
        print('\n\n')
        print(f'{self.LibName} have following book Collection : ')
        print()
        for i in self.collection:
            print(i)
        print('---\n\n')

    def show(self):
        print('\n\n')
        print(f'{self.LibName} have following books Available :')
        print()
        for i in self.lstOfBook:
            print(i)
        print('---\n\n')

    def lendbook(self,bookName):
        print('\n\n')
        if bookName not in self.lstOfBook:
            print(f'Sorry ! book is not available ')
        else:
            self.bookName = bookName
            self.lendedBook.append(bookName)
            self.lstOfBook.remove(bookName)

    def addBook(self,bookName):
        print('\n\n')
        self.collection.add(bookName)
        print('Book added Successfully !')

    def returnBook(self,bookName):
        print('\n\n')
        self.lstOfBook.append(bookName)
        print('Library Database updated successfully !')
        print('\n\n')

if __name__=='__main__':

    yash = Library(['python','c','linux','CLRS'], 'YashLibrary',['python','java','linux','CLRS','OOPS IN Cpp','Networking'])

    print(r'''
                            Welcome to ..
  _____                            _       _   _                                   
 |_   _|  _   _   _ __    ___     | |     (_) | |__    _ __    __ _   _ __   _   _ 
   | |   | | | | | '__|  / _ \    | |     | | | '_ \  | '__|  / _` | | '__| | | | |
   | |   | |_| | | |    | (_) |   | |___  | | | |_) | | |    | (_| | | |    | |_| |
   |_|    \__, | |_|     \___/    |_____| |_| |_.__/  |_|     \__,_| |_|     \__, |
          |___/                                                              |___/  by Yash Jivani 
    ''')
    print('\t\t\tNote : Read README.md File ')
    time.sleep(1.5)
    while True:
        print('\n1) Library Book Collection \n2) Available books \n3) Lend Book \n4) Return Book\n5) Add Book \n99) Exit')
        try:
            user = int(input('> '))
        except:
            print('\nPlease Enter vaild input !')
            exit()
        
        if user==1:
            yash.libCollection()

        elif user==2:
            yash.show()

        elif user==3:
            print('\nOnly Choose Books from Available Books !')
            book = input('enter Book name : ')
            yash.lendbook(book)
            print('operation performed successfully !')
        elif user==4:
            book1 = input('Enter book name : ')
            yash.returnBook(book1)

        elif user == 5:
            print('\nNew Book will added in book collection ')
            newBook1 = input('Book Name : ')
            yash.addBook(newBook1)
            print('New book will available soon for Readers !')

        elif user == 99:
            print('\nQuitting...\n')
            time.sleep(0.5)
            exit()
        
        else:
            print('Please enter vaild input ')
    
