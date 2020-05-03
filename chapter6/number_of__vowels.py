

def vowel_counter(words):
       total_vowel = 0
       total_consonant = 0
       for indx, vowel in enumerate(words):
            if vowel == 'a':
                total_vowel += 1
                print(total_vowel, vowel)
            else:
                total_consonant += 1 
                print(total_consonant, vowel)            

sentence = input("Enter a sentence: ")

vowel_counter(sentence)







