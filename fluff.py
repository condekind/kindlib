from IPython.display import display_html

def p(*args):
  s = ''  # html string
  for df in args:
    s += df.head().to_html()
  display_html(s.replace('table','table style="display:inline"'), raw=True)
  return args
