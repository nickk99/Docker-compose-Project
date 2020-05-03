import os
import webbrowser

while True:

    print('''         
             Press 1: To enter WordPress
             Press 2: To enter Joomla
             Press 3: To enter Ghost
             Press 4: To enter Drupal
             Press 5: To enter NextCloud
             Press 6: To enter OwnCloud
             Press 7: To exit from menu''')

    ch=int(input())

    if int(ch) == 1:
        print(" Launching Wordpress .....")
        webbrowser.open("http://192.168.43.220:8081/")
        print("Wait .........")

    elif int(ch) == 2:
        print("Launching Joomla ........ ")
        webbrowser.open("http://192.168.43.220:8082/")
        print("Wait..........")

    elif int(ch) == 3:
        print("Launching Ghost ........ ")
        webbrowser.open("http://192.168.43.220:8083/")
        print("Wait..........")

    elif int(ch) == 4:
        print("Launching Drupal ........ ")
        webbrowser.open("http://192.168.43.220:8084/")
        print("Wait..........")


    elif int(ch) == 5:
        print("Launching NextCloud ........ ")
        webbrowser.open("http://192.168.43.220:8085/")
        print("Wait..........")



    elif int(ch) == 6:
        print("Launching Owncloud  ........ ")
        webbrowser.open("http://192.168.43.220:8086/")
        print("Wait..........")
    
    elif int(ch) == 7:
        print("exiting ........")
        os.system( exit() )

    else:
        print("wrong choice")
    
    input("Enter to continue......")
    os.system("clear")
    
