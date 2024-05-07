from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ApiDemosTests:
    def __init__(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities={
                'platformName': 'Android',
                'automationName': 'uiautomator2',
                'platformVersion': '13',
                'deviceName': 'Android Emulator',
                'app': '',
                'noReset': True,
            }
        )

    def inicio_la_aplicacion_apidemos(self):
        assert self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiSelector().text("API Demos")').is_displayed()

    def deberia_ver_la_opcion_app_en_la_pantalla_de_inicio(self):
        assert self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("App")').is_displayed()

    def estoy_en_la_pantalla_de_inicio(self):
        assert self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiSelector().text("API Demos")').is_displayed()

    def doy_clic_en_la_opcion_app(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("App")').click()

    def deberia_ver_una_lista_de_opciones_de_aplicacion(self):
        assert self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiSelector().text("Action Bar")').is_displayed()
        assert self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiSelector().text("Voice Recognition")').is_displayed()

    def deberia_ver_la_opcion_alarm(self):
        assert self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiSelector().text("Alarm")').is_displayed()

    def estoy_en_la_pantalla_de_lista_de_opciones_de_aplicacion(self):
        assert self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiSelector().text("Action Bar")').is_displayed()
        assert self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiSelector().text("Voice Recognition")').is_displayed()

    def doy_clic_en_la_opcion_alarm(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiSelector().text("Alarm")').click()

    def deberia_ver_una_pantalla_con_las_opciones_de_alarma(self):
        assert self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiSelector().text("Alarm Controller")').is_displayed()
        assert self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiSelector().text("Alarm Service")').is_displayed()

    def estoy_en_la_pantalla_de_opciones_de_alarma(self):
        assert self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiSelector().text("Alarm Controller")').is_displayed()
        assert self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiSelector().text("Alarm Service")').is_displayed()

    def doy_clic_en_la_opcion_alarm_service(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiSelector().text("Alarm Service")').click()

    def doy_clic_en_el_boton_start_alarm_service(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiSelector().text("Start Alarm Service")').click()

    def deberia_ver_un_mensaje_de_alerta_diciendo_repeating_alarm_will_go_off_in_15_seconds_and_every_15_seconds_after_based_on_the_elapsed(
            self):  # nopep8
        self.__validar_mensajes_alerta("Repeating alarm will go off in 15 seconds and every 15 seconds "
                                       "after based on the elapsed")

    def doy_clic_en_el_boton_stop_alarm_service(self):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiSelector().text("Stop Alarm Service")').click()

    def deberia_ver_un_mensaje_de_alerta_diciendo_repeating_alarm_has_been_unscheduled(self):
        self.__validar_mensajes_alerta("Repeating alarm has been unscheduled")

    def __validar_mensajes_alerta(self, mensaje):
        locator_toast = f"//*[contains(@text, '{mensaje}')]"
        WebDriverWait(self.driver, 5).until(
            ec.presence_of_element_located((
                MobileBy.XPATH,
                locator_toast
            ))
        )
        mensaje_toast = self.driver.find_element(
            MobileBy.XPATH,
            locator_toast
        )
        assert mensaje_toast, f"El mensaje Toast con el texto '{mensaje}' no fue encontrado."

