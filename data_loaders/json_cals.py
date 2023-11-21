import json
import os
from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_file(*args, **kwargs):
    """
    Template for loading data from filesystem.
    Load data from 1 file or multiple file directories.

    For multiple directories, use the following:
        FileIO().load(file_directories=['dir_1', 'dir_2'])

    Docs: https://docs.mage.ai/design/data-loading#fileio
    """
    filepath = kwargs['file_source']

    cal_items = list()
    for filename in os.listdir(filepath):
        if not filename.endswith('.json'):
            continue
        if filename.startswith('._'):
            continue

        contents = None
        fullpath = os.path.join(filepath, filename)
        with open(fullpath, 'r') as f:
            contents = f.read()
    
        cal_items.append(json.loads(contents))#.get('items', []

    return cal_items

    # return FileIO().load(filepath, format='json', orient='records')


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'