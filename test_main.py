from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 20
	assert simple_work_calc(20, 3, 2) == 70
	assert simple_work_calc(30, 4, 2) == 240

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
  assert work_calc(30, 3, 2, lambda n: 2 * n) == 300
  assert work_calc(30, 3, 2, lambda n: n * log(n)) == 300



def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
  assert compare_work(simple_work_calc, work_calc) == [(10, 15, 300), (20, 530, 300), (30, 300, 300)]
  assert compare_work(simple_work_calc, work_calc) == [(5, 15, 300), (15, 530, 300), (25, 265, 325)]
	# create work_fn1
	# create work_fn2

    res = compare_work(work_fn1, work_fn2)
	print(res)

	
def test_compare_span():
  assert compare_span(10, 4, 5)
  assert compare_span(20, 4, 5)
  assert compare_span(30, 4, 5)
  assert compare_span(40, 4, 5)
	# TODO
