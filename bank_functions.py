from datetime import datetime, timedelta
import pprint


def init_bank_accounts() -> dict:
    '''
    Initialize the bank accounts data structure.
    :return:
    The bank accounts data structure (dict[any]) that includes the account data
    '''

    bank_accounts: dict = {
        1001: {
            "first_name": "Alice",
            "last_name": "Smith",
            "id_number": "123456789",
            "balance": 2500.50,
            "transactions_to_execute": [
                ("2024-08-17 14:00:00", 1001, 1002, 300), ("2024-08-17 15:00:00", 1001, 1003, 200)],
            "transaction_history": [
                ("2024-08-15 09:00:00", 1001, 1002, 500), ("2024-08-15 09:30:00", 1001, 1003, 100)]
        },
        1002: {
            "first_name": "Bob",
            "last_name": "Johnson",
            "id_number": "987654321",
            "balance": 3900.75,
            "transactions_to_execute": [],
            "transaction_history": []
        },
        1003: {
            "first_name": "Satoshi",
            "last_name": "Nakamoto",
            "id_number": "101001100",
            "balance": -12500.50,
            "transactions_to_execute": [],
            "transaction_history": []
        },
        1004: {
            "first_name": "John Pierpont",
            "last_name": "Morgan",
            "id_number": "987654321",
            "balance": 2200000000.75,
            "transactions_to_execute": [],
            "transaction_history": []
        }
    }
    return bank_accounts;


def trx_data(bank_accounts: dict) -> list:
    data_list: list = [];
    while True:
        try:
            data_list.append(int(input("sender account number: ")));
            if data_list[0] not in bank_accounts:
                print(f"sender account- {data_list[0]} - could not be found");
                continue;

            data_list.append(int(input("recipient account number: ")));
            if data_list[1] not in bank_accounts:
                print(f"recipient account- {data_list[1]} - could not be found");
                continue;

            data_list.append(float(input("sum of transfer: ")));
            if bank_accounts[data_list[0]]["balance"] < data_list[2]:
                print(f"sender account balance- {bank_accounts[data_list[0]]['balance']}\n"
                      f"the transfer sum - {data_list[2]}\n"
                      f"not enough balance");
                continue;

        except TypeError as e:
            print(f"{str(e)} - is not a valid input");

        except Exception as e:
            print(f"{e} - error has occurred");

        return data_list;


def create_trx(bank_accounts: dict, sender_account: int, receiver_account: int, trx_ammount: float) -> None:
    '''
    Create a new transaction for an account.
    :param bank_accounts:
    Bank accounts data (dict), sender account number, receiver account number, sum to transfer.
    :return:
    None
    '''
    temp_t: tuple = (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), sender_account, receiver_account, trx_ammount);
    bank_accounts[sender_account]["transactions_to_execute"].append(temp_t);


def get_account_number() -> int:
    '''
    get the account number from the user.
    :return:
    the account number as int if it is valid
    '''

    try:
        acc: int = int(input("account number: "));
    except TypeError as e:
        print(f"{str(e)} - is not a valid input");

    except Exception as e:
        print(f"{e} - error has occurred");

    return acc;


def perform_trx(bank_accounts: dict, acc_num: int) -> None:
    '''
    Commit the planed transactions for the given account.
    :param bank_accounts:
    Bank accounts data (dict), account number.
    :return:
    None
    '''

    if acc_num not in bank_accounts:
        print(f"account- {acc_num} - could not be found");
        # continue;
    transactions_pending: list[any] = bank_accounts[acc_num]["transactions_to_execute"][:];
    for tra in transactions_pending:
        bank_accounts[acc_num]['balance'] -= tra[3];
        bank_accounts[tra[2]]['balance'] += tra[3];
        bank_accounts[acc_num]["transaction_history"].append(tra);
        bank_accounts[acc_num]["transactions_to_execute"].remove(tra);
    # else:
    print();
    pprint.pprint(bank_accounts[acc_num]);


def get_id():
    while True:
        try:
            id_num: int = int(input("id number: "));
            return id_num;
        except TypeError as e:
            print(f"{str(e)} - is not a valid input");

        except Exception as e:
            print(f"{e} - error has occurred");


def find_by_id(bank_accounts: dict, id_num: int) -> dict:
    '''
    Find an account by users id number. And display its data.
    :param id_num:
    the account owners id
    :param bank_accounts:
    Bank accounts data (dict).
    :return:
    None
    '''

    for key in bank_accounts.keys():
        if bank_accounts[key]["id_number"] == str(id_num):
            return bank_accounts[key];


def get_acc_name() -> str:
    name: str = input("first name: ");
    return name;


def get_by_name(bank_accounts: dict, name: str) -> dict:
    '''
    Find an account by users name or part of it. And display its data.
    :param name:
    first name of account owner
    :param bank_accounts:
    Bank accounts data (dict).
    :return:
    None
    '''

    for key in bank_accounts.keys():
        if name.lower() in bank_accounts[key]["first_name"].lower():
            return bank_accounts[key];


def accounts_sorted_by_balance(bank_accounts: dict) -> None:
    '''
    Display all accounts data sorted by balance.
    :param bank_accounts:
    Bank accounts data (dict).
    :return:
    None
    '''

    acc_list: list = sorted(bank_accounts.keys(), key=lambda acc: bank_accounts[acc]['balance']);
    for acc_n in acc_list:
        pprint.pprint(bank_accounts[acc_n]);


def accounts_with_negative_balance(bank_accounts: dict) -> None:
    '''
    Display data of the accounts with negative balance.
    :param bank_accounts:
    Bank accounts data (dict).
    :return:
    None
    '''

    for key in bank_accounts.keys():
        if bank_accounts[key]["balance"] < 0:
            pprint.pprint(bank_accounts[key]);


def accounts_balance_sum(bank_accounts: dict) -> None:
    '''
    Display the sum of all founds in the accounts (sum of account balances)
    :param bank_accounts:
    Bank accounts data (dict).
    :return:
    None
    '''

    print(f"sum of all accounts: {sum(map(lambda key: bank_accounts[key]['balance'], bank_accounts))}");


def transactions_today(bank_accounts: dict) -> None:
    '''
    Display all of today's transactions (that were commited)
    :param bank_accounts:
    Bank accounts data (dict).
    :return:
    None
    '''

    tod_tr: list = [];
    today: str = datetime.today().strftime('%Y-%m-%d');
    for key in bank_accounts.keys():
        for transaction in bank_accounts[key]["transaction_history"]:
            tr_date: list[str] = str(transaction[0]).split(' ')[0];
            print(tr_date);
            if tr_date == today:
                tod_tr.append(transaction);
    print(f"today's transactions:\n{tod_tr}");


def open_new_account(bank_accounts: dict) -> None:
    '''
    Open a new bank account.
    :param bank_accounts:
    Bank accounts data (dict).
    :return:
    None
    '''

    acc_num: int = max(bank_accounts.keys()) + 1;
    fname: str = input("first name: ");
    lname: str = input("last name: ");
    id_num: str = input("id number: ");
    try:
        bal: int = int(input("starting balance: "));

        new_acc: dict = {
            "first_name": fname,
            "last_name": lname,
            "id_number": id_num,
            "balance": bal,
            "transactions_to_execute": [],
            "transaction_history": []
        }

        bank_accounts[acc_num] = new_acc;
    except TypeError as e:
        print(f"{str(e)} - is not a valid input");

    except Exception as e:
        print(f"{e} - error has occurred");
    finally:
        print(f"{fname} {lname} - thanks for joining our bank!\nyour money is in good hands.")


def view_reports(bank_accounts: dict) -> None:
    '''
    Open the view reports menu. Allows report actions (such as: finding an account by id or name, or the display of all
    negative balance accounts, etc. )
    :param bank_accounts:
    Bank accounts data (dict).
    :return:
    None
    '''

    print("===========Report Menu==============")
    print("0 - back to previous menu\n1 - print all\n2 - print account\n3 - find by id\n4 - find by name\n"
          "5 - print all accounts sorted by balance\n6 -  print all account with negative balance\n"
          "7 - print sum of all accounts\n8 - print transactions today");
    try:
        action: int = int(input("What is the purpose of your visit? "));
        while True:
            match action:
                case 0:
                    return;
                case 1:
                    pprint.pprint(bank_accounts);
                    return;
                case 2:
                    acc: int = int(input("account number: "));
                    if acc in bank_accounts.keys():
                        pprint.pprint(bank_accounts[acc]);
                    else:
                        print(f"account- {acc} - could not be found");
                    return;
                case 3:
                    pprint.pprint(find_by_id(bank_accounts, get_id()));
                    return;
                case 4:
                    pprint.pprint(get_by_name(bank_accounts, get_acc_name()));
                    return;
                case 5:
                    accounts_sorted_by_balance(bank_accounts);
                    return;
                case 6:
                    accounts_with_negative_balance(bank_accounts);
                    return;
                case 7:
                    accounts_balance_sum(bank_accounts);
                    return;
                case 8:
                    transactions_today(bank_accounts);
                    return;
                case _:
                    print("invalid input");
                    continue;
    except TypeError as e:
        print(f"{str(e)} - is not a valid input");

    except Exception as e:
        print(f"{e} - error has occurred");
    finally:
        print("You are exiting the reports menu")


def main_menu(bank_accounts: dict) -> None:
    '''
    Opens the main manu of the bank. Allows main menu actions
    (such as: opening a new account, or creating a new transaction, etc. ).
    :param bank_accounts:
    Bank accounts data (dict).
    :return:
    None
    '''

    # action: int = None;
    while True:
        print("===========Main Menu==============")
        print("0 - open new account\n1 - new transaction\n2 - commit all transactions\n3 - reports menu\n999 - exit");
        try:
            action: int = int(input("What is the purpose of your visit? "));
            match action:
                case 0:
                    open_new_account(bank_accounts);
                case 1:
                    transfer: list = trx_data(bank_accounts);
                    print(transfer);
                    create_trx(bank_accounts, transfer[0], transfer[1], transfer[2]);
                case 2:
                    perform_trx(bank_accounts, get_account_number());
                case 3:
                    view_reports(bank_accounts);
                case 999:
                    print("leaving the system, have a nice day!")
                    break;
                case _:
                    print("invalid input");
                    continue;

            print();

        except TypeError as e:
            print(f"{str(e)} - is not a valid input");

        except Exception as e:
            print(f"{e} - error has occurred");
        finally:
            print("Dear client, we thank you for choosing our bank.\nHave a great day!")

# bank_ac = init_bank_accounts();
# accounts_balance_sum(bank_ac);
