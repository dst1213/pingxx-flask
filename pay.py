#!/usr/bin/env python
import pingpp
import random
import string

pingpp.api_key = 'sk_test_1yDWr9WTiDeHPqXn1SDeb5iH'

orderno = ''.join(random.sample(string.ascii_letters + string.digits, 8))
ch = pingpp.Charge.create(
    order_no=orderno,
    channel='alipay',
    amount=1,
    subject='Your Subject',
    body='Your Body',
    currency='cny',
    app=dict(id='app_mjnfnLSijz54rzHe'),
    client_ip='127.0.0.1'
)
print ch
