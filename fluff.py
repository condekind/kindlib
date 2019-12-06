import pandas as pd
import re
import unidecode
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


def clean(args, wsep=' ', asep=''):
  if hasattr(args, '__iter__'):
    if hasattr(args[0], '__iter__') and len(args[0]) > 1:
      ty = type(args)
      return ty([
        unidecode.unidecode(
          re.sub(r'\ +', wsep,
            re.sub(r'[^\w\s]|[W_]', asep,
              s, re.UNICODE ) ) )
        .lower()
        .strip()
        for s in args])
    else:
      return (
        unidecode.unidecode(
          re.sub(r'\ +', wsep,
            re.sub(r'[^\w\s]|[W_]', asep,
              args, re.UNICODE ) ) )
        .lower()
        .strip()
      )
  else:
    return args