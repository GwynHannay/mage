import json
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_file(*args, **kwargs):
    """
    Template for loading data from any source.
    """
    pipeline_name = kwargs.get('pipeline_uuid')
    filepath = "/home/nfs/gphotos/, Peter/DSC_1015-COLLAGE.jpg.json"

    with open(filepath, 'r') as f:
        this_file = f.read()

    contents = json.loads(this_file)

    return contents


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
