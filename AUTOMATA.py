import urllib.error
from urllib import request as rq
import sys

class colors:
    green = '\033[92m'
    cyan = '\033[96m'
    bold = '\033[1m'
    warning = '\033[93m'
    fail = '\033[91m'
    end = '\033[0m'
    purple = '\033[95m'


def Banner():
    print(colors.green + "\n\n Version : v1\n")

    print(colors.cyan + '''                       /\\     |       |  #####;&&&&&  |~~~~~~/|  {}   {}     /\\     [][][;][][]     /\\   
                      /  \\    [       ]       |       |    /  |  | \\~/ |    /  \\         |         {  }                          
                     / {} \\   |       |       |       |  /    |  |     |   / == \\        |        / %% \\                  
                    /      \\  .<_____>.       |       |/______|  |     |  /      \\       |       /      \\  <ANONYM/> ''')

    print(
        colors.green + "______________________________________________________________________________________________________________________________________")


class funny:
    def __init__(self):
        try:
            print(colors.bold + "\n                                                        Initializing")
            print(colors.purple + "URL Examples : h t t p s : / / g o o g s . c o m"
                                  "\n               h t t p s : / / f a m b o o k . c o m "
                                  "\nPlease mention https ,http ,ftp or other protocols for this to work....")
            self.url = str(input(colors.green + "\nEnter a URL : "))
            

        except Exception as x:
            print(f'ERROR : {x}')

    def game(self):

        print(colors.bold + "\n Warming UP!! ")
        print(f"\n Working on URL : {self.url}")

        error_occurred = False
        while self.mode != int(9):
            try:    
                    elements = {}
                    print(colors.purple + "There are two things that are pivotal in this case:" +
                          colors.cyan + "\n 3 : The path"
                          "\n 1 : The element that is searching for the the word"
                          "\n 2 : The word that is getting searched"
                          "\n\n http://testphp.vulnweb.com/search.php "
                          "\n Here, testphp.vulnweb.com is the Network Location and /search.php is the path"
                          '\n\n Example : \n<input name="searchFor" type="text" size="10">'
                          '\n Here , " searchFor " is the element that searches the word'
                          '\n\n <h2 id="pageName">searched for: fancy</h2>'
                          '\n Here , " fancy " is the word that is being searched.'
                    
                          '\n\n You can, however, search multiple for multiple things in a webpage with this option.')
                    path = input(colors.cyan + '\n\n Path (no need for placing "/" in the beginning):')
                    while True:
                        searching = input(colors.purple + "\n\nEnter the searching element (Press 'q' to come out of "
                                                          "the loop) : ")

                        if searching.lower() == 'q':
                            break
                        searched = input(colors.purple + "\nEnter the word / element to be searched : ")

                        elements[searching] = searched
                    print(colors.bold + f"\n\nResulting pairs are : {elements}")
                    print(colors.cyan + "\n Proceeding further...")
                    url = self.url + '/' + path

                    encoded_data = urllib.parse.urlencode(elements).encode('utf-8')
                    read = rq.urlopen(url, data=encoded_data)
                    result = read.read().decode('utf-8')
                    print(result)

            except urllib.error.HTTPError as e:
                if not error_occurred:
                    print(colors.fail + "Status : ", e.code)
                    print(colors.warning + "Reason : ", e.reason)
                    print(colors.end + "URL : ", e.url)
                    error_occurred = True

                    continue_option = input(colors.purple + "Do you want to continue? (y/n): ").lower()
                    if continue_option != 'y':
                        print(colors.fail + "\n A.O.U.T.O.M.A.T.A FAILED")
                        break

            except ssl.SSLCertVerificationError as ssl_error:
                if not error_occurred:
                    print(colors.fail + f"SSL Certificate Verification Error: {ssl_error}")
                    error_occurred = True

                    continue_option = input(colors.purple + "Do you want to continue? (y/n): ").lower()
                    if continue_option != 'y':
                        break

            except urllib.error.URLError as e:
                if not error_occurred:
                    print(colors.fail + f"\nURL Error: {e}")
                    print(colors.warning + "\nURL Reason : ", e.reason)
                    error_occurred = True


if __name__ == '__main__':
    Banner()
    probe = funny()
    probe.game()
