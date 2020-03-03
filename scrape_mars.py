from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import datetime as dt



def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def NasaMarsNews(browser):
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    mars_soup = BeautifulSoup(html, "html.parser")

    try:
        slide_element = mars_soup.select_one("ul.item_list li.slide")
        slide_element.find("div", class_="content_title")
        latest_title = slide_element.find("div", class_="content_title").get_text()

        latest_paragragh = slide_element.find("div", class_="article_teaser_body").get_text()
    return latest_title, latest_paragragh


def Mars_Space_Images(browser):
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    mars_image = browser.find_by_id("full_image")
    mars_image.click()

    browser.is_element_present_by_text("more info", wait_time=1)
    more_info_image = browser.find_link_by_partial_text("more info")
    more_info_image.click()

    html = browser.html
    image_w_soup = BeautifulSoup(html, "html.parser")
    try:
        image_url = image_w_soup.select_one("img").get("src")
        image_url2 = f"https://www.jpl.nasa.gov{image_url}"

    return image_url, image_url2

    