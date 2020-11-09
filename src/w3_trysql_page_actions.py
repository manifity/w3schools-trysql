import allure
from time import sleep
from src.base_page import BasePage
from src.locators import SQLPageLocators


class SQLStatement(BasePage):

    @allure.step('Ввод SQL запроса в соответствующее поле')
    def input_sql_request(self, request):
        self._driver.execute_script(SQLPageLocators.code_mirror_block(request))

    @allure.step('Нажатие на кнопку "Run SQL"')
    def press_run_sql_button(self):
        self.get_element_and_click(SQLPageLocators.run_sql_button)
        sleep(1)


class SQLResults(BasePage):

    @allure.step('Количество результатов запроса')
    def quantity_table_results(self):
        return self.get_element_text(SQLPageLocators.table_results_counter)

    @allure.step('Получение строк таблицы')
    def get_result_from_table(self):
        table_strings = self.get_elements(SQLPageLocators.table_rows)

        string_text = []
        for i in range(0, len(table_strings)):
            cols = table_strings[i].text
            string_text.append(cols)

        return string_text

    @allure.step('Проверка строки в таблице')
    def check_single_row_in_table(self, rows, row_string):
        matches = 0
        for i in range(0, len(rows)):
            if row_string in rows[i]:
                matches += 1

        if matches == 1:
            return True
        else:
            return False

    @allure.step('Проверка двух значений в таблице')
    def check_two_value_in_table_row(self, rows, first_value, second_value):
        matches = 0
        for i in range(0, len(rows)):
            if first_value and second_value in rows[i]:
                matches += 1

        if matches == 1:
            return True
        else:
            return False

    @allure.step('Подсчёт количества совпадений в таблице')
    def count_values_in_table_strings(self, rows, value):
        matches = 0
        for i in range(0, len(rows)):
            if value in rows[i]:
                matches += 1

        return matches

    @allure.step('Получение текста о внесённых изменениях')
    def check_made_changes(self):
        return self.get_element_text(SQLPageLocators.sql_request_success)
