# All right reserved(lol) by Dmitry Sadykov (gr. 798)
# Practice #1 (var. 19)

def find_max_suff_len(string):
  try:
    expr, wildcard = get_expression(string)
  except (ValueError, TypeError):
    return 'ExpressionError'

  # subwords stacks for:
  all_wc = [] # all symbols in subword are wildcard
  wc_len = [] # length of wildcards suffix (may be a number when infinite)
  inf_wc = [] # if infinite wildcard suffix in subword

  for symb in expr:
    # for disjunction
    if symb == '+':
      if len(wc_len) < 2:
        return 'ExpressionError'
      if wc_len[-2] < wc_len[-1]:
        wc_len[-2] = wc_len[-1]
      all_wc[-2] = all_wc[-2] or all_wc[-1]
      all_wc.pop()
      wc_len.pop()
      inf_wc.pop()

    # for concatenation
    elif symb == '.':
      if len(wc_len) < 2:
        return 'ExpressionError'
      if all_wc[-1]:
        wc_len[-2] += wc_len[-1]
      else:
        wc_len[-2] = wc_len[-1]
      inf_wc[-2] = inf_wc[-1]
      all_wc[-2] = all_wc[-2] and all_wc[-1]
      all_wc.pop()
      wc_len.pop()
      inf_wc.pop()

    # for Kleene's star
    elif symb == '*':
      if len(wc_len) < 1:
        return 'ExpressionError'
      if all_wc[-1]:
        inf_wc[-1] = True
      elif len(wc_len) > 1 and wc_len[-2] > wc_len[-1]:
        all_wc[-1] = True
        wc_len[-1] = 0

    # for symbols
    else:
      inf_wc.append(False)
      if (symb == wildcard):
        all_wc.append(True)
        wc_len.append(1)
      else:
        all_wc.append(False)
        wc_len.append(0)

  if len(all_wc) != 1:
    return 'ExpressionError'
  if inf_wc[0] == True:
    return 'INF'
  return wc_len[0]


def get_expression(string):
  # expr = re.findall(r"[+.*abc]+", string)
  if not type(string) is str:
    raise TypeError

  expr = ['']
  allowed_symbols = {'+', '.', '*', 'a', 'b', 'c', ' '}
  for sy in string:
    if not sy in allowed_symbols:
      raise ValueError
    elif sy == ' ':
      expr.append('')
    else:
      expr[-1] += sy

  if len(expr) != 2 or len(expr[1]) != 1:
    raise ValueError
  return expr

def main():
  print (find_max_suff_len(input()))

if __name__ == "__main__":
  main()
