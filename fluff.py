import pandas as pd
import re
import unidecode
from IPython.display import display_html

def p(*args):
  w = 150  # pd.get_option('display.max_colwidth')
  s = ''  # html string
  for df in args:
    s += df.head().to_html()
  display_html(s.replace('table','table style="display:inline"')
                .replace('td','td style="max-width: {}px;overflow-x:hidden"'
                .format(w)), raw=True)
  return args

def Colstats(df: pd.DataFrame):
  return pd.DataFrame(data=[(
      c,
      df[c].dtype,
      df[c].nunique(),
      df[c].isna().sum(),
      len(df[df[c].duplicated() == True]))
      for c in df.columns
    ],
    columns=['col', 'type', 'nunique', 'nan', 'duplicated_values'])