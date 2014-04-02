'''
Created on Mar 24, 2014

@author: bonino
'''
import string, re, random

def build_mimic(text):
    '''
    Builds a mimic dictionary from the given text
    '''
    
    # to lower case
    text = string.lower(text)
    
    # clean
    text = re.sub("\\W", " ", text)
    text = re.sub("\s+", " ", text)
    
    # split in words
    words = text.split(" ")
    
    # the mimic vocabulary
    mimic_vocabulary = {} 
    
    for i in range(1, len(words)):
        # get the list of words associated to the current word
        next_words = mimic_vocabulary.get(words[i - 1])
        
        # check not empty
        if(next_words != None):
            # update the list
            next_words.append(words[i])
        else:
            mimic_vocabulary[words[i - 1]] = [words[i]]

    
    return mimic_vocabulary
        
            
def get_mimic_text(mimic_vocabulary, seed_word, word_count):
    '''
    Given a seed word, a word count and a mimic vocabulary generates a 
    mimicked text as long as word_count starting from the given seed_word
    '''
    # initialize the resulting word
    resulting_text = seed_word
    
    # get the next seeds
    next_seeds = mimic_vocabulary.get(seed_word);
    
    # if there are seeds continue
    if(next_seeds != None):
        # counter
        i = 0
        
        # do until the included word count is equal to the required one
        while i < word_count:
            
            # get the next seed
            seed = random.choice(next_seeds)
            # get the next set of following words
            next_seeds = mimic_vocabulary.get(seed)
            # compose the mimicked text
            resulting_text = resulting_text + " " + seed
            # update the counter
            i += 1
            
            # check if the generation should stop here 
            if(next_seeds == None):
                break
        
    return resulting_text
                    
    

if __name__ == '__main__':
    
    #open the file
    txt_file = open("alice.txt")
    
    #build the mimic vocabulary
    mimic_voc = build_mimic(txt_file.read())
    
    #read seeds and generate texts until exit
    seed=""
    while(seed!="exit"):
        #get the seed word
        seed = raw_input("Insert seed:\n>")
        #print the mimicked text
        print get_mimic_text(mimic_voc, seed, 40)
