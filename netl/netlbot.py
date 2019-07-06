import click

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
    envvar='NETL_DOMAINS',
    default='wsj.com',
    help='A comma-separated string of domains (eg wsj.com, nytimes.com, bbc.co.uk) to restrict the search to.'
)
@click.option(
    '--sources',
    envvar='NETL_SOURCES',
    default='the-wall-street-journal',
    help='A comma-separated string of identifiers of the news sources (eg the-wall-street-journal, the-new-york-times, bbc-news) or blogs you want headlines from.'
)
@click.option(
    '--send-to-console',
    envvar='NETL_SEND_TO_CONSOLE',
    default=1,
    help='Send the output to console. (default: 1 enabled, 0 to disable)'
)
@click.option(
    '--save-to-db',
    envvar='NETL_SAVE_TO_DB',
    default=0,
    help='Save the output to database. (default: 0 disabled, 1 to enable)'
)
def harvest(domains, sources):
    """Harvest the data with default options."""
    h1 = harvester.Harvester()
    h1.harvest(domains, sources)

if __name__ == '__main__':
    run()

