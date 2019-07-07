import click
import click_config_file
import logging
import yaml
from .harvester import Harvester

YAML_CONFIG_FILE_PATH="/tmp/netl-config.yaml"

def yaml_provider(file_path, cmd_name):
    with open(file_path) as config_data:
        return yaml.safe_load(config_data)[cmd_name]

@click.group()
def run():
    logging.basicConfig(level=logging.INFO)
    pass

@run.command()
@click_config_file.configuration_option(
    config_file_name=YAML_CONFIG_FILE_PATH,
    provider=yaml_provider
)
def classify():
    """Classify the cleansed data."""
    pass

@run.command()
@click_config_file.configuration_option(
    config_file_name=YAML_CONFIG_FILE_PATH,
    provider=yaml_provider
)
def cleanse():
    """Cleanse data extracted from news sources."""
    pass

@run.command()
@click_config_file.configuration_option(
    config_file_name=YAML_CONFIG_FILE_PATH,
    provider=yaml_provider
)
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
    """
    Harvest the data given domains, sources, and additional flags
    to control the behavior of the harvestor.  If --config option
    is specified the settings from the file will be used as opposed
    to the defaults.
    """
    logging.info(f"[{domains}] [{sources}] [{send_to_console}] [{save_to_db}]")
    harvester = Harvester(send_to_console, save_to_db)
    harvester.populate_sources()
    harvester.harvest(domains, sources, send_to_console, save_to_db)

if __name__ == '__main__':
    run()

