import confuse
import argparse
from .harvester import Harvester

def run():
    config = confuse.Configuration('netlbot', __name__)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--domains',
        help='A comma-separated string of domains '
            '(eg wsj.com, nytimes.com, bbc.co.uk) '
            'to restrict the search to.'
    )
    parser.add_argument(
        '--sources',
        help='A comma-separated string of identifiers '
            'of the news sources (eg the-wall-street-journal, '
            'the-new-york-times, bbc-news) or blogs you want '
            'headlines from.'
    )
    parser.add_argument(
        '--send-to-console',
        help='Send the output to console (disabled-0, enabled-1)'
    )
    parser.add_argument(
        '--save-to-db',
        help='Save the output to database (disabled-0, enabled-1)'
    )
    args = parser.parse_args()
    config.set_args(args)

    domains = config["domains"].get()
    sources = config["sources"].get()
    send_to_console = config["send-to-console"].get()
    save_to_db = config["save-to-db"].get()
    harvester = Harvester()
    harvester.populate_sources()
    harvester.harvest(domains, sources, send_to_console, save_to_db)

if __name__ == '__main__':
    run()

