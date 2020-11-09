import allure
from src.w3_trysql_page_actions import SQLStatement, SQLResults
from src.credo import select_all_request, select_by_city, insert_request, insert_string, update_request, update_string,\
    join_request, made_changes, customer_contact, customer_address, company, supplier, product


@allure.title('Проверка заказчика и его адреса в таблице Customers')
def test_check_customer_and_address(chrome):
    """
    Вывести все строки таблицы *Customers* и убедиться, что запись с ContactName равной ‘Giovanni Rovelli’
    имеет Address = ‘Via Ludovico il Moro 22’.
    """
    SQLStatement(chrome).input_sql_request(select_all_request)
    SQLStatement(chrome).press_run_sql_button()

    rows = SQLResults(chrome).get_result_from_table()
    assert SQLResults(chrome).check_two_value_in_table_row(rows, customer_contact, customer_address) is True


@allure.title('Проверка количества записей по названию города в таблице Customers')
def test_check_city(chrome):
    """
    Вывести только те строки таблицы *Customers*, где city='London'. Проверить, что в таблице ровно 6 записей.
    """
    SQLStatement(chrome).input_sql_request(select_by_city('\'London\''))
    SQLStatement(chrome).press_run_sql_button()

    assert 'Number of Records: 6' == SQLResults(chrome).quantity_table_results()


@allure.title('Добавление заказчика в таблицу Customers')
def test_add_customer(chrome):
    """
    Добавить новую запись в таблицу *Customers* и проверить, что эта запись добавилась.
    """
    # INSERT NEW DATA TO DB
    SQLStatement(chrome).input_sql_request(insert_request)
    SQLStatement(chrome).press_run_sql_button()

    assert SQLResults(chrome).check_made_changes() == made_changes

    # CHECK UPDATES IN DB

    SQLStatement(chrome).input_sql_request(select_all_request)
    SQLStatement(chrome).press_run_sql_button()

    rows = SQLResults(chrome).get_result_from_table()
    assert SQLResults(chrome).check_single_row_in_table(rows, insert_string) is True


@allure.title('Обновление всех полей одной записи в таблице Customers')
def test_change_rows_data(chrome):
    """
    Обновить все поля (кроме CustomerID) в любой записи таблицы *Customers*
    и проверить, что изменения записались в базу.
    """
    SQLStatement(chrome).input_sql_request(update_request)
    SQLStatement(chrome).press_run_sql_button()

    assert SQLResults(chrome).check_made_changes() == made_changes

    # CHECK UPDATES
    SQLStatement(chrome).input_sql_request(select_all_request)
    SQLStatement(chrome).press_run_sql_button()

    rows = SQLResults(chrome).get_result_from_table()
    assert SQLResults(chrome).check_single_row_in_table(rows, update_string)


@allure.title('Проверка заказчика и его продукта')
def test_check_supplier_and_product(chrome):
    """
    Придумать собственный автотест и реализовать (тут все ограничивается только вашей фантазией)

    Проверить, что у заказчика 'Hungry Owl All-Night Grocers' было не менее 2-х заказов у поставщика 'Leka Trading',
    и что этот поставщик не поставлял продукт 'Chang'.
    """
    SQLStatement(chrome).input_sql_request(join_request(company, supplier))
    SQLStatement(chrome).press_run_sql_button()

    rows = SQLResults(chrome).get_result_from_table()

    assert SQLResults(chrome).count_values_in_table_strings(rows, supplier) == 2
    assert SQLResults(chrome).check_single_row_in_table(rows, product) is False
