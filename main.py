from website_scraper import get_plain, get_images
from extract_imgs import save_images
from get_user_input import get_user_input



if __name__ == '__main__':
    print("Welcome to the AutoTrader.ca image scraper")
    print("Enter the link to the AutoTrader.ca page you want to scrape ")
    stop = False
    while not stop:
        link = get_user_input("Link: (press 'enter' stop) ")
        if not link:
            stop = True
        else:
            print("Scraping...")
            content = get_plain(link)
            results = get_images(content)
            save_images(results, get_user_input("Enter prefix for images:"))
            print("Scraping complete. Images saved to /images directory")
