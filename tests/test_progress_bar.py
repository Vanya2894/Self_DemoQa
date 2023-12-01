import time

from pages.page_progress_bar import Progress

def test_progressBar(browser):
    progress = Progress(browser)
    progress.visit()
    time.sleep(10)

    progress.startStopButton.click()

    while True:
        if progress.progressBar.get_dom_attribute('aria-valuenow') == '51':
            progress.startStopButton.click()
            break

    assert progress.progressBar.get_dom_attribute('aria-valuenow') == '51'




