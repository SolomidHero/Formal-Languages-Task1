# All right reserved(lol) by Dmitry Sadykov (gr. 798)
# Practice #1 (var. 19)

from dataclasses import dataclass

@dataclass
class Word:
  is_wildcarded: bool   # all symbols in subword are wildcard
  wildcard_length: int  # length of wildcards suffix (may be a number when infinite)
  is_infinite: bool     # if infinite wildcard suffix in subword

def find_max_suff_len(string):
  try:
    expr, wildcard = get_expression(string)
  except (ValueError, TypeError):
    return 'ExpressionError'

  # subwords stack of class words:
  subword = list()

  for symb in expr:
    # for disjunction
    if symb == '+':
      if len(subword) < 2:
        return 'ExpressionError'
      if subword[-2].wildcard_length < subword[-1].wildcard_length:
        subword[-2].wildcard_length = subword[-1].wildcard_length
      subword[-2].is_wildcarded = subword[-2].is_wildcarded or subword[-1].is_wildcarded
      subword.pop()

    # for concatenation
    elif symb == '.':
      if len(subword) < 2:
        return 'ExpressionError'
      if subword[-1].is_wildcarded:
        subword[-2].wildcard_length += subword[-1].wildcard_length
      else:
        subword[-2].wildcard_length = subword[-1].wildcard_length
      subword[-2].is_infinite = subword[-1].is_infinite
      subword[-2].is_wildcarded = subword[-2].is_wildcarded and subword[-1].is_wildcarded
      subword.pop()

    # for Kleene's star
    elif symb == '*':
      if len(subword) < 1:
        return 'ExpressionError'
      if subword[-1].is_wildcarded:
        subword[-1].is_infinite = True
      elif len(subword) > 1 and subword[-2].wildcard_length > subword[-1].wildcard_length:
        subword[-1].is_wildcarded = True
        subword[-1].wildcard_length = 0

    # for symbols
    else:
      if (symb == wildcard):
        subword.append(Word(True, 1, False))
      else:
        subword.append(Word(False, 0, False))

  if len(subword) != 1:
    return 'ExpressionError'
  if subword[0].is_infinite == True:
    return 'INF'
  return subword[0].wildcard_length


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
