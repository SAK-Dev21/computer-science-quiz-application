import random
import time
import string
import File_B 
import File_C 
from just_playback import Playback

"""--------------------------------------Class CTA (AKA Calls to Action)---------------------------------------"""
class CTA: #Call to Action for short
    
    
    """ Summary: The purpose of this class is to organise methods related to the beginning of the program. 
                These include acquiring and returning user details, customising settings, an introduction 
                And access to particular subtopics.
    """ 
    # These two details must be class variables so that they can be changed in settings():
    username = ""
    password = ""
    
    #To Play Audio here
    playback = Playback()
    
    @classmethod
    def Main_menu_confirm(cls):
        
        """ Summary: The purpose of this program is to automate confirmation choices for returning to main menu

        Returns:
            [ Main_Menu() ]
        """
        
        # Gives user the option to return to Main menu at any time they'd like. 
        
        while True:
            try:
                Enter = int(input(f"\n Enter [1] to return to main menu: "))
                if Enter == 1:
                    Main_menu()
                    break
                else:
                    print(f"\n Invalid Input. Try again.")
            except ValueError:
                print(f"----------------------------")
                print(f" Invalid input. Try again.")
                print("----------------------------")
                
    @classmethod
    def _RPG(cls,Character_length):
        
        """ Summary: The purpose of this function is to randomly generate a password for the user as a 
                    form of security.

        Returns:
            [ new_random_generated_password ]
        """
        
        # Acquiring letters lowercase, uppercase, numbers and symbols
        
        letters_A = string.ascii_lowercase
        letters_B = string.ascii_uppercase
        numbers = string.digits
        symbols = string.punctuation
        
        # Creating a brand new password out of the letters, numbers & symbols
        
        brand_new_password = letters_A + letters_B + numbers + symbols
        new_password = random.sample(brand_new_password, Character_length)
        
        # returning the new RPG password to the user...
        
        return "".join(new_password)
    
    @classmethod
    def Return_details(cls,username,password):
        
        """ Summary: The purpose of this function is to simply return the username and password of the user 
                    at any given time

        Returns:
            [ username, password ]
        """
        
        print(f"\n Please wait as we load up your new details...")
        
        # This is just a bootleg loading screen to look cool as you 'Wait' for your details to come up 😏:
        
        for I in range(3):
            print("\n ." * I)
            time.sleep(1)
                
        # Returns Username and Password
        print(f" Username: {CTA.username} \n Password: {CTA.password}")
    
    
    @classmethod
    def Acquire_username(cls):
        
        """ Summary: The purpose of this function is to acquire the username of the user at any given time
        
        Returns:
            [ Return_details(username,password) ]
        """
        
        # I don't want the username to be too long 😭😭😭
        
        while True:
            try: 
                username_input = input(f"\n Please enter a Username: \n E.G: WinnythePoo1939 ")
                if len(username_input) < 15:
                    CTA.username = username_input
                    CTA.Return_details(CTA.username, CTA.password)
                    time.sleep(3.0)
                    CTA.Customise_settings()
                    break
                else:
                    print("----------------------------")
                    print(f" Invalid input. Please try again")
                    print("----------------------------")
            except ValueError:
                print("----------------------------")
                print(f" Invalid Input. Please try again.")
                print("----------------------------")
                    
    @classmethod
    def Acquire_password(cls):
        """ Summary: The purpose of this method is to acquire a password from the user at any given time whenever
            called upon.
        """
        
        # I don't want the password to be too long 😭😭😭
        
        # Allowing the user to decide if they want a randomly generated password (for security reasons) or to 
        # Manually create their own password 
        
        while True:
            try: 
                password_choice = int(input(f"\n Would you like to manually create your password [1] or randomly generate it? [2] "))
                 
                if password_choice == 1:
                    
                    password_input = input(f"\n Please enter a Password: \n E.G: NoobMaster69 ")
                    if len(password_input) < 12:
                        CTA.password = password_input
                        CTA.Return_details(CTA.username,CTA.password)
                        time.sleep(3.0)
                        CTA.Customise_settings()
                        break
                    else:
                        print("----------------------------")
                        print(f" Password length longer than 12 characters. Please try again")
                        print("----------------------------")
        
                elif password_choice == 2:
                    
                    password_length = str(input(f"\n Enter (as a number) a reasonable length of this password: "))
                    if int(password_length) < 13:
                        CTA.password = CTA._RPG(int(password_length))
                        CTA.Return_details(CTA.username,CTA.password)
                        time.sleep(3.0)
                        CTA.Customise_settings()
                        break
                    else:
                        print("----------------------------")
                        print(f" Password length uncompromisable. Please try again.")
                        print("----------------------------")
            
                else:
                    print("----------------------------")
                    print(f" Invalid Input. You must select [1] or [2]")
                    print("----------------------------")        
                            
            except ValueError:
                print("----------------------------")
                print(f" Invalid Input. Please try again.")
                print("----------------------------")
                
    @classmethod
    def Introduction(cls):
        
        """Summary: Introduces the app to the user in more thorough detail

        Returns:
            [ An Introduction 🤷 ]
        """
        
        # Description of App
        
        print (f"\n Parody Revision is a resource developed with A level Computer Science"
                " students in mind to help them recall and test knowledge actively with all the computer science"
                "subtopics all in one place.  -> IN THE MOST UNEXPECTED WAY POSSIBLE 💀"
                "\n This resource will test your knowledge with rounds of 3 types."
                "\n Each subtopic is divided into 4 difficulties of ascending difficulty: Easy, Medium, Hard, Tryhard."
                "\n For each subtopic, all questions possible within that subtopic for A level are divided in to these categories."
                "\n Within each round, you will be asked to enter a multiple choice answer.")
        
        time.sleep(11.0) 
        
        # Returning to main menu
        
        CTA.Main_menu_confirm()         
    
    @classmethod
    def Legal_Ts_And_Cs(cls):
        """ Summary: The purpose of this function is to define everything legal and so me and my cohorts get sued
        £1.59 by any users
        """
    
        #Play Legal Audio
        File_C.Rounds.PlayAudioFile(CTA.playback,"./computer-science-quiz-application/Sound tracks/Legal Audio.wav", "Play")
        
        time.sleep(2.0)
        
        print(f""" \n Acceptance of Terms
                By using this quiz application, you agree to these terms and conditions. If you do not agree to these terms and conditions, please do not use this application.

                Use of the Application
                The quiz application is intended for personal and non-commercial use only. You may not use the application for any illegal or unauthorized purpose. You agree to comply with all applicable laws and regulations while using this application.

                Ownership
                The quiz application, including all intellectual property rights, belongs to the owner. You may not modify, reproduce, distribute, or sell any part of this application without the owner's prior written consent.

                Disclaimer of Warranties
                The quiz application is provided "as is" and without warranties of any kind, whether express or implied. The owner does not guarantee that the application will be error-free, secure, or available at all times.

                Limitation of Liability
                The owner is not liable for any damages, including but not limited to direct, indirect, incidental, special, or consequential damages, arising from the use of or inability to use the quiz application.

                Volume
                The quiz application may limit the volume of use that a single user or IP address may make of the application. You agree to abide by any such limits that the application imposes.

                Modification of Terms
                The owner reserves the right to modify these terms and conditions at any time. Your continued use of the quiz application after such modifications will constitute your acceptance of the modified terms.

                Governing Law
                These terms and conditions shall be governed by and construed in accordance with the laws of the jurisdiction in which the owner is located.

                Entire Agreement
                These terms and conditions constitute the entire agreement between you and the owner regarding the use of the quiz application. Any failure by the owner to enforce any right or provision of these terms shall not constitute a waiver of such right or provision.")
                """)
        
        while True:
        
            try:
                Choice = int(input(f"\n Press [1] to go to the Main menu: "))
                
                if Choice == 1:
                    #Stop Legal Audio
                    File_C.Rounds.PlayAudioFile(CTA.playback,"./computer-science-quiz-application/Sound tracks/Legal Audio.wav", "Stop")
                    Main_menu()
                    break
                else:
                    print("\n----------------------------")
                    print(f" Invalid input. Please try again.")
                    print("----------------------------")
                
            except ValueError:
                print("\n----------------------------")
                print(f" Invalid input. Please try again.")
                print("----------------------------")
        
    @classmethod
    def Customise_settings(cls):
        """ The purpose of this function is to allow the user to view their username and password as well as 
            allow them to change them at any time.
        """
            
        print(f"\n 1: View your Username and Password, 2: Change your username, 3: Change your password, 4: Return to Main menu.")
        print(f"\n NOTE: If you wish to keep either your username or password and change the other,"
                "just enter exactly what those values were for your Username/Password and change the values for the other.")
        
        
        # Gives the user the option to view or change their username and password, or return to main menu.
        
        while True:
            try:
                enter_choice = int(input(f"\n Choose a number based on the following: "))
                
                if enter_choice == 1:
                    CTA.Return_details(CTA.username,CTA.password)
                    time.sleep(5.0)
                    Main_menu()
                    break
                    
                elif enter_choice == 2:
                    CTA.Acquire_username()
                    break
                    
                elif enter_choice == 3:
                    CTA.Acquire_password()    
                    break
                
                elif enter_choice == 4:
                    Main_menu()
                    break
                
                else:
                    print("----------------------------")
                    print(f" Invalid input. Please try again.")
                    print("----------------------------")
                
            except ValueError:
                print("----------------------------")
                print(f" Invalid Input. Please try again.")
                print("----------------------------")
     
    @classmethod
    def Paper_2(cls):
        """ The purpose of this function is to allow the user to view the subtopics of paper 2 (as objects) and 
            allow them to decide which they want to choose and have a go on.
       """
        # Displaying the subtopics
        
        print(f"\n 1: Fundamentals of data representation ")
                
        
        choice = int(input(f"\n Enter the number in reference to the subtopic you'd like to interact with: "))
        
        while True:
            try: 
                if choice == 1:
                    # This object will be 
                    #(FODR) = Fundamentals of Data Representation
                    #FODR.Display_Difficulty()
                    
                    """ Creating FODR object whilst initialising questions from File_B """
                    
                    FODR = File_C.Questions_with_Stats("Fundamentals of Data Representation")
                    
                    FODR._EasyQuestions = File_B.Topic1.FODR_EasyQuestions
                    FODR._MediumQuestions = File_B.Topic1.FODR_MediumQuestions
                    FODR._HardQuestions = File_B.Topic1.FODR_HardQuestions
                    FODR._TryhardQuestions = File_B.Topic1.FODR_TryhardQuestions
                    
                    FODR.DisplayDifficulty(FODR._EasyQuestions,FODR._MediumQuestions,FODR._HardQuestions,FODR._TryhardQuestions)
                    
                    break
                
                else:
                    print("----------------------------")
                    print(f" Invalid input. Please try again.")
                    print("----------------------------")
                    
                    Main_menu()                    
                    
            except ValueError:
                print("----------------------------")
                print(f" Invalid Input. Please try again.") 
                print("----------------------------")
                
"""--------------------------------------Class CTA (AKA Calls to Action)---------------------------------------"""                

# This Social Credit Variable is Global so It can be seen throughout the program
Social_Credit = 0 
      
def Main_menu():
    
     
    while True:
        
        # Introducing the user, after all one must be chivalrous 😀
        
        # The last 2 lines can be randomised for comedic effect 
        
        print (f"\n Welcome to Paraody Revision!" 
            " This resource was created and developed in mind by Neuro_pseudochemist of -2057.5 years DR S.Khan."
            "\n For national security reasons, my government name must not be baited out... 🤫♋ ")
        
        print(f"\n TIP: YOU MAY WANT TO LOWER YOUR VOLUME BY AT LEAST 5% WHILST USING THIS APPLICATION 🎬")
        
        time.sleep(2.0)
        
        try:
            time.sleep(2.0)
            
            print(f"\n Social Credit: {Social_Credit}")
            
            print(f"\n Select the following numbers as options:")
            select_choice = int(input(f" 1: Settings \n 2: Paper 1 \n 3: Paper 2" 
                                "\n 4: What is Parody revision? "
                                "\n 5: Legal Terms and Conditions (Please Click before using this program"
                                "\n Enter your input: "))
            
            if select_choice == 1:
                CTA.Customise_settings()
            if select_choice == 2:
                # Paper 1()
                pass
                
            if select_choice == 3:
                # Paper 2()
                CTA.Paper_2()
                
            if select_choice == 4:
                CTA.Introduction()
            
            if select_choice == 5:
                #pass function
                CTA.Legal_Ts_And_Cs()
                
            else:
                print("\n----------------------------")
                print(f" Invalid input. Please try again.")
                print("----------------------------")

        except ValueError:
            print("\n----------------------------")
            print(f"Invalid input. Enter a number based on the options presented.")
            print("----------------------------")


if __name__ == '__main__':
    Main_menu()
    
