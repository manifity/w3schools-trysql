class SQLPageLocators:

    @staticmethod
    def code_mirror_block(request):
        return f'window.editor.setValue("{request}")'

    run_sql_button = 'css:.w3-green'
    table_results_counter = 'xpath://*[contains(text(),"Number of Record")]'
    table_rows = 'xpath://table[@class="w3-table-all notranslate"]/tbody/tr'
    sql_request_success = 'css:#divResultSQL > div'
