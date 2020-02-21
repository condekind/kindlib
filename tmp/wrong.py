#clean

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