#!/usr/bin/env python3

import wikipedia
import argparse

from urllib.parse import urlparse

def main():

    parser = argparse.ArgumentParser(
            description='takes a dbpedia uri and try to return the'\
                    ' wikipedia links for that page in different languages.')

    parser.add_argument(
            'uri',
            help='the uri from which we will try to guess the wiki links'
            )

    parser.add_argument(
            '-t',
            '--test',
            help='run the doctest suite and exit',
            action='store_true'
            )

    args = parser.parse_args()


    if args.test:
        import doctest
        doctest.testmod()
        exit(0)


    links = urltranslate(args.uri)
    print("\n".join(links))
    return

def urltranslate(url):

    title = title_url(url)
    links = wikipedia.langlinks(title)
    return links

def title_url(url):
    """ extract a page title from the given url

    EXAMPLE
    =======

    >>> title_url('http://dbpedia.org/resource/Montreal')
    'Montreal'
    """

    parsed = urlparse(url)

    title = parsed.path.split('/')[-1]
    return title

if __name__ == '__main__':
    main()
