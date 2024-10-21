def main() -> int:
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
    no_of_word= no_of_words(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{no_of_word} words found in the document")
    counted = count_characters(file_contents)
    sort_dict(counted)

    return 0

def no_of_words(text) -> int:
    no_ws = text.split()
    return len(no_ws)

def count_characters(text):
    dictio= {}
    lowered_string = text.lower()
    lowered_str = "".join(lowered_string.split())
    for x in lowered_str:
        if x in dictio:
            dictio[x] +=1
        else:
            dictio[x] = 1
    dict_list(dictio)
    return dictio

def sort_on(xd):
    return xd["num"]
        
def sort_dict(dictio):
    listed = dict_list(dictio)
    listed.sort(reverse=True, key=sort_on)
    for i in listed:
        if  i["char"].isalpha():
            print(f"The {i["char"]} character is found {i["num"]} times")

    
def dict_list(dictio):
    list_char = []
    for i in dictio:
        t_dict={"char": i, "num": dictio[i]}
        list_char.append(t_dict)
    return(list_char)



    
main()