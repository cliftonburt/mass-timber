import click
from pipelines.simulate_moisture import simulate_moisture
from pipelines.summarize_ops import summarize_moisture

@click.group()
def cli():
    pass

@cli.command()
@click.option('--count', default=10, help='Number of records to generate.')
def simulate_moisture_data(count):
    simulate_moisture(count)

@cli.command()
def summarize():
    summarize_moisture()

if __name__ == "__main__":
    cli()


@cli.command()
@click.option('--count', default=10, help='Number of production records to generate.')
def simulate_production_data(count):
    from pipelines.simulate_production import simulate_production
    simulate_production(count)

@cli.command()
def summarize_production_data():
    from pipelines.summarize_ops import summarize_production
    summarize_production()
