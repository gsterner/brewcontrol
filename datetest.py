import time
from rich.progress import Progress
from datetime import datetime
boil_time = 60
taste_hops = 15
aroma_hops = 0

boil_time_seconds = boil_time * 60
taste_time_seconds = (boil_time - taste_hops) * 60
aroma_time_seconds = (boil_time - aroma_hops) * 60


with Progress() as progress:
    task1 = progress.add_task("[red]Boil time", total=boil_time_seconds)
    task2 = progress.add_task("[green]Taste", total=taste_time_seconds)
    task3 = progress.add_task("[green]Aroma", total=aroma_time_seconds)
    task4 = progress.add_task("[red]Time", total=0)

    while not progress.finished:
        progress.update(task1, advance=1)
        progress.update(task2, advance=1)
        progress.update(task3, advance=1)
        progress.update(task4, advance=1, description="[purple]"+datetime.now().strftime('%H:%M:%S'))
        time.sleep(1)
