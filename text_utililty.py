def remove_white_spaces(text):
    '''Returns a copy with the white spaces(more than one) removed
    text: The text/paragraph/string'''
    return " ".join(text.split())

def remove_refs(text):
    '''Returns  a copy with all the refrences removed
    text: The text/paragraph/string'''
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    open_bracket = text.find("[")
    cleaned_text = text
    while(open_bracket != -1):
        close_bracket = cleaned_text.find("]", open_bracket + 1)
        ref_found = True
        if(close_bracket != -1):
            for char in cleaned_text[open_bracket + 1: close_bracket]:
                if (char not in punctuations) and not char.isdigit():
                    ref_found = False
            if (ref_found == True):
                cleaned_text = cleaned_text[:open_bracket] + cleaned_text[close_bracket + 1:]
                open_bracket = cleaned_text.find("[")
            else:
                open_bracket = cleaned_text.find("[", close_bracket + 1)
    return cleaned_text

def remove_punct(text):
    '''Returns  a copy with all the punctuations removed
    text: The text/paragraph/string'''
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    cleaned_text = text
    for punctuation in punctuations:
        cleaned_text = cleaned_text.replace(punctuation, "")
    return cleaned_text


def bag_of_words(text):
    '''Returns a dictionary with all the words of the text as key and number of occurences of that word as value
    text: The text/paragraph/string'''
#     words = {word: "h" if(word in words) else 1 for word in text.split(" ")}
    cleaned_text = remove_refs(text)
    cleaned_text = remove_punct(cleaned_text)
    words = {}
    for word in cleaned_text.split():
        if(word in words):
            words[word] += 1
        else:
            words[word] = 1
       
    def return_val(dict_item):
        return dict_item[1]
    
    return {item[0]: item[1] for item in sorted(words.items(), key=return_val, reverse=True)}

def find_all_substr(text, substring):
    '''Returns a list of the indexes of all occurences of the provided substring
    text: The text/paragraph/string to be searched upon
    substring: the substring to be found'''
    all_ind = []
    para = text.lower()
    substr = substring.lower()
    last_ind = para.find(substr, 0)
    while(last_ind != -1):
        all_ind.append(last_ind)
        last_ind = para.find(substr, last_ind + 1)
    return all_ind

def find_best_match(text, string_to_search):
    '''Returns a dictionary containg all the words, their positions, how much they match with the searched string and count of how many matching words/phrases found
    text: The text/paragraph/string to be searched upon
    string_to_search: The string/phrase to be searched'''
    search_str = string_to_search
    searched_pos = {}
    while(search_str):
        inds = find_all_substr(text, search_str)
        if inds:
            searched_pos["matched_words"] = [f"...{text[ind: ind + len(search_str) + 35]}..." for ind in inds]
            searched_pos["pos"] = inds
            searched_pos["%_match"] = f"{len(search_str)/len(string_to_search) * 100}%"
            searched_pos["count"] = len(inds)
            break
        search_str = search_str[:-1]
    return searched_pos
         
          
def count_sents(text):
    '''this function counts the number of sentences in the given text
    text: The text/paragraph/string'''
    if text[-1] == ".":
        return len(text.split(".")) - 1
    else:
        return len(text.split("."))

def count_words(text):
    '''this function counts the number of words in the given text
    text: The text/paragraph/string'''
    return len(text.split())
          
def count_lines(text):
    '''this function counts the number of lines in the given text
    text: The text/paragraph/string'''
    return text.count("\n") + 1
          
def count_tabs(text):
    '''this function counts the number of tabs in the given text
    text: The text/paragraph/string'''
    return text.count("\t")
          
        

    