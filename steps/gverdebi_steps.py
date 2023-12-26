from pages.gverdebi_page import GverdebiPage


class GverdebiPageSteps:

    @staticmethod
    def gverdebi_page_steps():
        value = "test_title"
        red_value = "red_title_test"
        gverdebi_page = GverdebiPage()
        gverdebi_page.click_pages_menu()
        gverdebi_page.is_visible()
        gverdebi_page.click_add_new_button()
        gverdebi_page.fill_head_name(value)
        gverdebi_page.click_add_button()
        added_page_list = gverdebi_page.find_edit_button()
        last_menu_edit = added_page_list[len(added_page_list) - 1]
        last_menu_edit.click()
        gverdebi_page.redact_head_name(red_value)
        gverdebi_page.click_add_button()
        gverdebi_page.click_back()
        redacted_page_list = gverdebi_page.find_delete_button()
        last_menu_delete = redacted_page_list[len(redacted_page_list) - 1]
        last_menu_delete.click()
        gverdebi_page.click_confirm_delete()