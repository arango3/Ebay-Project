import requests
from bs4 import BeautifulSoup as bs


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Referer': 'https://www.ebay.com/',
    'Upgrade-Insecure-Requests': '1'
}

class Scraper:
    @staticmethod
    def get_page(url, destination):
        r = requests.get(url, headers=headers)
        soup = bs(r.content, 'html.parser')
        file = open(destination, 'w')
        file.write(str(soup.prettify()))
        file.close()

    @staticmethod
    def extract(file, anchor_tag, nest_tag):
        file_path = file
        open_file = open(file_path, 'r')
        file_contents = open_file.read()
        soup = bs(file_contents, features='html.parser')
        open_file.close()

        categories = soup.find_all(class_=anchor_tag)
        nest_tags = []  # List to store the nest_tag values

        for tag in categories:
            link = tag[nest_tag]
            nest_tags.append(link)  # Append each nest_tag value to the list

        return nest_tags  # Return the list of nest_tag values
       # return categories


if __name__ == '__main__':
    url = 'https://www.ebay.com/b/Computer-Parts-Components/175673/bn_1643095'
    categories = 'categories.html'
    filters = 'filters.html'
    anchor_class = 'b-textlink b-textlink--sibling'
    tag = 'href'
    filter_anchor = 'brm__aspect-list'
    filter_tag = 'span'
#    Scraper.get_page(url, categories)
    extracted_categories = Scraper.extract(categories, anchor_class, tag)
    Scraper.get_page(extracted_categories[3], filters)
    # Print URLs with line break separator
    urls_with_separator = '\n'.join(extracted_categories)
    print(urls_with_separator)
    extract_filters = Scraper.extract(filters, filter_anchor, filter_tag)
    print(extract_filters)
#    for link in extracted_tags:
#        Scraper.get_page(extracted_tags, extracted_tags)
