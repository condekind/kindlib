import pandas as pd
from IPython.display import display_html

def p(*args):
  s = ''  # html string
  for df in args:
    s += df.head().to_html()
  display_html(s.replace('table','table style="display:inline"'), raw=True)
  return args

def Colstats(df: pd.DataFrame):
  return pd.DataFrame(data=[(
    c,
    df[c].dtype,
    df[c].nunique(),
    df[c].isna().sum(),
    len(df[df[c].duplicated() == True]))
    for c in df.columns], columns=[
    'col', 'type', 'nunique', 'nan', 'duplicated_values'])