
a = 0.1
b = 0.2
print(f"{a} + {b} = ", a + b)
'''
0.1 + 0.2 =  0.30000000000000004
'''

from decimal import Decimal
a = Decimal('0.1')
b = Decimal('0.2')
print(f"{a} + {b} = ", a + b)
'''
0.1 + 0.2 =  0.3
'''