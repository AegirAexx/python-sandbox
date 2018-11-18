""" Project 1 in SC-T-111-FORR @ Reykjavik University """


def get_interest(ammount):
    """ Returns the ammount owed for interests """
    if ammount > 1000:
        return ammount - ammount * 0.98
    return ammount - ammount * 0.985


def print_line(month, payment, interest, remaining):
    """ Prints the output in required format. """
    print('Month:{month} '
          'Payment:{payment} '
          'Interest:{interest} '
          'Remaining debt:{remaining} '
          .format(month=month,
                  payment=round(payment, 2),
                  interest=round(interest, 2),
                  remaining=round(remaining, 2)))


def print_final(month, total_interest):
    """ Prints out the final message. """
    print('\nNumber of months: {m}'.format(m=month))
    print('Total interest paid: {t}'.format(t=round(total_interest, 2)))


def payment_plan(loan, payment):
    """ The work horse """
    print()
    remaining = loan
    interest = get_interest(remaining)
    total_interest = 0
    month = 0
    while remaining > 0:
        month += 1
        if remaining > 0:
            remaining += interest - payment
        if remaining < 0:
            remaining = 0
        print_line(month, payment, interest, remaining)
        total_interest += interest
        interest = get_interest(remaining)
        if remaining < payment:
            payment = remaining + interest
    print_final(month, total_interest)


def get_input():
    """ Gets input from the user. """
    loan_ammount = input('Input the loan ammount of the item in $:')
    payment_ammount = input('Input the payment each month in $:')
    monthly_payment = get_interest(int(loan_ammount))
    if monthly_payment < int(payment_ammount):
        payment_plan(int(loan_ammount), int(payment_ammount))
    else:
        print('\nYou would never be able to pay back your loan with\n'
              'those monthly payments at a 2% interest rate. '
              '\n\nSorry...\n\nLOAN DECLINED!!')


get_input()
