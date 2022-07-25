import pyam
from nomenclature import DataStructureDefinition
from pathlib import Path

here = Path(__file__).absolute().parent


def main(df: pyam.IamDataFrame) -> pyam.IamDataFrame:
    """Project/instance-specific workflow for scenario processing"""

    # Cast to an IamDataFrame if necessary
    if not isinstance(df, pyam.IamDataFrame):
        df = pyam.IamDataFrame(df)

    # Import the codelists for the project
    definition = DataStructureDefinition(here / "definitions")

    # Validate `df` against the codelists
    # This method raises an error if any items are not defined in the codelists.
    definition.validate(df)

    return df
