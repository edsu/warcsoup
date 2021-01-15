#!/usr/bin/env python3

from bs4 import BeautifulSoup
from warcio.archiveiterator import ArchiveIterator

for record in ArchiveIterator(open('data.warc.gz', 'rb')):
    if record.rec_type == 'response':
        content_type = record.http_headers.get_header('Content-Type') 
        if 'html' in content_type:
            html = record.content_stream().read()
            soup = BeautifulSoup(html, 'html.parser')

            # do fun stuff with the html like print out the title of the page
            print(soup.select('head title')[0].text.strip())










