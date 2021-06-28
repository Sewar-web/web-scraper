from web_scraper.scraper import get_citations_needed_report, get_citations_needed_count


from web_scraper import __version__
def test_version():
    assert __version__ == '0.1.0'




def test_get_number_of_citation_needed():
    expected = get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico")
    assert expected == 5

def test_get_report_of_citation_needed():
    get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico")
    assert "The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.[citation needed][7] Such conditions encouraged the initial pursuit of a hunter-gatherer existence.\n" 

def test_get_citations_needed_report():
    get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico")
    assert  "During the three centuries of colonial rule, fewer than 700,000 Spaniards, most of them men, settled in Mexico.[citation needed] Europeans, Africans, and indigenous intermixed, creating a mixed-race casta population in a process known as mestizaje. Mestizos, people of mixed European-indigenous ancestry, constitute the majority of Mexico's population."
     

