import logging


def main():
    logging.basicConfig(level=logging.INFO, filename='app.log')
    while True:
        action = ''
        try:
            x = float(input("first value = "))
            logging.info(f'Your first value = {x}')
            action = input("action: ")
            logging.info(f'Your action = {action}')
            y = float(input("second value = "))
            logging.info(f'Your second value = {y}')
        except ValueError:
            print('Value Error')
            logging.error("Exception occurred", exc_info=True)
            continue
        if action in ('+', '-', '*', '/'):
            try:
                if action == '+':
                    print('%.0f + %.0f = %.0f' % (x, y, x+y))
                if action == '-':
                    print('%.0f - %.0f = %.0f' % (x, y, x-y))
                if action == '*':
                    print('%.0f * %.0f = %.0f' % (x, y, x*y))
                if action == '/':
                    print('%.0f / %.0f = %.0f' % (x, y, x/y))
            except ZeroDivisionError:
                print('Division by zero')
        else:
            print('No such action')


if __name__ == '__main__':
    main()

