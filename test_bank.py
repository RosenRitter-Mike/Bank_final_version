import bank_functions as bf
from datetime import datetime, timedelta
import pytest


def test_empty_exe_preform_trx():
    bank_data = bf.init_bank_accounts()
    bf.perform_trx(bank_data, 1001);
    actual: list = bank_data[1001]['transactions_to_execute'];

    assert actual == [];


def test_history_exe_preform_trx():
    bank_data = bf.init_bank_accounts()
    temporary: list = bank_data[1001]['transactions_to_execute'].copy();
    bf.perform_trx(bank_data, 1001);
    actual: list = bank_data[1001]['transaction_history'];

    assert set(temporary) < set(actual);


def test_change_balance_preform_trx():
    bank_data = bf.init_bank_accounts()
    balance: float = bank_data[1001]['balance'];
    change: float = 0;

    transactions_pending: list[any] = bank_data[1001]["transactions_to_execute"][:];
    for tra in transactions_pending:
        change += tra[3];

    bf.perform_trx(bank_data, 1001);
    actual: float = bank_data[1001]['balance'];

    assert actual == balance - change;


def test_get_change_preform_trx():
    bank_data = bf.init_bank_accounts();

    sum_list: list = [];
    balance_list: list = [];
    keys_list: list = [];
    transactions_pending: list[any] = bank_data[1001]["transactions_to_execute"][:];
    for tra in transactions_pending:
        sum_list.append(tra[3]);
        keys_list.append(tra[2]);
        balance_list.append(bank_data[tra[2]]['balance']);

    bf.perform_trx(bank_data, 1001);
    for i in range(len(keys_list)):
        if bank_data[keys_list[i]]['balance'] != balance_list[i] + sum_list[i]:
            assert False;

    assert True;


def test_create_trx():
    bank_data = bf.init_bank_accounts();
    exe_trx_len: int = len(bank_data[1004]["transactions_to_execute"]);
    bf.create_trx(bank_data, 1004, 1003, 14000);
    # transactions_pending: list[any] = bank_data[1004]["transactions_to_execute"][:];
    # for tra in transactions_pending:
    now: str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    last_trx: tuple = bank_data[1004]["transactions_to_execute"][len(bank_data[1004]["transactions_to_execute"])-1];
    if len(bank_data[1004]["transactions_to_execute"]) != exe_trx_len + 1:
        assert False;
    elif last_trx[0] != now:
        assert False;
    elif last_trx[1] != 1004:
        assert False;
    elif last_trx[2] != 1003:
        assert False;
    elif last_trx[3] != 14000:
        assert False;
    else:
        assert True;


def test_get_by_name():
    bank_data = bf.init_bank_accounts();
    assert bf.get_by_name(bank_data, "bo") == bank_data[1002];

def test_find_by_id():
    bank_data = bf.init_bank_accounts();
    assert bf.find_by_id(bank_data, 987654321)== bank_data[1002];
