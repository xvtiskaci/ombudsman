import time

from selenium.webdriver.common.by import By

from elements.button import Button
from elements.input import Input
from pages.base_form import BaseForm
from utils.DriverUtils import DriverUtils


class AddRecommendationPage(BaseForm):
    __rec_txt = Input(By.XPATH, "//textarea[contains(@placeholder,'დავალების ტექსტი')]", "davalebis teqsti")
    __rec_type = Button(By.XPATH, "//div[@id='react-select-5-placeholder']", "rekomendacis tipi")
    __rec_button = Button(By.XPATH, "//div[@id='react-select-5-option-2']", "rekomendacia")
    __year_checkbox = Button(By.XPATH, "//div[@class=' css-1o2nmjj-placeholder']", "year checkbox")
    __year_button = Button(By.XPATH, "//div[contains(text(),'2022')]", "year")
    __date_picker = Button(By.XPATH, "//div[@class='DatePicker ']", "date picker")
    __pick_date = Button(By.XPATH, "//div[text()='25']", "15 sect")
    __establishment_picker = Button(By.XPATH, "//div[@class=' css-1o2nmjj-placeholder']", "establishment picker")
    __pick_establishment = Button(By.XPATH, "//div[contains(text(),'მერია')]", "palrament")
    __parliament_calculation_head = Button(By.XPATH, "//div[@class=' css-1o2nmjj-placeholder']", "saparlamento angarishis tavi")
    __pick_parliament_head = Button(By.XPATH, "//div[contains(text(),'სიცოცხლის უფლება')]", "sicocxlis ufleba")
    __add_word_code = Button(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div[1]/form/div[2]/div[7]/div/div[1]", "sityva kodebi")
    __pick_code_word = Button(By.XPATH, "//div[contains(text(),'წერო')]", "sityva kodis damateba")
    __fill_done_indicator = Input(By.XPATH, "//input[@placeholder='შესრულების ინდიკატორის სათაური']", "shesrulebis indikatoris satauri")
    __add_activity_main = Input(By.XPATH, "//input[@placeholder='აქტივობა (არასავალდებულო)']", "aqtivobis damateba")
    __add_activity_button = Button(By.XPATH, "//div[@class='_AppActivityButton_1nrfl_1']", "indikatorshi aqtivobis damatebis gilaki")
    __add_activity_child = Input(By.XPATH, "//div[@class='_AppForm__Container_1nxup_48']//div[3]//input[1]", "shvilobili aqtivoba")
    __plus_button = Button(By.XPATH, "//figure[@class='_AppButton__Add_11zhs_24']", "pliusis gilaki")
    __fill_another_indicator = Input(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div[1]/form/div[3]/div[2]/div[1]/input", "damatebuli indikatori")
    __fill_another_activiti = Input(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/div[1]/form/div[3]/div[2]/div[2]/input", "damatebuli aqtivoba")
    __send_pdf = Button(By.XPATH, "//h3[contains(text(),'ფაილის ატვირთვა')]", "pedefis damateba")
    __recommendation_add_button = Button(By.XPATH, "//button[@class='_AppButton_16gsi_1 _AppButton--FullWidth_16gsi_55']", "damatebis gilaki")
    __recomendation_menu = Button(By.XPATH, "//span[contains(text(),'რეკომენდაციები')]", "rekomendaciebis meniu")
    __all_rec = Button(By.XPATH,"//a[contains(text(),'ყველა')]", "yvela rekomendacia")

    def __init__(self):
        super().__init__(By.XPATH, "//h1[contains(text(),'დამატება')]", "title")

    def fill_rec_txt(self, value):
        locator = self.__rec_txt.by, self.__rec_txt.locator
        DriverUtils.wait_for_visible(locator)
        self.__rec_txt.send_text(value)

    def select_type(self):
        time.sleep(3)
        self.__rec_type.click()

    def click_recommendation(self):
        self.__rec_button.click()

    def check_year(self):
        self.__year_checkbox.click()

    def click_year(self):
        time.sleep(3)
        self.__year_button.click()

    def click_date_picker(self):
        self.__date_picker.click()

    def click_pick_date(self):
        self.__pick_date.click()

    def click_establishment(self):
        self.__establishment_picker.click()

    def pick_parlament(self):
        self.__pick_establishment.click()

    def click_parliament_head(self):
        self.__parliament_calculation_head.click()

    def click_life_rights(self):
        self.__pick_parliament_head.click()

    def click_word_code_bar(self):
        self.__add_word_code.click()

    def click_word_wero(self):
        self.__pick_code_word.click()

    def fill_indicator_title(self, value):
        self.__fill_done_indicator.send_text(value)

    def add_activity(self, activiti):
        self.__add_activity_main.send_text(activiti)

    def click_add_activity_button(self):
        self.__add_activity_button.click()

    def fill_activity_child(self, value):
        self.__add_activity_child.send_text(value)

    def click_plus_button(self):
        self.__plus_button.click()

    def fill_enother_indicator(self, value):
        self.__fill_another_indicator.send_text(value)

    def fill_another_activiti(self, value):
        self.__fill_another_activiti.send_text(value)

    def send_pdf(self):
        self.__send_pdf.click()

    def click_add_button(self):
        self.__recommendation_add_button.click()

    def click_rec_menu(self):
        self.__recomendation_menu.click()


    def click_rec_all(self):
        self.__all_rec.click()


