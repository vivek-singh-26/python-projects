import argparse
import math
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--type', help='Choose between Differentiated or Annuity payment methods')
parser.add_argument('--principal', help='Give the principal')
parser.add_argument('--periods', help='Give the period')
parser.add_argument('--interest', type=float, help='Give the interest')
parser.add_argument('--payment', help='Give the payment')

args = parser.parse_args()

if args.principal is not None:
    principal = int(args.principal)
else:
    principal = None

if args.periods is not None:
    periods = int(args.periods)
else:
    periods = None

if args.payment is not None:
    payment = int(args.payment)
else:
    payment = None

if args.interest is not None:
    interest = args.interest/(12*100)
else:
    interest = None


def differentiated_payment():
    curr_rep_mon = 1
    all_payment = 0
    for x in range(periods):
        diff_payment = (principal/periods) + interest * (principal - (principal*(curr_rep_mon-1)/periods))
        curr_rep_mon += 1
        all_payment += math.ceil(diff_payment)
        print(f'Month {x+1}: payment is {math.ceil(diff_payment)}')
    overpayment = all_payment - principal
    print(f'\nOverpayment = {overpayment}')


def loan_principal():
    l_principal = payment / (
                (interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1))
    print(f'Your loan principal = {math.floor(l_principal)}!')

    diff_overpayment = payment * periods - l_principal
    print(f'\nOverpayment = {diff_overpayment}')


def time_taken_to_repay():
    no_of_periods = math.ceil(
        math.log(payment / (payment - (interest * principal)), 1 + interest))
    year = int(no_of_periods // 12)
    months = math.ceil(no_of_periods % 12)

    if year == 1 and months == 0:
        print(f'It will take {year} year to repay this loan!')
    elif year > 1 and months == 0:
        print(f'It will take {year} years to repay this loan!')
    elif year < 0:
        print(f'It will take {months} months to repay this loan!')
    else:
        print(f'It will take {year} years and {months} months to repay this loan!')

    overpayment = payment * no_of_periods - principal
    print(f'Overpayment = {overpayment}')


def annuity_payment():
    ann_payment = principal * (
                (interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1))
    print(f'Your monthly payment = {math.ceil(ann_payment)}!')

    overpayment = math.ceil(ann_payment) * periods - principal
    print(f'Overpayment = {overpayment}')


if args.type == 'diff' and interest is not None:
    differentiated_payment()
elif args.type == 'annuity' and payment is None:
    annuity_payment()
elif args.type == 'annuity' and payment is not None and interest is not None:
    if periods is not None:
        loan_principal()
    elif principal is not None:
        time_taken_to_repay()
elif args.type not in ['diff', 'annuity'] or len(sys.argv) < 5 or interest is None:
    print('Incorrect parameters')

