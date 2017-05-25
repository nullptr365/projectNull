import page_crawlerV1_1

test_filename = "pydoc.txt"
test_site = "https://www.kali.org"


testSiteObj = page_crawlerV1_1.Crawler()

try:
    testSiteObj.crawl(test_site)
    #testSiteObj.create_file(test_filename)
    #testSiteObj.write_to_file()
    testSiteObj.display_log()
    #testSiteObj.delete_file(testSiteObj.filename)
except FileNotFoundError:
    pass
