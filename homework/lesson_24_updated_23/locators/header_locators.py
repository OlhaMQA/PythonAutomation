class HeaderLocatorsCollection:
    def __init__(self):
        self.__burger_menu = ('xpath', '//button[@aria-label="menu"]')
        self.__close_menu = ('xpath', '//button[@class="icon f-navbtn"]')
        self.__logo = ('xpath', '//img[@alt="Examples.com"]')
        self.__header = ('xpath', '//header')
        self.__search_icon = ('xpath', '//button[@class="icon search-iocn"]')
        self.__search_field = ('xpath', '//input[@id="headerSearch"]')

    @property
    def burger_menu(self):
        return self.__burger_menu

    @property
    def close_menu(self):
        return self.__close_menu

    @property
    def logo(self):
        return self.__logo

    @property
    def header(self):
        return self.__header

    @property
    def search_icon(self):
        return self.__search_icon

    @property
    def search_field(self):
        return self.__search_field



