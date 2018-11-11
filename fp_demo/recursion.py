#!/usr/bin/env python3

def rec(x):
  result = '- Result in the beginning -'
  if(x < 0):
    result = 0
  else:
    print('Before(x): ', x)
    print('Before(result): ', result)
    result = x + rec(x - 1)
    print('After(x): ', x)
    print('After(result): ', result)
  return result

print('\n\nRecursion Example Results')
rec(6)
