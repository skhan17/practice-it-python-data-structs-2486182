import string
from collections import Counter


def count_words(paragraph):
    paragraph = paragraph.lower()
    paragraph = paragraph.translate(str.maketrans('', '', string.punctuation))
    wordList = paragraph.split()
    counter = Counter(wordList)
    return counter


def main():
    paragraph = """Nadia’s Garden Restaurant is the creation of husband and wife team Nadia and Timothy Arbore. 
    Their American-infused, Italian-based, organically created, cuisine was inspired by Nadia’s papa, an immigrant from Italy, 
    who shared his love of cooking with Nadia as a young girl. His focus on using fresh ingredients and family style dining were 
    the inspiration for Nadia’s Garden Restaurant. Located in the heart of Main Streets Historic District, they are proud to be a 
    part of a rich community. In 2011, the duo remodeled the restaurant and updated their menu to include newer and more diverse entrées
     that could be made from local organic suppliers. Preservation of the building’s original layout has allowed them to create smaller, 
     more intimate, dining spaces. Nadia and Timothy are committed to sharing their family history of cuisine, along with their new inspirations,
      with their customers. Their passion for community, entertainment, and hospitality are found in every aspect of Nadia’s Garden Restaurant."""
    print(count_words(paragraph))


if __name__ == "__main__":
    main()

# print following:
# Counter({'of': 7, 'and': 7, 'the': 6, 'their': 6, 'nadia’s': 4, 'restaurant': 4, 'to': 4, 'garden': 3, 'nadia': 3, 'with': 3, 'a': 3, 'in': 3, 'are': 3, 'timothy': 2, 'cuisine': 2, 'from': 2, 'his': 2, 'family': 2, 'dining': 2, 'for': 2, 'be': 2, 'community': 2, 'more': 2, 'is': 1, 'creation': 1, 'husband': 1, 'wife': 1, 'team': 1, 'arbore': 1, 'americaninfused': 1, 'italianbased': 1, 'organically': 1, 'created': 1, 'was': 1, 'inspired': 1, 'by': 1, 'papa': 1, 'an': 1, 'immigrant': 1, 'italy': 1, 'who': 1, 'shared': 1, 'love': 1, 'cooking': 1, 'as': 1, 'young': 1, 'girl': 1, 'focus': 1, 'on': 1, 'using': 1, 'fresh': 1, 'ingredients': 1, 'style': 1, 'were': 1,
#         'inspiration': 1, 'located': 1, 'heart': 1, 'main': 1, 'streets': 1, 'historic': 1, 'district': 1, 'they': 1, 'proud': 1, 'part': 1, 'rich': 1, '2011': 1, 'duo': 1, 'remodeled': 1, 'updated': 1, 'menu': 1, 'include': 1, 'newer': 1, 'diverse': 1, 'entrées': 1, 'that': 1, 'could': 1, 'made': 1, 'local': 1, 'organic': 1, 'suppliers': 1, 'preservation': 1, 'building’s': 1, 'original': 1, 'layout': 1, 'has': 1, 'allowed': 1, 'them': 1, 'create': 1, 'smaller': 1, 'intimate': 1, 'spaces': 1, 'committed': 1, 'sharing': 1, 'history': 1, 'along': 1, 'new': 1, 'inspirations': 1, 'customers': 1, 'passion': 1, 'entertainment': 1, 'hospitality': 1, 'found': 1, 'every': 1, 'aspect': 1})
