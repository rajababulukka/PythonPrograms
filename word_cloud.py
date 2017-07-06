def count_words(string):
    punctuation = {',':True,'.':True,':':True,' ':True,'!':True,'?':True,';':True,'-':True}
    word_to_count={}
    first_index=0
    
    for index in range(len(string)):
        if string[index] in punctuation:
            word=string[first_index:index].lower()
            #print("Word",word)
            if word=='':
                continue
            word_to_count[word]=word_to_count.get(word,0)+1
            first_index=index+1
    return word_to_count

string="After beating the eggs, Dana read the next step: Add milk and eggs, then add flour and sugar."
print(count_words(string))

            
            
