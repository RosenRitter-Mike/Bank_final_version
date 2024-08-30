import bank_functions as bf


def main():
    bank_data = bf.init_bank_accounts()
    bf.main_menu(bank_data);


if __name__ == "__main__":
    main()