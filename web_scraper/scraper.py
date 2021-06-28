import requests
from bs4 import BeautifulSoup


URL='https://en.wikipedia.org/wiki/History_of_Mexico'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')


def get_citations_needed_count(URL):
    results = soup.find_all('span',text='citation needed')
    print('The number of citation needed is : ' , len(results))
    print('\n')
    print('-'*90)
    return len(results)



def get_citations_needed_report(URL):

    results = soup.find_all('span',text='citation needed')
    
    final_result = []
    citation = 1
    for text in results:
        if text not in final_result: 
            final_result.append(text)
            
    for element in final_result:
        parent = element.find_parent('p')
        
        print(parent.text.strip())
        citation = citation + 1
        print('-'*90)

if __name__ == "__main__":
    get_citations_needed_count(URL)
    get_citations_needed_report(URL)