# coding=utf-8
import unittest
import iyzipay


class BasicPaymentPreAuthSample(unittest.TestCase):
    def runTest(self):
        self.should_pay_with_card()
        self.should_pay_with_card_token()

    def should_pay_with_card(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['price'] = '1'
        request['paidPrice'] = '1'
        request['installment'] = '1'
        request['currency'] = 'TRY'
        request['buyerEmail'] = 'email@email.com'
        request['buyerId'] = 'B2323'
        request['buyerIp'] = '85.34.78.112'
        request['connectorName'] = 'connector name'

        payment_card = dict([('cardHolderName', 'John Doe')])
        payment_card['cardNumber'] = '5528790000000008'
        payment_card['expireMonth'] = '12'
        payment_card['expireYear'] = '2030'
        payment_card['cvc'] = '123'
        payment_card['registerCard'] = '0'
        request['paymentCard'] = payment_card

        # make request
        basic_payment_pre_auth = iyzipay.BasicPaymentPreAuth()
        basic_payment_pre_auth_response = basic_payment_pre_auth.create(request, options)

        # get and print response
        print(basic_payment_pre_auth_response.read().decode('utf-8'))

    def should_pay_with_card_token(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['price'] = '1'
        request['paidPrice'] = '1'
        request['installment'] = '1'
        request['currency'] = 'TRY'
        request['buyerEmail'] = 'email@email.com'
        request['buyerId'] = 'B2323'
        request['buyerIp'] = '85.34.78.112'
        request['connectorName'] = 'connector name'

        payment_card = dict([('cardToken', 'card token')])
        payment_card['cardUserKey'] = 'card user key'
        request['paymentCard'] = payment_card

        # make request
        basic_payment_pre_auth = iyzipay.BasicPaymentPreAuth()
        basic_payment_pre_auth_response = basic_payment_pre_auth.create(request, options)

        # get and print response
        print(basic_payment_pre_auth_response.read().decode('utf-8'))
