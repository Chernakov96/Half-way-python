from .logger import logging

AVAILABLE_MODES_MAIN_MENU = 6
MUST_BE_INTEGER = 'Incorrect input! Input must be an integer.'
INCORRECT_INPUT = 'Incorrect input! Please look at the available modes.'
NO_VALID_FILE = 'No valid file for reading.'


def validation_mode() -> int:
    """ Function for check user's input from main mode.
    \nChecks user input and returns main menu mode. """
    while True:
        try:
            main_menu_mode = int(input('Which mode do you need: '))
        except ValueError as err:
            print(MUST_BE_INTEGER)
            logging.exception(err)
            continue
        if main_menu_mode in range(AVAILABLE_MODES_MAIN_MENU):
            if main_menu_mode == 0:
                logging.info('Finished work from main menu.')
            else:
                logging.info(f'Main mode of interface = {main_menu_mode}')
            return main_menu_mode
        print(INCORRECT_INPUT)
        logging.exception(INCORRECT_INPUT)


def validation_operation(main_menu_mode: int) -> int:
    """ Function for check user's input for operation mode.
    \nChecks user input and returns operation mode. """
    match main_menu_mode:
        case 1:
            return validate_read()
        case 2:
            return 21
        case 3:
            return 31
        case 4:
            return 41
        case 5:
            return 51
        case _:
            logging.INFO(INCORRECT_INPUT)


def validate_read() -> int:
    """ Function for check user's input for reading operation type.
    \nChecks user input and returns operation type. """
    number_of_available_modes = 4
    while True:
        try:
            operation_type = int(input('Enter operation code: '))
        except ValueError as err:
            print(MUST_BE_INTEGER)
            logging.exception(err)
            continue
        if operation_type in range(number_of_available_modes):
            logging.info(f'Operation code for read = {operation_type + 10}')
            return operation_type + 10
        print(INCORRECT_INPUT)
        logging.exception(INCORRECT_INPUT)


def validation_filename() -> str:
    """ Function for check user's input for filename.
    \nChecks user input and returns filename. """
    while True:
        try:
            filename = input('Enter filename: ').strip()
        except Exception as err:
            print('Something went wrong when reading filename. Try again.')
            logging.exception(err)
            continue
        if not filename:
            print('Reading default file.')
            logging.info('Reading default file.')
            return filename
        elif not filename.isalnum():
            print('Please use only letters and numbers in filename.')
            logging.info(f'Corrupt filename {filename}.')
            continue
        print(f'Valid for read {filename = }.')
        logging.info(f'Valid for read {filename = }.')
        return filename


def validation_id(data: dict) -> int:
    """ Function for check user's input for id selection.
        \nChecks user input and returns selected id of the note. """
    while True:
        try:
            available_ids = [data['notes'][i]['id'] for i in range(len(data['notes']))]
            selected_id = int(input('Enter id of the note: '))
            if selected_id in available_ids:
                logging.info(f'{selected_id = }')
                return selected_id
        except ValueError as err:
            print(MUST_BE_INTEGER)
            logging.exception(err)
            continue
        except TypeError as error:
            print('Corrupted data file.')
            logging.exception(error)
            return -1
        except KeyError as error:
            print(NO_VALID_FILE)
            logging.exception(error)
            break;
        print('Incorrect ID! Please look at the available IDs in the table above.')
        logging.exception('Incorrect ID! Please look at the available IDs in the table above.')


def validation_data(max_symbols: int) -> str:
    """ Function for check user's input for note filling.
        \nChecks user input and returns string. """
    while True:
        try:
            fill_data = input(f'Type something. Max {max_symbols} characters: ')
        except Exception as err:
            print('Something went wrong when collecting data. Try again.')
            logging.exception(err)
            continue
        if len(fill_data) in range(max_symbols + 1):
            logging.info(f'Entered data for note {fill_data = } with length = {len(fill_data)}.')
            return fill_data
        print(f'Max characters is {max_symbols}.')
        logging.info(f'Entered data for note {fill_data = } with length = {len(fill_data)}.')


def validate_edit() -> int:
    """ Function for check user's input for editing the note operation type.
    \nChecks user input and returns operation type. """
    number_of_available_modes = 3
    while True:
        try:
            operation_type = int(input('Enter operation code: '))
        except ValueError as err:
            print(MUST_BE_INTEGER)
            logging.exception(err)
            continue
        if operation_type in range(number_of_available_modes):
            logging.info(f'Operation code for read = {operation_type + 30}')
            return operation_type + 30
        print(INCORRECT_INPUT)
        logging.exception(INCORRECT_INPUT)