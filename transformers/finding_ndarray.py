from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.constants import ActionType, Axis
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action
from pandas import DataFrame
import numpy as np

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def execute_transformer_action(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Execute Transformer Action: ActionType.FIX_SYNTAX_ERRORS

    This marks any improperly formatted values in each column specified
    as invalid.

    Docs: https://docs.mage.ai/guides/transformer-blocks#fix-syntax-errors
    """
    # column_types = kwargs.get('column_types', {})
    # df_columns = df.columns.tolist()
    # ctypes = {k: v for k, v in column_types.items() if k in df_columns}
    # new_cols = [col for col in df_columns if col not in column_types] # column_name
    # kwarg_list = [kwargs] * len(new_cols) #kwargs
    
    # df_sample = df
    # columns = [df_sample[col] for col in new_cols] #series
    # dd = df_sample.dtypes[new_cols] #dtype

    # i = 0
    # cnt = len(columns)
    # zippy = list()
    # while True:
    #     zippy.append(
    #         {
    #             'dtype': dd[i],
    #             'series': columns[i],
    #             'column_name': new_cols[i],
    #             'kwargs': kwarg_list[i]
    #         }
    #         )
    #     i = i + 1
    #     if i == cnt:
    #         break

    # for thing in zippy:
    #     print(thing['column_name'])
    #     if thing['dtype'] == 'object':
    #         clean_series = thing['series'].apply(lambda x: x.strip(' \'\"') if type(x) is str else x)
    #         clean_series = clean_series.map(lambda x: x if (not isinstance(x, str) or x != '') else np.nan)
    #         clean_series = clean_series.dropna()

    #         exact_dtype = type(clean_series.iloc[0]) if clean_series.count() else None
    #         print(exact_dtype)

    # return df
    action = build_transformer_action(
        df,
        action_type=ActionType.FIX_SYNTAX_ERRORS,
        arguments=df.columns,  # Specify columns to fix syntax errors for.
        axis=Axis.COLUMN,
    )

    return BaseAction(action).execute(df)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'