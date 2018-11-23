from main import find_max_suff_len
from main import get_expression

def test_simple():
  assert find_max_suff_len("ab.c+ b") == 1

def test_simple_concat():
  assert find_max_suff_len("aa. a") == 2
  assert find_max_suff_len("ab. a") == 0
  assert find_max_suff_len("ba. a") == 1

def test_simple_disjunction():
  assert find_max_suff_len("aa+ a") == 1
  assert find_max_suff_len("ab+ a") == 1
  assert find_max_suff_len("ba+ a") == 1

def test_simple_star():
  assert find_max_suff_len("a* b") == 0
  assert find_max_suff_len("b* b") == 'INF'
  assert find_max_suff_len("ab.* b") == 1

def test_diff_choices():
  assert find_max_suff_len("ab.c+bca..+cbb..+ b") == 2

def test_infinity():
  assert find_max_suff_len("ba.a+* a") == 'INF'
  assert find_max_suff_len("ab.b+* b") == 'INF'
  assert find_max_suff_len("aba.+* a") == 'INF'

def test_type():
  assert find_max_suff_len(list('abc')) == 'ExpressionError'
  assert find_max_suff_len({'a' : 1}) == 'ExpressionError'
  assert find_max_suff_len(Exception('ab.b+* b')) == 'ExpressionError'

def test_wrong_format_symbols():
  assert find_max_suff_len("aba..c+bd.+ b") == 'ExpressionError'

def test_wrong_polish_notate():
  assert find_max_suff_len("ab.cb+ b") == 'ExpressionError'
  assert find_max_suff_len("ab.cb+++ b") == 'ExpressionError'

def test_concatenation():
  assert find_max_suff_len("ab.ab.bb.+. b") == 3

def test_number_after_inf():
  assert find_max_suff_len("c*ac.. c") == 1

def test_star_decrease():
  assert find_max_suff_len("bbbb...a*. b") == 4
  assert find_max_suff_len("bb.a*.bb.. b") == 4

def test_many_stars():
  assert find_max_suff_len("ac*.* a") == 'INF'
  assert find_max_suff_len("ac*.* c") == 'INF'
  assert find_max_suff_len("ac*.*b+* c") == 'INF'

def test_many_concatenations():
  assert find_max_suff_len("bb.bb.bb.bb.bb..... b") == 10

def test_Pavel_Akhtyamov_hw_example1():
  assert find_max_suff_len("ab+c.aba.*.bac.+.+* b") == 1

def test_Pavel_Akhtyamov_hw_example2():
  assert find_max_suff_len("acb..bab.c.*.ab.ba.+.+*a. b") == 0
