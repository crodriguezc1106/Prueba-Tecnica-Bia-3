*** Settings ***
Documentation     Pruebas de servicio de alarma en la aplicacion ApiDemos
Libraryappium           ../resources/ApiDemosTests.py

*** Test Cases ***
Visualizar la opción de aplicación en la pantalla de inicio
    Given Inicio la aplicacion apidemos
    Then Deberia ver la opcion App en la pantalla de inicio

Navegar a la pantalla con la lista de opciones de aplicación
    Given Estoy en la pantalla de inicio
    When Doy clic en la opcion App
    Then Deberia ver una lista de opciones de aplicacion
    And Deberia ver la opcion Alarm

Navegar a la pantalla con las opciones de alarma
    Given Estoy en la pantalla de lista de opciones de aplicacion
    When Doy clic en la opcion Alarm
    Then Deberia ver una pantalla con las opciones de alarma

Iniciar el servicio de alarma
    Given Estoy en la pantalla de opciones de alarma
    When Doy clic en la opcion Alarm Service
    And Doy Clic En El Boton Start Alarm Service
    Then Deberia ver un mensaje de alerta diciendo Repeating alarm will go off in 15 seconds and every 15 seconds after based on the elapsed

Detener el servicio de alarma
    Given Estoy en la pantalla de opciones de alarma
    When Doy clic en la opcion Alarm service
    And Doy clic en el boton Stop Alarm Service
    Then Deberia ver un mensaje de alerta diciendo Repeating alarm has been unscheduled