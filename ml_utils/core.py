# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_core.ipynb (unless otherwise specified).

__all__ = ['assert_eq', 'pivot_vs', 'display']

# Cell
def assert_eq(a, b):
    assert a==b, f"{a} != {b}"

# Cell
import pandas as pd

def pivot_vs(df, col, n=20, min_cnt=10):
    """pivot the counts a column horizontally to make it more readable

    https://twitter.com/TedPetrou/status/1287769454567456768
    """
    vc = df[col].value_counts()
    vc = vc[vc >= min_cnt]
    vcs = []
    for i in range(0, len(vc), n):
        cur_df = vc.iloc[i:i + n].reset_index()
        cur_df.columns = ['value', 'count']
        cur_df['rank'] = range(i + 1, i + len(cur_df) + 1)
        vcs.append(cur_df)
    return pd.concat(vcs, axis=1)

# Cell

class display(object):
    """Display HTML representation of multiple objects"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""

    def __init__(self, *args):
        self.args = args

    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                     for a in self.args)

    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                       for a in self.args)