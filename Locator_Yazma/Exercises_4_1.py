from selenium.webdriver.common.by import By


class Locators:
    # UTM settings on Newsletter design page
    UTM_CHECKBOX = (By.CLASS_NAME, ".checkboxDefault")
    # on Maven design page, when you rename variation cross button
    MAVEN_CROSS_BUTTON = (By.CLASS_NAME, ".variationNameUpdateCancel")
    # on Maven design page, when you rename variation check button
    MAVEN_CHECK_BUTTON = (By.CLASS_NAME, ".variationNameUpdateSubmit")
    # input warning message, for example, on Journey SMS page when we try to save empty title input
    JOURNEY_WARNING_MESSAGE = (By.CLASS_NAME, ".attributeList.animationHalf")
    # on Journey do list filter input
    JOURNEY_SEARCH_BAR = (By.XPATH, '//*[@placeholder="Filter by journey name"]')
    # tags list when we select template in created journey campaign and didn’t click Use this Template button
    SELECT_TEMPLATE_TAGS = (By.CLASS_NAME, ".tag.animationHalf")
    # on Journey do list how to click exactly needed campaign’s Statistics button if there is more than 1 campaigns in the list
    # We need to search campaign first with JOURNEY_SEARCH_BAR then click to JOURNEY_STATISTICS
    JOURNEY_STATISTICS = (By.CLASS_NAME, ".icon-stats")
    # on Message box design page remove variation cross icon
    MESSAGE_BOX_CROSS = (By.CLASS_NAME, ".variationDelete")
    # Change element buttons on Journey canvas page
    ARCHITECT_CHANGE_ELEMENT = (
        By.XPATH, './/*[@*="/assets/img/journey-builder/do-it-your-self/change-element-icon.svg"]')
    # Remove element buttons on Journey canvas page
    ARCHITECT_REMOVE_ELEMENT = (
        By.XPATH, './/*[@*="/assets/img/journey-builder/do-it-your-self/delete-element-icon.svg"]')
    # Alert toaster on any page of panel
    ALERT_BOX = (By.CLASS_NAME, ".messageAlertBoxIcon")
    # on Api and js (access area) free js body input
    API_AND_JS = (By.CSS_SELECTOR, '#js-settings-editor .CodeMirror')
