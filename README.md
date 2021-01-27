# text_utility Module 
<p>text_utility module can be used to perform basic and intermediate operations on strings/text in python. Following are some major functions of text_utitilty module.</p>
<ol>
    <li><a href="#find_best_match">find_best_match(text, string_to_search)</a></li>
    <li><a href="#bag_of_words">bag_of_words(text)</a></li>
    <li><a href="#remove_refs">remove_refs(text)</a></li>
    <li><a href="#find_all_substr">find_all_substr(text, substring)</a></li>
    <li><a href="#remove_punct">remove_punct(text)</a></li>
    <li><a href="#remove_white_spaces">remove_white_spaces(text)</a></li>
    <li><a href="#count_words">count_words(text)</a></li>
    <li><a href="#count_sent">count_sent(text)</a></li>
    <li><a href="#count_lines">count_lines(text)</a></li>
    <li><a href="#count_tabs">count_tabs(text)</a></li>
<ol>

<a id="find_best_match"></a>

## Find Best Match
<p>this function finds the best match of the searched string/phrase. It can be used for providing suggestions while searching or it can be used as search algoritm for a given text</p>
<p><b>arguments:</b> this function takes two required positional arguments</p>
<div>text(str): The text/paragraph/string to be searched upon</div>
<div>string_to_search(str): The string to be searched</div><br>

<p><b>Returns(dict):</b> a dictionary containg all the words, their positions, how much they match with the searched string and count of how many matching words/phrases are there</p><br>

<a id="bag_of_words"></a>

## Bag Of Words
<p>this function creates a dictionary of all the words in the given text with the count of no of times they occur in text</p>
<p><b>arguments:</b> this function takes one required positional arguments</p>
<div>text(str): The text/paragraph/string </div><br>

<p><b>Returns(dict):</b> a dictionary containg all the words as key and the no of times they appear as key</p><br>

<a id="remove_refs"></a>

## Remove References
<p>this function removes all the references inside the given text</p>
<p><b>arguments:</b> this function takes one required positional arguments</p>
<div>text(str): The text/paragraph/string</div><br>

<p><b>Returns(str):</b> a text with all refernces being filtered out</p><br>

<a id="find_all_substr"></a>

## Find All Substring
<p>this function finds the position of the all the occurences of the given substring</p>
<p><b>arguments:</b> this function takes two required positional arguments</p>
<div>text(str): The text/paragraph/string to be searched upon</div>
<div>substring(str): The substring to be found</div><br>

<p><b>Returns(list):</b> a list containing all the positions of occurences of the givent substring</p><br>

<a id="remove_punct"></a>

## Remove Punctuation
<p>this function removes all the punctuation inside the given text</p>
<p><b>arguments:</b> this function takes one required positional arguments</p>
<div>text(str): The text/paragraph/string</div><br>

<p><b>Returns(str):</b> a text with all punctutation being filtered out</p><br>

<a id="remove_white_spaces"></a>

## Remove White Spaces
<p>this function removes all the whitespaces(more than one whitespace) from start, between and end of the given text</p>
<p><b>arguments:</b> this function takes one required positional arguments</p>
<div>text(str): The text/paragraph/string</div><br>

<p><b>Returns(str):</b> a text with all white spaces(more than one whitespace) being filtered out</p><br>

<a id="count_words"></a>

## Count Words
<p>this function counts the number of words in the given text</p>
<p><b>arguments:</b> this function takes one required positional arguments</p>
<div>text(str): The text/paragraph/string</div><br>

<p><b>Returns(str):</b> Number of words</p>

<a id="count_sent"></a>

## Count Sentences
<p>this function counts the number of sentences in the given text</p>
<p><b>arguments:</b> this function takes one required positional arguments</p>
<div>text(str): The text/paragraph/string</div><br>

<p><b>Returns(int):</b> Number of sentences</p>

<a id="count_lines"></a>

## Count Lines
<p>this function counts the number of lines in the given text</p>
<p><b>arguments:</b> this function takes one required positional arguments</p>
<div>text(str): The text/paragraph/string</div><br>

<p><b>Returns(int):</b> Number of lines</p>

<a id="count_tabs"></a>

## Count Tabs
<p>this function counts the number of tabs in the given text</p>
<p><b>arguments:</b> this function takes one required positional arguments</p>
<div>text(str): The text/paragraph/string</div><br>

<p><b>Returns(int):</b> Number of tabs</p>
