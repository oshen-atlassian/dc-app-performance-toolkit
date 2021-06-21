from selenium.webdriver.common.by import By

from selenium_ui.confluence.pages.pages import Editor
from selenium_ui.conftest import print_timing
# def app_specific_action(webdriver, datasets):
#     page = BasePage(webdriver)
#     if datasets['custom_pages']:
#         app_specific_page_id = datasets['custom_page_id']

# To run action as specific user uncomment code bellow.
# NOTE: If app_specific_action is running as specific user, make sure that app_specific_action is running
# just before test_2_selenium_z_log_out
# @print_timing("selenium_app_specific_user_login")
# def measure():
#     def app_specific_user_login(username='admin', password='admin'):
#         login_page = Login(webdriver)
#         login_page.delete_all_cookies()
#         login_page.go_to()
#         login_page.wait_for_page_loaded()
#         login_page.set_credentials(username=username, password=password)
#         login_page.click_login_button()
#         if login_page.is_first_login():
#             login_page.first_user_setup()
#         all_updates_page = AllUpdates(webdriver)
#         all_updates_page.wait_for_page_loaded()
#     app_specific_user_login(username='admin', password='admin')
# measure()

# @print_timing("selenium_app_custom_action")
# def measure():
#     @print_timing("selenium_app_custom_action:view_page")
#     def sub_measure():
#         page.go_to_url(f"{CONFLUENCE_SETTINGS.server_url}/pages/viewpage.action?pageId={app_specific_page_id}")
#         page.wait_until_visible((By.ID, "title-text"))  # Wait for title field visible
#         page.wait_until_visible(
#             (By.ID, "ID_OF_YOUR_APP_SPECIFIC_UI_ELEMENT"))  # Wait for you app-specific UI element by ID selector
#
#     sub_measure()
#
# measure()

def app_specific_create_content(webdriver, datasets):
    edit_page = Editor(webdriver, page_id=datasets['page_id'])

    @print_timing("app_specific_edit_page")
    def measure():
        @print_timing("selenium_edit_page:open_create_page_editor")
        def sub_measure():
            edit_page.go_to()
            edit_page.wait_for_page_loaded()

        sub_measure()

        unknown_attachment_html = '<img class="confluence-embedded-image confluence-external-resource" ' \
                                  'src="http://bulldogwiki.internal.atlassian.com/wiki/plugins/servlet/confluence' \
                                  '/placeholder/unknown-attachment?locale=en_US&amp;version=2" ' \
                                  'data-image-src="http://bulldogwiki.internal.atlassian.com/wiki/plugins/servlet' \
                                  '/confluence/placeholder/unknown-attachment?locale=en_US&amp;version=2"> '
        edit_page.hard_set_tinymce_html(unknown_attachment_html)

        @print_timing("selenium_edit_page:save_edited_page")
        def sub_measure():
            edit_page.save_edited_page()

        sub_measure()

    measure()
