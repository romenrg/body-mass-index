import argparse
import sys
import pprint

from bmi import Bmi

def execute_calculate(args):
    return Bmi.calculate_bmi(args.weight[0], args.height[0])

def execute_calculate_bmi_with_info(args):
    if args.lang:
        return Bmi.calculate_bmi_with_info(args.weight[0], args.height[0], args.lang)
    else:
        return Bmi.calculate_bmi_with_info(args.weight[0], args.height[0])

def execute_range_info(args):
    if args.lang:
        return Bmi.range_info(args.bmi[0], args.lang)
    else:
        return Bmi.range_info(args.bmi[0])

def execute_ranges_with_info(args):
    return Bmi.ranges_with_info(args.lang)

def execute_calculate_weight(args):
    return Bmi.calculate_weight(args.height[0], args.bmi[0])

def execute_healthy_weight(args):
    return Bmi.calculate_healthy_weight(args.height[0])

def subparserIsEnabled(args):
    return (len(sys.argv) > 1) and (hasattr(args, 'func'))

def cli():
    parser = argparse.ArgumentParser(description='BMI', prog='python3 -m bmi', usage='%(prog)s')
    subparsers = parser.add_subparsers(title="available commands", help='More information:')
    sub_cmd_calculate = subparsers.add_parser('calculate', help='Calculate BMI, providing weight and height')
    sub_cmd_calculate.set_defaults(func=execute_calculate)
    sub_cmd_calculate.add_argument('weight', metavar='weight', type=float, nargs=1, help='weight in kilograms (e.g. 80)')
    sub_cmd_calculate.add_argument('height', metavar='height', type=float, nargs=1, help='height in meters (e.g. 1.80)')
    sub_cmd_calculate_w_info = subparsers.add_parser('calculate_info', help='Calculate BMI with range info, providing weight, height and language')
    sub_cmd_calculate_w_info.set_defaults(func=execute_calculate_bmi_with_info)
    sub_cmd_calculate_w_info.add_argument('weight', metavar='weight', type=float, nargs=1, help='weight in kilograms (e.g. 80)')
    sub_cmd_calculate_w_info.add_argument('height', metavar='height', type=float, nargs=1, help='height in meters (e.g. 1.80)')
    sub_cmd_calculate_w_info.add_argument('--lang', metavar='lang', type=str, nargs='?', default='en', help='language <"en" (default) or "es">')
    sub_cmd_range_info = subparsers.add_parser('range_info', help='Return range info, providing BMI and language')
    sub_cmd_range_info.set_defaults(func=execute_range_info)
    sub_cmd_range_info.add_argument('bmi', metavar='bmi', type=float, nargs=1, help='Body Mass Index (BMI) value (e.g. 22)')
    sub_cmd_range_info.add_argument('--lang', metavar='lang', type=str, nargs='?', default='en', help='language <"en" (default) or "es">')
    sub_cmd_ranges_w_info = subparsers.add_parser('ranges_info', help='Return info of all ranges')
    sub_cmd_ranges_w_info.add_argument('--lang', metavar='lang', type=str, nargs='?', default='en', help='language <"en" (default) or "es">')
    sub_cmd_ranges_w_info.set_defaults(func=execute_ranges_with_info)
    sub_cmd_calculate_weight = subparsers.add_parser('calculate_weight', help='Calculate, providing height and BMI')
    sub_cmd_calculate_weight.set_defaults(func=execute_calculate_weight)
    sub_cmd_calculate_weight.add_argument('height', metavar='height', type=float, nargs=1, help='height in meters (e.g. 1.80)')
    sub_cmd_calculate_weight.add_argument('bmi', metavar='bmi', type=float, nargs=1, help='Body Mass Index (BMI) value (e.g. 22)')

    sub_cmd_healthy_weight = subparsers.add_parser('healthy_weight', help='Show healthy weight range, providing height')
    sub_cmd_healthy_weight.set_defaults(func=execute_healthy_weight)
    sub_cmd_healthy_weight.add_argument('height', metavar='height', type=float, nargs=1, help='height in meters (e.g. 1.80)')
    args = parser.parse_args()
    if subparserIsEnabled(args):
        result = args.func(args)
        if isinstance(result, list):
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(result)
        else:
            print(result)
    else:
        parser.print_help()


# Start CLI
cli()