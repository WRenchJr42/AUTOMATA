from urllib import request as rq
import sys
import re
from urllib.parse import urlparse

class colors:
    green = '\033[92m'
    cyan = '\033[96m'
    bold = '\033[1m'
    warning = '\033[93m'
    fail = '\033[91m'
    end = '\033[0m'

def Banner():
    print(colors.green + "\n\n Version : v1\n")

    print(colors.cyan + '''  /\\     |       |  #####;&&&&&  |~~~~~~/|  {}   {}     /\\     [][][;][][]     /\\   
                      /  \\    [       ]       |       |    /  |  | \\~/ |    /  \\         |         {  }                          
                     / {} \\   |       |       |       |  /    |  |     |   / == \\        |        / %% \\                  
                    /      \\  .<_____>.       |       |/______|  |     |  /      \\       |       /      \\  <ANONYM/> ''')

    print(colors.green + "____________________________________________________________________________________________________________________________________________________________________")

class funny:
    def __init__(self):
        try:
            print(colors.bold + "\n Initializing")

            self.url = str(input(colors.green + "Enter a URL : "))
            self.mode = int(input(colors.bold + "\nEnter the option : "
                                                "\n\n 0 : Check Connection "
                                                "\n 1 : GET ; Response Code"
                                                "\n 2 : GET ; Byte Length"
                                                "\n 3 : GET ; Peek at the response"
                                                "\n 4 : GET ; Decode "
                                                "\n 5 : PARSE "
                                                "\n 6 : EXIT\n\n"))

            if int(self.mode) > int(6) or int(self.mode) < int(-1):
                print(colors.warning + "\n ERROR : Invalid Input")
                print(colors.fail + "\n A.O.U.T.O.M.A.T.A FAILED")
                sys.exit(1)

        except Exception as x:
            print(f'ERROR : {x}')

    def game(self):
        try:
            print(colors.bold + "\n Warming UP!! ")
            print(f"\n Working on URL : {self.url}")

            read = rq.urlopen(self.url)

            while self.mode != int(6):
                if self.mode == int(0):
                    response = rq.urlopen(self.url)
                    read = rq.urlopen(self.url)
                    print(f'\n Is URL closed? : {response.closed}')

                elif self.mode == int(1):
                    read = rq.urlopen(self.url)
                    print(f'Response Code : {read.getcode()}')

                elif self.mode == int(2):
                    read = rq.urlopen(self.url)
                    print(f'Byte Length : {len(read.read())}')

                elif self.mode == int(3):
                    read = rq.urlopen(self.url)
                    print(f'Peek URL : {read.peek()}')

                elif self.mode == int(4):
                    read = rq.urlopen(self.url)
                    data = read.read()
                    html = data.decode("UTF-8")
                    print(html)

                elif self.mode == int(5):
                    parsed_url = urlparse(self.url)
                    print("Protocol : ", parsed_url.scheme)
                    print("Network Location : ", parsed_url.netloc)
                    print("Path : ", parsed_url.path)
                    print("Query : ", parsed_url.query)

                self.mode = int(input(colors.bold + "\nEnter the option : "
                                                "\n\n 0 : Check Connection "
                                                "\n 1 : GET ; Response Code"
                                                "\n 2 : GET ; Byte Length"
                                                "\n 3 : GET ; Peek at the response"
                                                "\n 4 : GET ; Decode "
                                                "\n 5 : PARSE "
                                                "\n 6 : EXIT\n\n"))

            if self.mode == int(6):
                print("\n Exiting A.U.T.O.M.A.T.A")
                sys.exit(0)

        except Exception as x:
            print(f"ERROR : {x}")


if __name__ == '__main__':
    Banner()
    probe = funny()
    probe.game()
