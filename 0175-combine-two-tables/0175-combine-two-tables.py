import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return person.merge(
        address[['personId', 'city', 'state']],
        on='personId',
        how='left',
        copy=False
    )[['firstName', 'lastName', 'city', 'state']]