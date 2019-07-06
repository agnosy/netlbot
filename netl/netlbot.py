import click
from .harvester import Harvester

@click.group()
def run():
    pass

@run.command()
def classify():
    """Classify the cleansed data."""
    pass

@run.command()
def cleanse():
    """Cleanse data extracted from news sources."""
    pass

@run.command()
@click.option(
    '--domains',
    envvar='NETL_HARVEST_DOMAINS',
    default='wsj.com',
    help='A comma-separated string of domains '
        '(eg wsj.com, nytimes.com, bbc.co.uk) '
        'to restrict the search to.'
)
@click.option(
    '--sources',
    envvar='NETL_HARVEST_SOURCES',
    default='the-wall-street-journal',
    help='A comma-separated string of identifiers '
        'of the news sources (eg the-wall-street-journal, '
        'the-new-york-times, bbc-news) or blogs you want '
        'headlines from.'
)
@click.option(
    '--send-to-console',
    envvar='NETL_HARVEST_SEND_TO_CONSOLE',
    default=1,
    help='Send the output to console. (disabled-0, enabled-1, default: 1)'
)
@click.option(
    '--save-to-db',
    envvar='NETL_HARVEST_SAVE_TO_DB',
    default=1,
    help='Save the output to database. (disabled-0, enabled-1, default: 1)'
)
def harvest(domains, sources, send_to_console, save_to_db):
    """Harvest the data with default options."""
    harvester = Harvester()
    harvester.harvest(domains, sources, send_to_console, save_to_db)

if __name__ == '__main__':
    run()

