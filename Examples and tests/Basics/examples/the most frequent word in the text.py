punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
# Текст, который можно использовать в качестве примера:
text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."

def get_most_frequent_word(text):
    
    # removing punctuation marks
    
    for a in punctuation_list:
        text=text.replace (a,'')
    
     # We bring all the letters to the same format
            
    text=text.lower()
    text=text.split()
    # Adding letters to the dictionary
    text_dict={}
    
    for b in text:
        if b in text_dict:
            text_dict[b]+=1
        else: 
            text_dict.update ({b:1})
  
    # We find the letter that is mentioned more often
    n=0
    key=''
    for c in text_dict:
        if text_dict[c]>n:
            n = text_dict[c]
            key = c    
    return key
    

print(get_most_frequent_word(text_example))

