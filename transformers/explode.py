import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    for field in kwargs['list_fields']:
        exploded = data.explode(field, ignore_index=True)
        normed = pd.json_normalize(exploded[field])
        normed = normed.add_prefix(''.join([field, '_']))
        exploded.drop(field, axis=1, inplace=True)

        suffix = ''.join(['_', field])

        data = exploded.join(normed, how='inner', rsuffix=suffix, validate='1:1')

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'