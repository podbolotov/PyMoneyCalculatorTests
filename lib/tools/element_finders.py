def find_by_locator(driver, locator):

    element = driver.find_element(
        by=locator.type,
        value=locator.value
    )

    return element
