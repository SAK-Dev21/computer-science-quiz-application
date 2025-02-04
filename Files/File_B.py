# E = Easy, M = Medium, H = Hard, T = Tryhard'

# [Insert Difficulty]_Options_[insert Question Number] - E.G: EOptions1  = The Options presented in a question

"""
  "Question" :            
  "Answer" :  
  "Hint" :   
"""

"""--------------------------------------Fundamentals of Data Representation-----------------------------------"""

# Topic 1 = Fundamentals of Data Representation. This class is just created to organise variables 😭

class Topic1: 


  """.............................................Easy Difficulty................................................"""


  EOptions1_FODR = """ 
 1: A number that can be expressed as a fraction, with the numerator and denominator as integers, not including 0
 2: A number that can be expressed as a fraction, with the numerator and dendenominatoromainator as integers, including 0 
                   """
              
  EOptions2_FODR = """ 
 1: Because all integers can be expressed as a fraction with 1 as the denominator
 2: Because all integers can be expressed as a fraction with 0 as the denominator
                   """
                   
  EOptions3_FODR = """ 
 1: Yes
 2: No           """
 
  EOptions4_FODR = """ 
 1: 14
 2: 7
  """
  
  EOptions5_FODR = """
 1: Rational
 2: Integer
 3: Irrational
  """
                    
  EOptions6_FODR = """
 1: Integer
 2: Float
 3: Rational 
  """
  
  EOptions7_FODR = """
 1: Compression which largely reduces the size of the file albeit permanently 
 2: Compression which moderately reduces the size of the file but the quality can be restored
 3: Compression which largely reduces the size of the file but the quality can be restored. 
 4: Compression which moderately reduces the size of the file albeit permanently.
  """
  EOptions8_FODR = """
 1: Compression which largely reduces the size of the file albeit permanently 
 2: Compression which moderately reduces the size of the file but the quality can be restored
 3: Compression which largely reduces the size of the file but the quality can be restored. 
 4: Compression which moderately reduces the size of the file albeit permanently.
  """
  
  EOptions9_FODR = """
 1: Name
 2: File Type
 3: Date/Time Settings
 4: Bits per pixel 
  
  """
  
  EOptions10_FODR = """
 1: True
 2: False
 
  """
  

  FODR_EasyQuestions = [
                      {
                      "Question" : f"\n 1. Describe what a rational number is: \n " + EOptions1_FODR,
                      "Answer" : 2,
                      "Hint" : "\n Example of Rational Number: 3/4"
                      },
                      {
                      "Question" : f"\n 2. Explain why all integers are rational numbers: \n " + EOptions2_FODR,
                      "Answer" : 1, 
                      "Hint" : "\n What do all Integers have in common?"
                      },
                      {
                      "Question" : "\n 3. Is 0 a Natural number? \n " + EOptions3_FODR,
                      "Answer" : 2,
                      "Hint" : "\n Is 0 a negative number? "
                      },
                      {
                      "Question" : "\n 4. What is the smallest positive integer that is evenly divisible by 7? \n " + EOptions4_FODR,
                      "Answer" : 1,
                      "Hint" : "\n What is the smallest positive integer that is evenly divisible by 7?"
                      },
                      {
                      "Question" : "\n 5. What kind of number is √5? \n " + EOptions5_FODR,
                      "Answer" : 3,
                      "Hint" : "\n How can you represent √5 as a fraction?"
                      },
                      {
                      "Question" : "\n 6. What kind of number is 10? \n " + EOptions6_FODR,
                      "Answer" : 1,
                      "Hint" : "\n 10 can be represented as all 3... But how would you generally write 10?"   
                      },
                      {
                      "Question" : "\n 7. What is lossy compression?" + EOptions7_FODR,           
                      "Answer" :  1,
                      "Hint" :  "\n Think of the suffix of... Lossy"
                      },
                      {
                      "Question" : "\n 8. What is loseless compression?" + EOptions8_FODR,                      
                      "Answer" : 2,
                      "Hint" : "\n Think of the suffix of... Loseless"
                      },
                      {
                      "Question" : "\n 9. Select the false example of metadata:" + EOptions9_FODR,           
                      "Answer" : 4 ,
                      "Hint" : "\n Imagine yourself opening the properties of a file. What options look like something you'd see?"  
                      }, 
                      {
                      "Question" : "\n 10. True or False? \n The Vernon cipher is more secure than the Caesar cipher?" + EOptions10_FODR,           
                      "Answer" : 1,
                      "Hint" : "What cipher between these two is more used in today's day and age and why?"    
                      }
                      ]
  
  """.............................................Medium Difficulty.............................................."""

  MOptions1_FODR = """
 1: 01101000 
 2: 01100110 
 3: 01101000     """


  MOptions2_FODR = """
1: 57 
2: 59 
3: 53         """

  MOptions3_FODR = """
1: MAC addresses 
2: Encryption 
3: Binary Translation """

  MOptions4_FODR = """
1: Because it saves time 
2: Because it reduces compiling time
3: Because it is easier for us humans to read data as opposed to binary """
  
  MOptions5_FODR = """
1: 228
2: 218
3: 224 """

  MOptions6_FODR = """
 1: Pattern recognition is easier to identify with the Caesar cipher. For instance, it only takes some letters to be cracked 
    from ciphertext to plaintext for the whole encrypted text to be discovered. This is because the cipher works via 
    a shift of letters in the alphabet - in which there are maximum 25/26 combinations. 
 2: Each Plaintext letter is always converted to the same letter with the Caesar cipher. With the Vernam cipher, there 
    is a uniform probability that different plaintext letters can map to the same ciphertext letter.
 3: All of the above
  
  """
  
  MOptions7_FODR = """
 1: True 
 2: False 
 
  """
  MOptions8_FODR = """
 1: True 
 2: False
  """
  MOptions9_FODR = """
 1: The Key exchange problem is how to exchange keys securely on any platform
 2: The Key exchange problem is how to exchange keys used between 2 or more entities to decrypt/encrypt files 
    on any platform
 3: The Key exchange problem is how to exchange keys used between 2 or more entities to decrypt/encrypt files 
    on communication mediums
 4: The Key exchange problem is how to exchange keys used between 2 or more entities to decrypt/encrypt files 
    on communication mediums \n without the keys being intercepted
  """

  MOptions10_FODR = """
 1: Asymmetric encryption is the process of using a public encryption key only to exchange files securely.
    Symmetric encryption involves using a public encryption key and a private encryption key to exchange files securely.
 2: Asymmetric encryption is the process of using a private encryption key and a public encryption key to exchange files securely.
    Symmetric encryption involves using a public encryption key only to exchange files securely.
  """

  FODR_MediumQuestions = [
                        {
                        "Question" : "\n 1. What is the Binary equivalant of the decimal number 102? \n" + MOptions1_FODR,
                        "Answer" : 2,
                        "Hint": "Think of the different methods to convert binary to decimal and vice versa. Use the binary table for instance"
                        },
                        {
                        "Question" : "\n 2. What is the Hexadecimal equivalent of the decimal number 87? \n" + MOptions2_FODR, 
                        "Answer" : 1,
                        "Hint" : "Think of the different methods to convert decimal to hexadecimal and vice versa."
                        },
                        {
                        "Question" : "\n 3. Which of the following are examples of uses of Hexadecimal notation? \n" + MOptions3_FODR,
                        "Answer" : 1,
                        "Hint" : "Its not 00001111 😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭"  
                        },
                        {
                        "Question" : "\n 4. Why do Programmers use Hexadecimal instead of Binary to represent Bit Patterns? \n" + MOptions4_FODR,
                        "Answer" : 3,
                        "Hint" : "Why does Binary look like Martian Hieroglyphics combined with Russian Sanscript?" 
                        },
                        {
                        "Question" : "\n 5. What is the Denary representation of the Hexadecimal number E4? \n" + MOptions5_FODR,
                        "Answer" : 1,
                        "Hint" : "The Big Bang Theory 🚀 . \n \n No seriously, think of the 16 time tables."
                        },
                        {
                        "Question" : "\n 6. Which reason is True as to why the Vernam cipher is more secure than the Caesar cypher \n " + MOptions6_FODR,           
                        "Answer" : 3,
                        "Hint" :  "Think about how the Vernam cipher works. In what ways is it better than the Caesar cipher?"   
                        },
                        {
                        "Question" : "\n 7. True or False. One advantage of Vector graphics is that you can use any image editing tool to edit the pixels \n " + MOptions7_FODR,          
                        "Answer" : 2, 
                        "Hint" : "\n Imagine you're using Adobe Photoshop to edit the Nike Logo (an example of a vector image). \n What editing tools can you use that can make changes to the logo? "
                        },
                        {
                        "Question" : "\n 8. True or False. One disadvantage of Vector graphics is that you can't manipulate all the objects in an image \n " + MOptions8_FODR,            
                        "Answer" : 2,  
                        "Hint" : "What is an object in a vector image? \n Can you do anything with it?"     
                        },
                        {
                        "Question" : "\n 9. What is the Key Exchange Problem? \n" + MOptions9_FODR,                     
                        "Answer" : 4, 
                        "Hint" : "What is THE MOST IMPORTANT concept in encryption with cryptography keys?."   
                        },
                        {
                        "Question" : "\n 10. What is Asymmetric and Symmetric encryption? \n" + MOptions10_FODR,           
                        "Answer" : 2,
                        "Hint" : "The Key Exchange Problem."  
                        },
                        ]



  """................................................Hard Difficulty............................................."""

  HOptions1_FODR = """ 
1: 00100100
2: 01010011
3: 00001100
4: 00011011 """

  HOptions2_FODR = """ 
1: 128 
2: 127
3: 63
4: 64 """

  HOptions3_FODR = """ 
1: -3 
2: -4
3: 2.5
4: -2/5 """

  HOptions4_FODR = """ 
1: Reduced Precision, Increased Range
2: Reduced Precision, Reduced Range
3: Increased Precision, Reduced Range
4: Increased Precision, Increased Range """

  HOptions5_FODR = """ 
1: Normalised form allows for maximimum accuracy within a given number of bits
2: Normalised form allows for data to not be redundant   
3: Normalised form allows for a unique representation of each number 
  """
  HOptions6_FODR = """
Run-length encoding works as follows:
- For every general colour noticed, assign a binary number to said colour
- Then assign a 'count' variable to count how many instances of said colour were found
- Then merge all general colours found together to form a compressed version of the original image. 

1: True
2: False
  
  """
  
  HOptions7_FODR = """
  
1: 16.5 Mb
2: 17.3 Mb
3: 21.1 Mb -> (Can you do something for me?)
4: 4.2 Mb 
 
  """  
  
  HOptions8_FODR = """
  A) The heights/amplitudes of the samples are measured accordingly.
  B) Each sample is then assigned a particular binary value based on their amplitudes.
  C) The ADC takes samples of the analogue sound at regular intervals
  
  1: BAC
  2: ABC
  3: CBA
  4: CAB
  """
  HOptions9_FODR = """
  1: There is No loss of quality when compressing a file
  2: The quality of a file can be restored if desired
  3: Loseless compression results in redundant data

  """

  HOptions10_FODR = """

  A) A key can only be used a maximum of 2 times
  B) The key(s) must be random
  C) The key(s) must only be known between the entities and no one else
  D) The key must be transferred as quickly as possible between entities. 

  1: ADC
  2: BC
  3: DBA
  4: CD

  """



  FODR_HardQuestions = [
                    {
                    "Question" : "\n 1. What is the answer to this Binary Multiplication: 00001001 * 00000011? \n" + HOptions1_FODR,
                    "Answer" : 4,
                    "Hint" : "What's 0 * 0? What's 0 * 1? What's 1 * 0? What's 1 * 1? \n How does Column Multiplication work? "
                    },
                    {
                    "Question" : "\n 2. A number is to be represented using 7 bits and Two's complement. \n What is the largest positive number that can be represented using this representation? \n " + HOptions2_FODR,
                    "Answer" : 3,
                    "Hint" : "If the most significant bit of this number is 0 or 1, what does this mean for each case?"
                    },
                    {
                    "Question" : "\n 3. This number is a floating representation of another number: \n Mantissa: 1.0110000 \n Exponent: 0010 \n Calculate the denary equivalent of this number: \n " + HOptions3_FODR,
                    "Answer" : 4,
                    "Hint" : "A new number is determined by the exponent. If it is positive or negative, how is the mantissa affected and what happens to it?"
                    },
                    {
                    "Question" : "\n 4. What are the effects of using a 7 bit Mantissa 5 bit Exponent as opposed to an 8 bit Mantissa 3 Bit Exponent? \n" + HOptions4_FODR,
                    "Answer" : 1,
                    "Hint" : "Think of Range and Precision respectively."
                    },
                    {
                    "Question" : "\n 5. The following options are advantages of normalised representation. State which option is the false statement: \n" + HOptions5_FODR,
                    "Answer" : 2,
                    "Hint" : "There are no hints for this one. Good luck 💀"
                    },
                    {
                    "Question" : "\n 6. Is the following statement about Run-length encoding True or False? \n" + HOptions6_FODR,         
                    "Answer" : 1, 
                    "Hint" : "Why do the colours in an image after Run-length encoding look the same as opposed to before the image? \n"
                    },
                    {
                    "Question" : "\n 7. Your very host, DR S.Khan, made a 3 minute song about creating a cooking recipe using Samsung Earphones and radioactive Samosas to " 
                                  "Experiment on Ancient Petri Dishes. \n His Microphone, the Blue yeti, uses 16 bits to record audio as its sample resolution."
                                  "The sample rate of this track is 48.1 kHz. \n Calculate the size of this file? -> (to 3sf) " + HOptions7_FODR,          
                    "Answer" : 2,
                    "Hint" : "Remember, 8 bits = 1 byte."
                    },
                    {
                    "Question" : "\n 8. I need your help in correctly ordering the statements by number on how sound is "
                    "converted from an analogue to digital converter (ADC). Which order of numbers is correct? \n" + HOptions8_FODR,            
                    "Answer" : 4, 
                    "Hint" : "💀 NO HINTS FOR YOU HAHAHAHA 🤣🤣🤣🤣"
                    },
                    {
                    "Question" : "\n 9. Which is the True statement about loseless compression? \n" + HOptions9_FODR,           
                    "Answer" : 2, 
                    "Hint" : "Think carefully with this question."
                    },
                    {
                    "Question" : "\n 10. With each statement, enter the correct numbers on what a cipher must have in "
                    " order to achieve 'Perfect' security? \n" + HOptions10_FODR,                       
                    "Answer" : 2, 
                    "Hint" : "Visualise a data transmission being encrypted using keys. How could this work as best as possible?"
                    }
                    ]


  """.............................................Tryhard Difficulty............................................."""

  TOptions1_FODR = """ 
1: Odd Parity is a form of parity check during data transmission where the most significant bit is 0 
2: Odd Parity checks for an Odd number of 1s to see if the data received during transmission is correct. 
3: Odd Parity is more efficient than Even Parity.
4: Odd parity will work for more than 1 binary numbers received during data transmission.
"""

  TOptions2_FODR = """ 
1: Unicode is composed of 16 bits whilst ASCII composes of 7 bits, Extended Ascii being 8 bits 
2: Unicode allows for a range of symbols, characters and numbers of a variety numbers to be represented digitally across multiple languages
3: Unicode costs more bandwidth than ASCII during data transmission as it has more bits
4: Unicode has completely replaced Ascii/Extended Ascii """ 

  TOptions3_FODR = """ 
1: True
2: False """

  TOptions4_FODR = """ 
1: True
2: False """

  TOptions5_FODR = """ 
1: Majority Voting prevents Redundant data. \n This is because at the end of data transmission, it discards all the bits that aren't the 'correct' value based on its frequency.
2: Majority Voting can correct and identify data. \n This is because the majority bits are recognised and considered as the 'correct' value, leaving the minority bits discarded 
3: Majority Voting takes a shorter amount of time to debug errors during data transmission than parity bits. \n This is because, unlike parity bits, it doesn't crash if errors are discovered on more than one bit that was received."""

  TOptions6_FODR = """

1: Asymmetric Encryption uses a public and private key for encryption and decryption 
   whilst Symmetric Encryption only uses the same key
2: Asymmetric Encryption uses two different keys for encryption whilst Symmetric Encryption only uses a public key
3: Asymmetric Encryption uses a public and private key for encryption and decryption whilst 
   Symmetric Encryption only uses a public key for encryption
4: Asymmetric Encryption uses two different keys for encryption whilst Symmetric Encryption uses the same key. 

"""
  TOptions7_FODR = """

1: True
2: False

"""

  TOptions8_FODR = """

1: Music is represented as a series of MIDI event messages. Examples include pitch, volume, audio effects. 
2: Music is represented as pre-recorded sample sound. You can then apply effects such as equalisation, pitch, verbosity. 
3: Music is represented as computer generated sound. You can change the value of bits to apply audio effects like the following above.
"""

  TOptions9_FODR = """

1: It is easy to edit notes and modify values for different effects. E.G: Db level for Volume
2: MIDI is more compact to represent music 
3: It is more portable to use MIDI as opposed to sampled sound. 
4: MIDI is easier to record music than sampled sound. 

"""

  FODR_TryhardQuestions = [
                        {
                        "Question" : "\n 1. Select the True statement about Odd Parity: \n" + TOptions1_FODR,
                        "Answer" : 2
                        },
                        {
                        "Question" : "\n 2. Select the False Statement about Unicode: \n" + TOptions2_FODR,
                        "Answer" : 4
                        },
                        {
                        "Question" : "\n 3. To calculate the parity bit of a 8 bit binary number using the Even parity system, \n you count the amount of 1s in the binary number to see if it is an even amount. \n If yes, the most significant bit is 1. \n Else, the most significant bit is 0. \n Is this statement True or False? \n " + TOptions3_FODR, 
                        "Answer" : 1  
                        },
                        {
                        "Question" : "\n 4. Each bit is sent multiple times during transmission. \n The receiving device, if all bits are the same, checks the bit with the most amount of copies and assumes that it is the correct value.   \n Is this statement about Majority voting True or False? \n " + TOptions4_FODR,
                        "Answer" : 2  
                        },
                        {
                        "Question" : "\n 5. Which of the following is an advantage of Majority Voting? \n" + TOptions5_FODR,
                        "Answer" : 2
                        },
                        {
                        "Question" :  "\n 6. What is the difference between Asymmetric Encryption and Symmetric Encryption? \n" + TOptions6_FODR,           
                        "Answer" : 4
                        },
                        {
                        "Question" : "\n 7. True or False. Nyquist's theorem is that the sample rate must be at least "
                        "double the highest frequency component in a sample. \n With this in mind, if I have a sample rate"
                        "of 44,100 Hz and the average frequency of a sample is 22,100. Will this be enough to produce a "
                        "good reproduction of PURE QUALLLITY SOUND? \n" + TOptions7_FODR,           
                        "Answer" : 2
                        },
                        {
                        "Question" : "\n 8. How does MIDI represent music? \n" + TOptions8_FODR,                     
                        "Answer" : 1
                        },
                        {
                        "Question" : "\n 9. List an advantage of using MIDI to represent music instead of sampled sound? \n" + TOptions9_FODR,            
                        "\n Enter your answer as numbers together: E.G: "
                        "Answer" : 1 or 2
                        } 
                        ]