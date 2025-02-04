import time
import random
import File_A
from just_playback import Playback



"""-----------------------------------------Class Questions_with_Stats-----------------------------------------"""

""" 
Purpose: Stores questions, hints, skill, score average skill and average score (of a subtopic),  
The Questions are a list of dictionaries where each sub-contained dictionary has a question, 
answer and hint as a key.

"""

class Questions_with_Stats(object):

  def __init__(self, Name_of_Subtopic = ""):
    
    """ Summary: The purpose of this function is to initialise all the variables I am going to use. """
    
    """ Public Variables"""
    
    self.Name_of_Subtopic = Name_of_Subtopic

    """ Private Variables"""
    
    # Questions
    self._EasyQuestions = []
    self._MediumQuestions = []
    self._HardQuestions = []
    self._TryhardQuestions = []

  def DisplayDifficulty(self,EasyQuestions,MediumQuestions,HardQuestions,TryhardQuestions):
      
    """ Summary: Displays the Difficulty options as a menu for the user to decide which to choose. """
    
    while True:
        try:
            Choice = int(input(f"\n Choose from the following options: \n 1. Easy \n 2. Medium \n 3. Hard \n 4. Tryhard \n 5. Exit \n "))
            
            EasyQuestions = self._EasyQuestions
            MediumQuestions = self._MediumQuestions
            HardQuestions = self._HardQuestions
            TryhardQuestions = self._TryhardQuestions
            
            # Added together all the [insert difficutly] set of questions together for the Waffle rounds type 2
            Waffle_questions = MediumQuestions + HardQuestions + EasyQuestions + TryhardQuestions
            random.shuffle(Waffle_questions)
            
            if Choice == 1:
                
                """ Creating [Insert Difficulty] as an object of Round() """
                 
                # E.G: Call Easy_FODR = Rounds() (FODR = Fundamentals of Data Representation as an example)
                # E.G: Call Medium_FODR = Rounds() (FODR = Fundamentals of Data Representation as an example)
                # E.G: Call Hard_FODR = Rounds() (FODR = Fundamentals of Data Representation as an example)
                # E.G: Call Tryhard_FODR = Rounds() (FODR = Fundamentals of Data Representation as an example)
                
                """ Initialise values for Easy rounds here"""
                
                # Easy.DisplayMenu()
                Easy = Rounds(10, EasyQuestions, Waffle_questions, self.Name_of_Subtopic, "Easy")
                Easy.DisplayMenu()
                break
        
            if Choice == 2:
                
                """ Initialise values for Medium rounds here"""
                
                # Medium.DisplayMenu()
                Medium = Rounds(20, MediumQuestions, Waffle_questions, self.Name_of_Subtopic, "Medium")
                Medium.DisplayMenu()
                break
                
            if Choice == 3:
                
                
                """ Initialise values for Hard rounds here"""
                
                # Hard.DisplayMenu()
                Hard = Rounds(30, HardQuestions, Waffle_questions, self.Name_of_Subtopic, "Hard")
                Hard.DisplayMenu()
                break
            
            if Choice == 4:
                
                
                """ Initialise values for Tryhard rounds here"""
                
                # Tryhard_FODS.DisplayMenu()
                Tryhard = Rounds(40, TryhardQuestions, Waffle_questions, self.Name_of_Subtopic, "Tryhard")
                Tryhard.DisplayMenu()
                break
            
            if Choice == 5:
                File_A.CTA.Main_menu_confirm()
                break
                
            else:
                print("\n----------------------------")
                print(f" Invalid input. Please try again. ")
                print("----------------------------")
                
        except ValueError:
            print("\n----------------------------")
            print(f" Invalid input. Please try again. ")
            print("----------------------------")
    

"""-----------------------------------------Class Questions_with_Stats-----------------------------------------"""


"""--------------------------------------------------Class Rounds---------------------------------------------------"""

""" 
Purpose: Contains functionality for what happens within a round
Inherits values from Questions_with_Stats  so that it can obtain values easily

"""

class Rounds(Questions_with_Stats):
    
    def __init__(self, Social_Credit_Cost, Questions, Waffle_questions, Name_of_Subtopic = "", Difficulty = "", ):
        
       """ Summary: The purpose of this function is to initialise the attributes used for Rounds() 
           The Parent attributes this class will be inheriting are Name_of_Subtopic, Average_Score & Difficulty
           
           NH: No Hints
           H: Hints
           
           Type1(): Rounds with no hints -> # DEVELOP THIS FIRST!
           Type2(): Rounds with hints  -> # DEVELOP THIS SECOND...
            
           WType1_NH(): Waffle Round Type 1 with no hints -> # DEVELOP THIS THIRD!
           WType1_H(): Waffle Round Type 2 with hints -> ' DEVELOP THIS FOURTH... 
            
           WType2_NH(): Waffle Round Type 2 with no hints -> # DEVELOP THIS FIFTH!
           WType2_H(): Waffle Round Type 2 with hints -> ' DEVELOP THIS SIXTH...          
           
       """
        
       """ Public Variables """
       
       # Inheriting Parent Class Values for the DisplayMenu() method  & 
       # Initialising variables to be used for the round [I.E: Before a round]:
       
       super().__init__(Name_of_Subtopic)
    
       self.Difficulty = Difficulty
 
       # Initialising variables to be used for during a round
       self.Playback = Playback()
       self.Social_Credit_Cost = Social_Credit_Cost
       self.Questions = Questions   
       self.Question_limit = 0
       self.Waffle_questions = Waffle_questions
       
       self.AudioList_W1 = ["./computer-science-quiz-application/Sound tracks/W1_ Vine Boom + Oh No NO No.wav", "./computer-science-quiz-application/Sound effects/Korean guy raging.mp3", "./computer-science-quiz-application/Sound effects/Apple Alarm 2 remastered.mp3"]  
       self.AudioList_W2 = ["./computer-science-quiz-application/Sound tracks/ME3 Ambience but random.mp3", "./computer-science-quiz-application/Sound effects/Monkey noises 1 hour.mp3", "./computer-science-quiz-application/Sound tracks/Gunshots ambiance funny.mp3"]
        
    """ Utility Functions """
    
    @classmethod
    def Waffle_introduction(cls):
        
        """ Summary: The purpose of this function is just to save code and just introduce the waffle rounds """ 
        
        time.sleep(3.0)

        print(f" \n Warning: This setting is not for the weak, faint hearted or easily distracted. " 
                          "\n These rounds were specifically designed by neurologist and pseudochemist of -3574 years, "
                          "developer of this resource, acquaintance of Walter White and legendary world renowned waffler "
                          "Dr S.Khan. \n "
                          "\n (For Legal and National Security reasons, my government name MUST NOT BE BAITED OUT AT ALL COSTS 🤫) \n "
                          "\n You will answer questions alongside the added risk of being distracted by "
                          "my poetic words 😘😘😘 \n"
                          "\n Brace yourself, because you will hear things that will make you question "
                          "your very existence on this planet we call... 🌍")
                        
        time.sleep(3.0)    
        print("-" * 50)
                
        print(f"\n Waffle rounds will work in 1 of 2 ways. "
                "\n \n 1: Type 1 will work like a normal round, but for every question "
                "you get wrong, you will hear my CRISP 😏, ULTRA HD voice until you get "
                "a question right or until the round ends."

                "\n \n 2: EXTREME rounds: "
                "\n \n Type 2 will work like any other round, except you'll receive a " 
                "\n TONNE more questions and you'll hear my LULLING voice 😏😏😏 create Salt and Vinegar "
                "pringles inside of you. "
                "\n Difficulty: There's none. YOU CONSENTED TO BEING 'AUDIBLY PLEASED' by what you're about to hear. "
                "\n Me and my cohorts are not liable for any suing or damage to certain properties."
                "\n By choosing to play EXTREME Rounds, you LEGALLY agreed to take part in these rounds. "
                "\n With all the boring ethics aside, I DARE YOU TO TAKE THIS CHALLENGE. I DARE YOU 😭")
        
        time.sleep(3.0)
        
        print(f"\n You will hear me speak Eloquently throughout 😏 "
                "\n gOOD luck! ")

        time.sleep(3.0)    
        print("-" * 50) 
    
    @classmethod     
    def PlayAudioFile(cls, Playback, Audio_file, Argument):
        
        """ Summary: The purpose of this function is to play, stop, pause, resume and loop audio."""
        
        Playback.load_file(Audio_file)
        
        if Argument == "Play":
            Playback.set_volume(1.3)
            Playback.play()
        if Argument == "Stop":
            Playback.stop()
        if Argument == "Pause":
            Playback.pause()
        if Argument == "Resume":
            Playback.resume()
        if Argument == "Loop":
            Playback.loop_at_end(True)
        if Argument == "Stop loop":
            Playback.loop_at_end(False)
                
    """ 1: Displaying the Appropiate Menus 🍖"""
    
    def DisplayMenu_WNH(self):
        
        """ Summary: The purpose of this function is to display the menu for the Waffle rounds WITH NO HINTS❓ """
    
        Rounds.Waffle_introduction()
        
        
        while True:
            try:
                Select_Choice = int(input(f"\n Press [1] to try Waffle Rounds Type 1. "
                                          "\n Press [2] to try Waffle Rounds Type 2. "
                                          "\n Press [3] to return to Rounds Menu. "
                                          "\n Press [4] to return to Main Menu"
                                          "\n Enter your input: "))
                
                if Select_Choice == 1:
                    #Add Special_Round.WType1(_____)
                    self.WType1_NH(self.Questions,self.Social_Credit_Cost,self.Playback,self.Question_limit)
                    break
                
                elif Select_Choice == 2:
                    #Add Special_Round.WType2(_____)
                    self.WType2_NH(self.Waffle_questions,self.Social_Credit_Cost,self.Playback,self.Question_limit)
                    break
                
                elif Select_Choice == 3:
                    self.DisplayMenu()
                    break
                
                elif Select_Choice == 4:
                    File_A.CTA.Main_menu_confirm()
                    break
                
                else:
                     print(f"----------------------------")
                     print(f" Invalid input. Try again.")
                     print("----------------------------")  
            
            except ValueError:
                print(f"----------------------------")
                print(f" Invalid input. Try again.")
                print("----------------------------")  
    
    def DisplayMenu_WH(self):
        
        """ Summary: The purpose of this function is to display the menu for the Waffle rounds WITH NO HINTS❓ """
    
        Rounds.Waffle_introduction()
        
        while True:
            try:
        
                Select_Choice = int(input(f"\n Press [1] to try Waffle Rounds Type 1. "
                                          "\n Press [2] to try Waffle Rounds Type 2. "
                                          "\n Press [3] to return to Rounds menu. "
                                          "\n Press [4] to return to Main menu. "
                                          "\n Enter your input: "))
                
                if Select_Choice == 1:
                    #Add Special_Round.WType1(_____)
                    self.WType1_H(self.Questions,self.Social_Credit_Cost,self.Playback,self.Question_limit)
                    break
                
                elif Select_Choice == 2:
                    #Add Special_Round.WType2(_____)
                    self.WType2_H(self.Waffle_questions,self.Social_Credit_Cost,self.Playback,self.Question_limit)
                    break
                
                elif Select_Choice == 3:
                    self.DisplayMenu()
                    break
                
                elif Select_Choice == 4:
                    File_A.CTA.Main_menu_confirm()
                    break
                
                else:
                     print(f"----------------------------")
                     print(f" Invalid input. Try again.")
                     print("----------------------------")  
            
            except ValueError:
                print(f"----------------------------")
                print(f" Invalid input. Try again.")
                print("----------------------------")  
 
    def DisplayMenu(self):
        
        while True:
            
            # Welcoming the user into the round 
            print(f"\n Welcome{File_A.CTA.username} to the Round of {self.Name_of_Subtopic}! \n ")
            print(f"\n Difficulty: {self.Difficulty} ")
            
            # Displaying Social Credit
            print(f"\n{File_A.CTA.username} Social Credit: {File_A.Social_Credit}")
    
            print("-" * 50)
            
            time.sleep(5.0)
            
            # Giving an overview of how Rounds will work, for the user's sake
            
            print("\n Rounds work as multiple choice questions here. When a question appears, you will have to enter "
                "the number corresponding to the option. \n Here's an example of a question during a round... ")
            
            print("\n Unless you WANT to lose Social Credit points by not entering any of the numbers displayed "
                  "during a question, ONLY enter the numbers you see. 🛑")
            
            time.sleep(4.0)
            
            print(f"\n E.G: Is Apple Juice better than Orange Juice? \n 1. Yes \n 2. No")
            print(f"\n Enter your answer: 1") 
            print("\n P.S: Water is the BEST DRINK ALIVE‼‼‼‼‼‼‼ - Especially when filtered 🌊🌊🌊")
            
            # Giving the User the option to enable Waffle for the rounds:
            
            print("-" * 50)
            
            time.sleep(5.0)
            
            try:
                Round_options = int(input(f"\n Select either of the following: \n 1. Round 1: No waffle and [Hints] -> [Easy] "
                                          "\n 2. Round 2: Waffle and [Hints] -> [Medium] "
                                          "\n 3. Round 3: No waffle, [No Hints] -> [Hard] "
                                          "\n 4. Round 4: Waffle, with [No hints] -> [Tryhard] "
                                          "\n 5. Exit "
                                          "\n Enter the Number associated with the option: "))
                
                
                """ If Option 1 was selected ✔ """ 
                
                if Round_options == 1:
                    
                    # Calculating how much Social Credit should be taken away from the user whenever they use hints
                    
                    # The Calculation being: (Amount of Questions) * (Social_Credit_Cost / 2)
                    
                    while self.Difficulty != "Tryhard":
                    
                        print(File_A.Social_Credit)
                        
                        time.sleep(2.0)
                        
                        if File_A.Social_Credit >= 0:
                            
                            File_A.Social_Credit -= len(self.Questions) * (self.Social_Credit_Cost / 2)
                            
                            print(f"\n After using hints... \n Social Credit: {File_A.Social_Credit}")
                            
                            # Implement YES hints & NO waffle...
                            time.sleep(2.0)
                            
                            print(f"\n Starting the round in...")
                            time.sleep(1.0)
                            
                            for I in range(6,0,-1):
                                print(f"\n {I}")
                                time.sleep(1.0)
                            
                            # The self.questions and self.Social_Credit_Cost have been predetermined based off their difficulty
                            # in Questions_With_Stats()
                            
                            self.Type2(self.Questions,
                                        self.Social_Credit_Cost,
                                        self.Playback,
                                        self.Question_limit)
                            break
                                        
                        else:
                            print(f"\n You don't have enough Social Credit to use hints")
                            self.DisplayMenu()
                            break
                        
                    else:
                        print(f"n Hints aren't allowed on Tryhard difficulty. You want hints, try an easier difficulty. ")
                        self.DisplayMenu()
                        break
                    
                """ If Option 2 was selected ❌ """
                
                if Round_options == 2:
                    
                    while self.Difficulty != "Tryhard":
                        
                        print(File_A.Social_Credit)
                        
                        time.sleep(2.0)
                            
                        if File_A.Social_Credit >= 0:
                            
                            File_A.Social_Credit -= len(self.Questions) * (self.Social_Credit_Cost / 2)
                        
                            print(f"\n After using hints... \n Social Credit: {File_A.Social_Credit}")
                            
                            # Implement YES hints & NO waffle...
                            time.sleep(2.0)
                            
                            # The self.questions and self.Social_Credit_Cost have been predetermined based off their difficulty
                            # in Questions_With_Stats()
                            
                            self.DisplayMenu_WH()
                            break
                                        
                        else:
                            
                            print(f"\n You don't have enough Social Credit to use hints")
                            self.DisplayMenu()
                            break
                        
                    else:
                        print(f"n Hints aren't allowed on Tryhard difficulty. You want hints, try an easier difficulty. ")
                        self.DisplayMenu()
                        break
                    
                
                """ If Option 3 was selected ✔ """
                
                if Round_options == 3:
                                                     
                    """ Type 1 of Rounds:  """
                    
                    """
                    HINTS: ❌
                    WAFFLE: ❌
                    """
                    # The self.questions and self.Social_Credit_Cost have been predetermined based off their difficulty
                    # in Questions_With_Stats()
                    
                    for X in range(5,-1,-1):
                        print(f"\n {X}")
                        time.sleep(1.0)
                    
                    self.Type1(self.Questions,
                                self.Social_Credit_Cost,
                                self.Playback,
                                self.Question_limit)
                    break
                            
                """ If Option 4 was selected ❌"""
                
                if Round_options == 4: 
                    
                    self.DisplayMenu_WNH()
                    break
                             
                """ If Option 5 was selected """
                
                if Round_options == 5:
                    File_A.CTA.Main_menu_confirm()
                    break
                
                else:
                    print(f"----------------------------")
                    print(f" Invalid input. Try again.")
                    print("----------------------------")
            
            except ValueError:
                print(f"----------------------------")
                print(f" Invalid input. Try again.")
                print("----------------------------")    
     
    """ 2: Category 1: Rounds """  
      
    # No hints, no waffle
        
    def Type1(self, Set_of_Questions, Social_Credit_Cost, Play_file, Question_limit = 0):
        
        """ Summary: The purpose of this function is to create the functionality for what happens during a round. 
        
        HINTS: ❌
        WAFFLE: ❌
        
        """
        
        # Initialise values for the round. (This will be done by setting the following variables
        # as local variables
        
        """ Question Limit: Increments by 1 so that when it reaches the same number as the length of the 
                            set of questions, the round stops and the final results are displayed.
                    
            Current Score:  The Current Score of the user during a round. 
            
            Social_Credit_Total: This records how much Social Credit the user earns during a round. This is
                                 then displayed at the end of the round. 
                                 
            Score_Percentage: This records the Current Score of the user at the end of the round as a percentage.
                              This will be displayed at the end of the round and will be used to indicate the
                              user's strengths/weaknesses for each difficulty.
                              
            Audio list: This stores the names of all Audio files to be used so that they can be played whenever
                        they're called.        
                        
            Play_file: This is used to play the audio files as a placeholder for self.Playback          
        """
        
        Current_Score = 0
        Social_Credit_Total = 0
        Score_Percentage = 0.0
        
        while Question_limit < len(Set_of_Questions):
            
            
            for Question in Set_of_Questions:
                question_text = Question.get("Question")
                print("-" * 100)
                print(question_text)
                    
                try: 
                    user_answer = int(input(f"\n Enter the correct number: "))
                    correct_answer = Question.get("Answer")
                
                    if user_answer == correct_answer:
                        
                        """ What will happen if the user gets the question right
                        
                        Social Credit increases by the pre-determined Social_Credit_Cost, CurrentScore increases by 1
                        and Social_Credit_Total increases too. Finally, the Question_Limit increases by 1
                        
                        """
                        
                        File_A.Social_Credit +=  Social_Credit_Cost
                        Current_Score += 1
                        Social_Credit_Total += Social_Credit_Cost
                        Question_limit += 1
                        
                        Rounds.PlayAudioFile(Play_file,"./computer-science-quiz-application/Sound effects/Correct Type Sound Effect.mp3","Play")
                        
                        # Returning Current score to the user
                        print(f"\n Your Score: {Current_Score} / {len(Set_of_Questions)}")
                        print("-" * 100)
            
                    if user_answer != correct_answer:
                        
                        """ What will happen if the user gets the question wrong
                        
                        Social Credit decreases by the pre-determined Social_Credit_Cost,and Social_Credit_Total 
                        decreases too. Finally, the Question_Limit increases by 1
                        
                        """
                        
                        print("\n Incorrect 😭😭😭😭😭😭😭😭😭😭😭😭 "
                                "\n You GOT THE QUESTION WRONG 💀💀💀💀💀💀💀💀")
                        
                        File_A.Social_Credit -= Social_Credit_Cost
                        Social_Credit_Total -= Social_Credit_Cost
                        
                        Rounds.PlayAudioFile(Play_file,"./computer-science-quiz-application/Sound effects/vine-boom-sound-effect-longer-verison-for-real-read-description-please.mp3"
                                        , "Play")
                        Question_limit += 1
                        
                        # Returning Current score to the user
                        print(f"\n Your Score: {Current_Score} / {len(Set_of_Questions)}")
                        print("-" * 100)

                        
                    if Question_limit == len(Set_of_Questions):
                        
                        # Pass function

                        """ Displaying the final result... """
                        
                        Score_Percentage = (Current_Score / len(Set_of_Questions)) * 100
                                                
                        print(f"\n The Round has now officially finished!!! ")
                        
                        time.sleep(2.0)
                        
                        print(f"\n Loading up your results in ... ")
                        
                        for X in range(5,0,-1):
                            print(f"\n {X}")
                            time.sleep(1.0)
                        
                        print(f"\n Your Score: {Current_Score} / {len(Set_of_Questions)}"
                            f"\n Percentage: {Score_Percentage} "
                            f"\n Social Credit Acquired: {Social_Credit_Total} ")
                        
                        time.sleep(3.0)
                        
                        if Score_Percentage < 25.0:
                            
                            print(f"\n 💀💀💀💀💀💀 YOU DONE TERRIBLE 😂 YOU SHOULD GO AND REVISE..... NOW 😂")
                        
                        if Score_Percentage >= 25.0 and Score_Percentage < 50.0:
                            
                            print(f"\n You done your best and that's respectable. \n But Unfortunately, you NEED to do better. ")
                        
                        if Score_Percentage >= 50.0 and Score_Percentage < 75.0:
                            
                            print(f"\n Not bad, Not bad 👏👏👏👏👏👏 ")
                            
                        if Score_Percentage >= 75.0 and Score_Percentage <= 100:
                            
                            print(f"\n OH SORRRRY, OH SORRRRRY, Someone wants to go to Graduate Computer Science. 🦹‍♂️ ")
                            
                        File_A.CTA.Main_menu_confirm()
                        break     
                    
                    
                    if type(user_answer) == int and user_answer > 4 or user_answer <= 0:
                        print("----------------------------")
                        print(f" Invalid Input. Please try again.") 
                        print("----------------------------")
                        
                        File_A.Social_Credit -= Social_Credit_Total 
                        
                        print("\n To save resources on our servers, we will guide you back to the display menu. "
                        "Please only enter the numbers displayed or you will be Alt + F4 back to the Shadowrealm 🦨")
                        time.sleep(2.0)
                        self.DisplayMenu()
                        break
            
                except ValueError:
                    print("----------------------------")
                    print(f" Invalid Input. Please try again.") 
                    print("----------------------------")
                    
                    File_A.Social_Credit -= Social_Credit_Total
                    
                    print("\n To save resources on our servers, we will guide you back to the display menu. "
                    "Please only enter the numbers displayed or you will be Alt + F4 back to the Shadowrealm 🦨")
                    time.sleep(2.0)
                    self.DisplayMenu()
                    break
   
                        
    """ 3: Category 2: Rounds """
    
    # Hints, no waffle
    
    def Type2(self, Set_of_Questions, Social_Credit_Cost, Play_file, Question_limit = 0):
        
        """ Summary: The purpose of this function is to create the functionality for what happens during a round. 
        
        HINTS: ✔
        WAFFLE: ❌
        
        """
        
        # Initialise values for the round. (This will be done by setting the following variables
        # as local variables
        
        """ Question Limit: Increments by 1 so that when it reaches the same number as the length of the 
                            set of questions, the round stops and the final results are displayed.
                    
            Current Score:  The Current Score of the user during a round. 
            
            Social_Credit_Total: This records how much Social Credit the user earns during a round. This is
                                 then displayed at the end of the round. 
                                 
            Score_Percentage: This records the Current Score of the user at the end of the round as a percentage.
                              This will be displayed at the end of the round and will be used to indicate the
                              user's strengths/weaknesses for each difficulty.
                              
            Audio list: This stores the names of all Audio files to be used so that they can be played whenever
                        they're called.        
                        
            Play_file: This is used to play the audio files as a placeholder for self.Playback          
        """
        
        Current_Score = 0
        Social_Credit_Total = 0
        Score_Percentage = 0.0
        
        while Question_limit < len(Set_of_Questions):
            
            for Question in Set_of_Questions:         
                question_text = Question.get("Question")
                hint_text = Question.get("Hint")
                
                print("-" * 100)
                print(question_text)
                print(f"\n Hint: {hint_text}")
                
                try: 
                    
                    user_answer = int(input(f"\n Enter the correct number: "))
                    correct_answer = Question.get("Answer")
                
                    if user_answer == correct_answer:
                        
                        """ What will happen if the user gets the question right
                        
                        Social Credit increases by the pre-determined Social_Credit_Cost, CurrentScore increases by 1
                        and Social_Credit_Total increases too. Finally, the Question_Limit increases by 1
                        
                        """
                        
                        File_A.Social_Credit +=  Social_Credit_Cost
                        Current_Score += 1
                        Social_Credit_Total += Social_Credit_Cost
                        Question_limit += 1
                        
                        Rounds.PlayAudioFile(Play_file,"./computer-science-quiz-application/Sound effects/Correct Type Sound Effect.mp3", "Play")
                        
                        # Returning Current score to the user
                        print(f"\n Your Score: {Current_Score} / {len(Set_of_Questions)}")
                        print("-" * 100)
            
                    if user_answer != correct_answer:
                        
                        """ What will happen if the user gets the question wrong
                        
                        Social Credit decreases by the pre-determined Social_Credit_Cost,and Social_Credit_Total 
                        decreases too. Finally, the Question_Limit increases by 1
                        
                        """
                        
                        print("\n Incorrect 😭😭😭😭😭😭😭😭😭😭😭😭 "
                                "\n You GOT THE QUESTION WRONG 💀💀💀💀💀💀💀💀")
                        
                        File_A.Social_Credit -= Social_Credit_Cost
                        Social_Credit_Total -= Social_Credit_Cost
                        Rounds.PlayAudioFile(Play_file,
                                            "./computer-science-quiz-application/Sound effects/vine-boom-sound-effect-longer-verison-for-real-read-description-please.mp3",
                                            "Play")
                        Question_limit += 1
                        
                        # Returning Current score to the user
                        print(f"\n Your Score: {Current_Score} / {len(Set_of_Questions)}")
                        print("-" * 100)
                    
                    
                    if Question_limit == len(Set_of_Questions):

                        """ Displaying the final result... """
                        
                        Score_Percentage = (Current_Score / len(Set_of_Questions)) * 100
                                                
                        print(f"\n The Round has now officially finished!!! ")
                        
                        time.sleep(2.0)
                        
                        print(f"\n Loading up your results in ... ")
                        
                        for X in range(5,0,-1):
                            print(f"\n {X}")
                            time.sleep(1.0)
                        
                        print(f"\n Your Score: {Current_Score} / {len(Set_of_Questions)}"
                            f"\n Percentage: {Score_Percentage} "
                            f"\n Social Credit Acquired: {Social_Credit_Total} ")
                        
                        time.sleep(3.0)
                        
                        if Score_Percentage < 25.0:
                            
                            print(f"\n 💀💀💀💀💀💀 YOU DONE TERRIBLE 😂 YOU SHOULD GO AND REVISE..... NOW 😂")
                        
                        if Score_Percentage >= 25.0 and Score_Percentage < 50.0:
                            
                            print(f"\n You done your best and that's respectable. \n But Unfortunately, you NEED to do better. ")
                        
                        if Score_Percentage >= 50.0 and Score_Percentage < 75.0:
                            
                            print(f"\n Not bad, Not bad 👏👏👏👏👏👏 ")
                            
                        if Score_Percentage >= 75.0 and Score_Percentage <= 100:
                            
                            print(f"\n OH SORRRRY, OH SORRRRRY, Someone wants to go to Graduate Computer Science. 🦹‍♂️ ")
                            
                        File_A.CTA.Main_menu_confirm()
                        break
            
                    if type(user_answer) == int and user_answer > 4 or user_answer <= 0:
                        print("----------------------------")
                        print(f" Invalid Input. Please try again.") 
                        print("----------------------------")
                        
                        File_A.Social_Credit -= Social_Credit_Total 
                        
                        print("\n To save resources on our servers, we will guide you back to the display menu. "
                        "Please only enter the numbers displayed or you will be Alt + F4 back to the Shadowrealm 🦨")
                        time.sleep(2.0)
                        self.DisplayMenu()
                        break
            
                except ValueError:
                    print("----------------------------")
                    print(f" Invalid Input. Please try again.") 
                    print("----------------------------")
                    
                    File_A.Social_Credit -= Social_Credit_Total
                    
                    print("\n To save resources on our servers, we will guide you back to the display menu. "
                    "Please only enter the numbers displayed or you will be Alt + F4 back to the Shadowrealm 🦨")
                    time.sleep(2.0)
                    self.DisplayMenu()
                    break
                   
    """ 4: Category 3: Rounds"""
    
    def WType1_NH(self, Set_of_Questions, Social_Credit_Cost, Play_file, Question_limit = 0 ):
        
        """ Summary: The purpose of this function is to create the functionality for Type_1 Waffle rounds 
        
        HINTS: ❌
        WAFFLE: ✔
        
        """
 
        """ Question Limit: Increments by 1 so that when it reaches the same number as the length of the 
                            set of questions, the round stops and the final results are displayed.
                    
            Current Score:  The Current Score of the user during a round. 
            
            Social_Credit_Total: This records how much Social Credit the user earns during a round. This is
                                 then displayed at the end of the round. 
                                 
            Score_Percentage: This records the Current Score of the user at the end of the round as a percentage.
                              This will be displayed at the end of the round and will be used to indicate the
                              user's strengths/weaknesses for each difficulty.
                              
            Audio list: This stores the names of all Audio files to be used so that they can be played whenever
                        they're called.        
                        
            Play_file: This is used to play the audio files as a placeholder for self.Playback          
        """
        
        Current_Score = 0
        Social_Credit_Total = 0
        Score_Percentage = 0.0
        
      
        
        while Question_limit < len(Set_of_Questions):
            
            for Question in Set_of_Questions:
                question_text = Question.get("Question")
                print("-" * 100)
                print(question_text)
                
                Audio = random.choice(self.AudioList_W1)
                    
                try:
                    user_answer = int(input(f"\n Enter the correct number: "))
                    correct_answer = Question.get("Answer")
                    
                    if user_answer == correct_answer:
                        
                        """ What will happen if the user gets the question right
                        
                        Social Credit increases by the pre-determined Social_Credit_Cost, CurrentScore increases by 1
                        and Social_Credit_Total increases too. Finally, the Question_Limit increases by 1
                        
                        """
                        # Stopping Waffle if answer is right
                        if Play_file.active:
                            Rounds.PlayAudioFile(Play_file, Audio,"Stop")
                        else:
                            Rounds.PlayAudioFile(Play_file, Audio,"Stop")
                        
                        File_A.Social_Credit +=  Social_Credit_Cost
                        Current_Score += 1
                        Social_Credit_Total += Social_Credit_Cost
                        Question_limit += 1
                        
                        # Returning Current score to the user
                        print(f"\n Your Score: {Current_Score} / {len(Set_of_Questions)}")
                        print("-" * 100)
            
                    if user_answer != correct_answer:
                        
                        """ What will happen if the user gets the question wrong
                        
                        Social Credit decreases by the pre-determined Social_Credit_Cost,and Social_Credit_Total 
                        decreases too. Finally, the Question_Limit increases by 1
                        
                        """
                        # Playing Audio if Answer Wrong
                        if Play_file.paused == False:
                            Rounds.PlayAudioFile(Play_file, Audio,"Play")   
                        else:
                            Rounds.PlayAudioFile(Play_file, Audio,"Resume")
                        
                        print("\n Incorrect 😭😭😭😭😭😭😭😭😭😭😭😭 "
                                "\n You GOT THE QUESTION WRONG 💀💀💀💀💀💀💀💀")
                        
                        File_A.Social_Credit -= Social_Credit_Cost
                        Social_Credit_Total -= Social_Credit_Cost
                        Question_limit += 1
                        
                        # Returning Current score to the user
                        print(f"\n Your Score: {Current_Score} / {len(Set_of_Questions)}")
                        print("-" * 100)
                        
                    if Question_limit == len(Set_of_Questions):
                
                        #Stopping Random Audio from playing once the round has ended
                        
                        Rounds.PlayAudioFile(Play_file, Audio, "Stop")

                        """ Displaying the final result... """
                        
                        Score_Percentage = (Current_Score / len(Set_of_Questions)) * 100
                                                
                        print(f"\n The Round has now officially finished!!! ")
                        
                        time.sleep(2.0)
                        
                        print(f"\n Loading up your results in ... ")
                        
                        for X in range(5,0,-1):
                            print(f"\n {X}")
                            time.sleep(1.0)
                        
                        print(f"\n Your Score: {Current_Score} / {len(Set_of_Questions)}"
                            f"\n Percentage: {Score_Percentage} "
                            f"\n Social Credit Acquired: {Social_Credit_Total} ")
                        
                        time.sleep(3.0)
                        
                        if Score_Percentage < 25.0:
                            
                            print(f"\n 💀💀💀💀💀 YOU DONE TERRIBLE 😂 YOU SHOULD GO AND REVISE..... NOW 😂")
                        
                        if Score_Percentage >= 25.0 and Score_Percentage < 50.0:
                            
                            print(f"\n You done your best and that's respectable. \n But Unfortunately, you NEED to do better. ")
                        
                        if Score_Percentage >= 50.0 and Score_Percentage < 75.0:
                            
                            print(f"\n Not bad, Not bad 👏👏👏👏👏👏 ")
                            
                        if Score_Percentage >= 75.0 and Score_Percentage <= 100:
                            
                            print(f"\n OH SORRRRY, OH SORRRRRY, Someone wants to go to Graduate Computer Science. 🦹‍♂️ ")
                            
                        File_A.CTA.Main_menu_confirm()
                        break
                    
                    
                    if type(user_answer) == int and user_answer > 4 or user_answer <= 0:
                        print("----------------------------")
                        print(f" Invalid Input. Please try again.") 
                        print("----------------------------")
                        
                        # Subtracting Social Credit if invalid input entered
                        File_A.Social_Credit -= Social_Credit_Total 
                        
                        # Stopping audio too
                        Rounds.PlayAudioFile(Play_file, Audio, "Stop")
                        
                        print("\n To save resources on our servers, we will guide you back to the display menu. "
                        "Please only enter the numbers displayed or you will be Alt + F4 back to the Shadowrealm 🦨")
                        time.sleep(2.0)
                        self.DisplayMenu_WNH()
                        break
            
                except ValueError:
                    print("----------------------------")
                    print(f" Invalid Input. Please try again.") 
                    print("----------------------------")
                    
                    # Subtracting Social Credit if invalid input entered
                    File_A.Social_Credit -= Social_Credit_Total 
                    
                    # Stopping audio too
                    Rounds.PlayAudioFile(Play_file, Audio, "Stop")
                    
                    print("\n To save resources on our servers, we will guide you back to the display menu. "
                    "Please only enter the numbers displayed or you will be Alt + F4 back to the Shadowrealm 🦨")
                    time.sleep(2.0)
                    self.DisplayMenu_WNH()
                    break

    def WType1_H(self, Set_of_Questions, Social_Credit_Cost, Play_file, Question_limit = 0 ):
        
        """ Summary: The purpose of this function is to create the functionality for Type_1 Waffle rounds 
        
        HINTS: ❌
        WAFFLE: ✔
        
        """
 
        """ Question Limit: Increments by 1 so that when it reaches the same number as the length of the 
                            set of questions, the round stops and the final results are displayed.
                    
            Current Score:  The Current Score of the user during a round. 
            
            Social_Credit_Total: This records how much Social Credit the user earns during a round. This is
                                 then displayed at the end of the round. 
                                 
            Score_Percentage: This records the Current Score of the user at the end of the round as a percentage.
                              This will be displayed at the end of the round and will be used to indicate the
                              user's strengths/weaknesses for each difficulty.
                              
            Audio list: This stores the names of all Audio files to be used so that they can be played whenever
                        they're called.        
                        
            Play_file: This is used to play the audio files as a placeholder for self.Playback          
        """
        
        Current_Score = 0
        Social_Credit_Total = 0
        Score_Percentage = 0.0
        
        while Question_limit < len(Set_of_Questions):
            
            for Question in Set_of_Questions:
                question_text = Question.get("Question")
                hint_text = Question.get("Hint")
                
                print("-" * 100)
                print(question_text)
                print(f"\n Hint: {hint_text} ")
                
                # Playing audio here
                Audio = random.choice(self.AudioList_W1)
                
                try:
                    user_answer = int(input(f"\n Enter the correct number: "))
                    correct_answer = Question.get("Answer")
                    
                    if user_answer == correct_answer:
                        
                        """ What will happen if the user gets the question right
                        
                        Social Credit increases by the pre-determined Social_Credit_Cost, CurrentScore increases by 1
                        and Social_Credit_Total increases too. Finally, the Question_Limit increases by 1
                        
                        """
                        # Stopping Waffle if answer is right
                        if Play_file.active:
                            Rounds.PlayAudioFile(Play_file, Audio,"Stop")
                        else:
                            Rounds.PlayAudioFile(Play_file, Audio,"Stop")
                        
                        File_A.Social_Credit +=  Social_Credit_Cost
                        Current_Score += 1
                        Social_Credit_Total += Social_Credit_Cost
                        Question_limit += 1
                        
                        # Returning Current score to the user
                        print(f"\n Your Score: {Current_Score} / {len(Set_of_Questions)}")
                        print("-" * 100)
            
                    if user_answer != correct_answer:
                        
                        """ What will happen if the user gets the question wrong
                        
                        Social Credit decreases by the pre-determined Social_Credit_Cost,and Social_Credit_Total 
                        decreases too. Finally, the Question_Limit increases by 1
                        
                        """
                        # Playing Audio if Answer Wrong
                        if Play_file.paused == False:
                            Rounds.PlayAudioFile(Play_file, Audio,"Play")
                        else:
                            Rounds.PlayAudioFile(Play_file, Audio,"Resume")
                        
                        print("\n Incorrect 😭😭😭😭😭😭😭😭😭😭😭😭 "
                                "\n You GOT THE QUESTION WRONG 💀💀💀💀💀💀💀💀")
                        
                        File_A.Social_Credit -= Social_Credit_Cost
                        Social_Credit_Total -= Social_Credit_Cost
                        Question_limit += 1
                        
                        # Returning Current score to the user
                        print(f"\n Your Score: {Current_Score} / {len(Set_of_Questions)}")
                        print("-" * 100)
                    
                    if Question_limit == len(Set_of_Questions):
                        
                        #Stopping Random Audio from playing once the round has ended
                        
                        Rounds.PlayAudioFile(Play_file, Audio, "Stop")
        
                        """ Displaying the final result... """
                        
                        Score_Percentage = (Current_Score / len(Set_of_Questions)) * 100
                                                
                        print(f"\n The Round has now officially finished!!! ")
                        
                        time.sleep(2.0)
                        
                        print(f"\n Loading up your results in ... ")
                        
                        for X in range(5,0,-1):
                            print(f"\n {X}")
                            time.sleep(1.0)
                        
                        print(f"\n Your Score: {Current_Score} / {len(Set_of_Questions)}"
                            f"\n Percentage: {Score_Percentage} "
                            f"\n Social Credit Acquired: {Social_Credit_Total} ")
                        
                        time.sleep(3.0)
                        
                        if Score_Percentage < 25.0:
                            
                            print(f"\n 💀💀💀💀💀 YOU DONE TERRIBLE 😂 YOU SHOULD GO AND REVISE..... NOW 😂")
                        
                        if Score_Percentage >= 25.0 and Score_Percentage < 50.0:
                            
                            print(f"\n You done your best and that's respectable. \n But Unfortunately, you NEED to do better. ")
                        
                        if Score_Percentage >= 50.0 and Score_Percentage < 75.0:
                            
                            print(f"\n Not bad, Not bad 👏👏👏👏👏👏 ")
                            
                        if Score_Percentage >= 75.0 and Score_Percentage <= 100:
                            
                            print(f"\n OH SORRRRY, OH SORRRRRY, Someone wants to go to Graduate Computer Science. 🦹‍♂️ ")
                           
                        File_A.CTA.Main_menu_confirm()
                        break
                    
                        
                    if type(user_answer) == int and user_answer > 4 or user_answer <= 0:
                        print("----------------------------")
                        print(f" Invalid Input. Please try again.") 
                        print("----------------------------")
                        
                        # Subtracting Social Credit if invalid input entered
                        File_A.Social_Credit -= Social_Credit_Total 
                        
                        # Stopping audio too
                        Rounds.PlayAudioFile(Play_file, Audio, "Stop")
                        
                        print("\n To save resources on our servers, we will guide you back to the display menu. "
                        "Please only enter the numbers displayed or you will be Alt + F4 back to the Shadowrealm 🦨")
                        time.sleep(2.0)
                        self.DisplayMenu_WH()
                        break
            
                except ValueError:
                    print("----------------------------")
                    print(f" Invalid Input. Please try again.") 
                    print("----------------------------")
                    
                    # Subtracting Social Credit if invalid input entered
                    File_A.Social_Credit -= Social_Credit_Total 
                    
                    # Stopping audio too
                    Rounds.PlayAudioFile(Play_file, Audio, "Stop")
                    
                    print("\n To save resources on our servers, we will guide you back to the display menu. "
                    "Please only enter the numbers displayed or you will be Alt + F4 back to the Shadowrealm 🦨")
                    time.sleep(2.0)
                    self.DisplayMenu_WH()
                    break
                 

    """ 5: Category 4: Rounds """
    
    def WType2_NH(self, Set_of_Questions, Social_Credit_Cost, Play_file, Question_limit = 0):
        
        """ Summary: The purpose of this function is to create the functionality for Type_2 Waffle rounds 
        
        HINTS: ❌
        WAFFLE: ✔
        
        """
 
        """      
            Current Score:  The Current Score of the user during a round. 
            
            Social_Credit_Total: This records how much Social Credit the user earns during a round. This is
                                 then displayed at the end of the round. 
                                 
            Score_Percentage: This records the Current Score of the user at the end of the round as a percentage.
                              This will be displayed at the end of the round and will be used to indicate the
                              user's strengths/weaknesses for each difficulty.
                              
            Audio list: This stores the names of all Audio files to be used so that they can be played whenever
                        they're called.        
                        
            Play_file: This is used to play the audio files as a placeholder for self.Playback
            
            Seconds: Used as a parameter input to indicate how long the round will be (There will be no question limit
            for these particular type of rounds)
                      
        """
        
        #Counting down to start the round 
        for I in range(3,0,-1):
            print(f"\n {I}")
            time.sleep(1.0)
        
        Current_Score = 0
        Social_Credit_Total = 0
        Score_Percentage = 0.0
        Audio = random.choice(self.AudioList_W2)
        
        while Question_limit < len(Set_of_Questions):
            
            #Play Audio
            self.PlayAudioFile(Play_file,Audio,"Play")
            
            for Question in Set_of_Questions:
                question_text = Question.get("Question")
                print("-" * 100)
                print(question_text)
                    
                try: 
                    
                    user_answer = int(input(f"\n Enter the correct number: "))
                    correct_answer = Question.get("Answer")
                
                    if user_answer == correct_answer:
                        
                        """ What will happen if the user gets the question right
                        
                        Social Credit increases by the pre-determined Social_Credit_Cost, CurrentScore increases by 1
                        and Social_Credit_Total increases too. Finally, the Question_Limit increases by 1
                        
                        """
                        
                        File_A.Social_Credit +=  Social_Credit_Cost / 2
                        Current_Score += 1
                        Social_Credit_Total += Social_Credit_Cost / 2
                        Question_limit += 1
                        
                        # Returning Current score to the user
                        print(f"\n Your Score: {Current_Score} / {len(Set_of_Questions)}")
                        print("-" * 100)
            
                    if user_answer != correct_answer:
                        
                        """ What will happen if the user gets the question wrong
                        
                        Social Credit decreases by the pre-determined Social_Credit_Cost,and Social_Credit_Total 
                        decreases too. Finally, the Question_Limit increases by 1
                        
                        """
                        
                        print("\n Incorrect 😭😭😭😭😭😭😭😭😭😭😭😭 "
                                "\n You GOT THE QUESTION WRONG 💀💀💀💀💀💀💀💀")
                        
                        File_A.Social_Credit -= Social_Credit_Cost 
                        Social_Credit_Total -= Social_Credit_Cost 

                        Question_limit += 1
                        
                        # Returning Current score to the user
                        print(f"\n Your Score: {Current_Score} / {len(Set_of_Questions)}")
                        print("-" * 100)

                        
                    if Question_limit == len(Set_of_Questions):

                        """ Displaying the final result... """
                        
                        #Stop Audio
                        self.PlayAudioFile(Play_file, Audio, "Stop")
                        
                        Score_Percentage = (Current_Score / len(Set_of_Questions)) * 100
                                                
                        print(f"\n The Round has now officially finished!!! ")
                        
                        time.sleep(2.0)
                        
                        print(f"\n Loading up your results in ... ")
                        
                        for X in range(5,0,-1):
                            print(f"\n{X}")
                            time.sleep(1.0)
                        
                        print(f"\n Your Score: {Current_Score} / {len(Set_of_Questions)}"
                            f"\n Percentage: {Score_Percentage} "
                            f"\n Social Credit Acquired: {Social_Credit_Total} ")
                        
                        time.sleep(3.0)
                        
                        if Score_Percentage < 25.0:
                            
                            print(f"\n 💀💀💀💀💀 YOU DONE TERRIBLE 😂 YOU SHOULD GO AND REVISE..... NOW 😂")
                        
                        if Score_Percentage >= 25.0 and Score_Percentage < 50.0:
                            
                            print(f"\n You done your best and that's respectable. \n But Unfortunately, you NEED to do better. ")
                        
                        if Score_Percentage >= 50.0 and Score_Percentage < 75.0:
                            
                            print(f"\n Not bad, Not bad 👏👏👏👏👏👏 ")
                            
                        if Score_Percentage >= 75.0 and Score_Percentage <= 100:
                            
                            print(f"\n OH SORRRRY, OH SORRRRRY, Someone wants to go to Graduate Computer Science. 🦹‍♂️ ")
                            
                        File_A.CTA.Main_menu_confirm()
                        break     
                    
                    
                    if type(user_answer) == int and user_answer > 4 or user_answer <= 0:
                        print("----------------------------")
                        print(f" Invalid Input. Please try again.") 
                        print("----------------------------")
                        
                        # Subtracting Social Credit if invalid input entered
                        File_A.Social_Credit -= Social_Credit_Total 
                        
                        # Stopping audio too
                        Rounds.PlayAudioFile(Play_file, Audio, "Stop") 
                        
                        print("\n To save resources on our servers, we will guide you back to the display menu. "
                        "Please only enter the numbers displayed or you will be Alt + F4 back to the Shadowrealm 🦨")
                        time.sleep(2.0)
                        self.DisplayMenu()
                        break
            
                except ValueError:
                    print("----------------------------")
                    print(f" Invalid Input. Please try again.") 
                    print("----------------------------")
                    
                    # Subtracting Social Credit if invalid input entered
                    File_A.Social_Credit -= Social_Credit_Total 
                    
                    # Stopping audio too
                    Rounds.PlayAudioFile(Play_file, Audio, "Stop")
                    
                    print("\n To save resources on our servers, we will guide you back to the display menu. "
                    "Please only enter the numbers displayed or you will be Alt + F4 back to the Shadowrealm 🦨")
                    time.sleep(2.0)
                    self.DisplayMenu()
                    break       
    
    
    def WType2_H(self, Set_of_Questions, Social_Credit_Cost, Play_file, Question_limit = 0):
        
        """ Summary: The purpose of this function is to create the functionality for Type_2 Waffle rounds 
        
        HINTS: ❌
        WAFFLE: ✔
        
        """
 
        """      
            Current Score:  The Current Score of the user during a round. 
            
            Social_Credit_Total: This records how much Social Credit the user earns during a round. This is
                                 then displayed at the end of the round. 
                                 
            Score_Percentage: This records the Current Score of the user at the end of the round as a percentage.
                              This will be displayed at the end of the round and will be used to indicate the
                              user's strengths/weaknesses for each difficulty.
                              
            Audio list: This stores the names of all Audio files to be used so that they can be played whenever
                        they're called.        
                        
            Play_file: This is used to play the audio files as a placeholder for self.Playback
            
            Seconds: Used as a parameter input to indicate how long the round will be (There will be no question limit
            for these particular type of rounds)
                      
        """
        
        #Counting down to start the round 
        for I in range(3,0,-1):
            print(f"\n {I}")
            time.sleep(1.0)
        
        Current_Score = 0
        Social_Credit_Total = 0
        Score_Percentage = 0.0
        #Playing audio here
        Audio = random.choice(self.AudioList_W2)
        
        while Question_limit < len(Set_of_Questions):
            
            #Play Audio
            Rounds.PlayAudioFile(Play_file,Audio,"Play")
             
            for Question in Set_of_Questions:
                question_text = Question.get("Question")
                hint_text = Question.get("Hint")
                
                print("-" * 100)
                print(question_text)
                print(f"\n Hint: {hint_text}")
                    
                try: 
                    
                    user_answer = int(input(f"\n Enter the correct number: "))
                    correct_answer = Question.get("Answer")
                
                    if user_answer == correct_answer:
                        
                        """ What will happen if the user gets the question right
                        
                        Social Credit increases by the pre-determined Social_Credit_Cost, CurrentScore increases by 1
                        and Social_Credit_Total increases too. Finally, the Question_Limit increases by 1
                        
                        """
                        
                        File_A.Social_Credit +=  Social_Credit_Cost
                        Current_Score += 1
                        Social_Credit_Total += Social_Credit_Cost
                        Question_limit += 1
                        
                        # Returning Current score to the user
                        print(f"\n Your Score: {Current_Score} / {len(Set_of_Questions)}")
                        print("-" * 100)
            
                    if user_answer != correct_answer:
                        
                        """ What will happen if the user gets the question wrong
                        
                        Social Credit decreases by the pre-determined Social_Credit_Cost,and Social_Credit_Total 
                        decreases too. Finally, the Question_Limit increases by 1
                        
                        """
                        
                        print("\n Incorrect 😭😭😭😭😭😭😭😭😭😭😭😭 "
                                "\n You GOT THE QUESTION WRONG 💀💀💀💀💀💀💀💀")
                        
                        File_A.Social_Credit -= Social_Credit_Cost
                        Social_Credit_Total -= Social_Credit_Cost

                        Question_limit += 1
                        
                        # Returning Current score to the user
                        print(f"\n Your Score: {Current_Score} / {len(Set_of_Questions)}")
                        print("-" * 100)

                        
                    if Question_limit == len(Set_of_Questions):

                        """ Displaying the final result... """
                        
                        #Stop Audio
                        Rounds.PlayAudioFile(Play_file, Audio, "Stop")
                        
                        Score_Percentage = (Current_Score / len(Set_of_Questions)) * 100
                                                
                        print(f"\n The Round has now officially finished!!! ")
                        
                        time.sleep(2.0)
                        
                        print(f"\n Loading up your results in ... ")
                        
                        for X in range(5,0,-1):
                            print(f"\n{X}")
                            time.sleep(1.0)
                        
                        print(f"\n Your Score: {Current_Score} / {len(Set_of_Questions)}"
                            f"\n Percentage: {Score_Percentage} "
                            f"\n Social Credit Acquired: {Social_Credit_Total} ")
                        
                        time.sleep(3.0)
                        
                        if Score_Percentage < 25.0:
                            
                            print(f"\n 💀💀💀💀💀 YOU DONE TERRIBLE 😂 YOU SHOULD GO AND REVISE..... NOW 😂")
                        
                        if Score_Percentage >= 25.0 and Score_Percentage < 50.0:
                            
                            print(f"\n You done your best and that's respectable. \n But Unfortunately, you NEED to do better. ")
                        
                        if Score_Percentage >= 50.0 and Score_Percentage < 75.0:
                            
                            print(f"\n Not bad, Not bad 👏👏👏👏👏👏 ")
                            
                        if Score_Percentage >= 75.0 and Score_Percentage <= 100:
                            
                            print(f"\n OH SORRRRY, OH SORRRRRY, Someone wants to go to Graduate Computer Science. 🦹‍♂️ ")
                            
                        File_A.CTA.Main_menu_confirm()
                        break     
                    
                    
                    if type(user_answer) == int and user_answer > 4 or user_answer <= 0:
                        print("----------------------------")
                        print(f" Invalid Input. Please try again.") 
                        print("----------------------------")
                        
                        # Subtracting Social Credit if invalid input entered
                        File_A.Social_Credit -= Social_Credit_Total 
                        
                        # Stopping audio too
                        Rounds.PlayAudioFile(Play_file, Audio, "Stop")
                        
                        print("\n To save resources on our servers, we will guide you back to the display menu. "
                        "Please only enter the numbers displayed or you will be Alt + F4 back to the Shadowrealm 🦨")
                        time.sleep(2.0)
                        self.DisplayMenu()
                        break
            
                except ValueError:
                    print("----------------------------")
                    print(f" Invalid Input. Please try again.") 
                    print("----------------------------")
                    
                    # Subtracting Social Credit if invalid input entered
                    File_A.Social_Credit -= Social_Credit_Total 
                    
                    # Stopping audio too
                    Rounds.PlayAudioFile(Play_file, Audio, "Stop")
                    
                    print("\n To save resources on our servers, we will guide you back to the display menu. "
                    "Please only enter the numbers displayed or you will be Alt + F4 back to the Shadowrealm 🦨")
                    time.sleep(2.0)
                    self.DisplayMenu()
                    break       

"""---------------------------------------------------Class Rounds---------------------------------------------------"""

