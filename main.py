# Importing the required libraries

import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.supremenewyork.com/shop")
soup = BeautifulSoup(page.content, 'html.parser')

# Creating lists to store data
url_list = []
titles_list = []
price_list = []
image_url_list = []
color_list = []
button_list = []
sizes_list = []

# Creating a function to collect data from individual item
def get_other_details(link):
    page2 = requests.get(link)
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    main_div = soup2.find(id = 'wrap')
    inner_div = main_div.find(id = 'container')
    details = inner_div.find(id = 'details')
    
    if(details != None):
        #To get the title
        title = details.find('h1')
        titles_list.append(str(title)[str(title).find('>')+1 : -5])
        
        #To get the price
        price = details.find(class_ = 'price')
        price_list.append(str(price)[str(price).find('¥')+1 : str(price).find('</')])
    
        #To get the image urls
        styles = details.find(class_ = 'styles')
        styles_images = styles.find_all('a')
        str_styles_images = str(styles_images)
    
        images_array = []
        start_image = [i for i in range(len(str_styles_images)) if str_styles_images.startswith('src=', i)]
        end_image = [i for i in range(len(str_styles_images)) if str_styles_images.startswith('.jpg" ', i)]
        if(len(start_image) == len(end_image)):
            for i in range(len(start_image)):
                images_array.append('https:' + str_styles_images[start_image[i]+5 : end_image[i]+4])
            image_url_list.append(images_array)
        else:
            image_url_list.append('Null')
    
        #To get colors
        colors_array_with_duplicates = []
        colors_array_without_duplicates = []
        start_color = [i for i in range(len(str_styles_images)) if str_styles_images.startswith('data-style-name="', i)]
    
    
        #print(start_color)
        for i in range(len(start_color)):
            colors_array_with_duplicates.append(str_styles_images[start_color[i]+17 : start_color[i]+22])
        for j in range(len(colors_array_with_duplicates)):
            if (colors_array_with_duplicates[j] in colors_array_without_duplicates):
                pass
            else:
                colors_array_without_duplicates.append(colors_array_with_duplicates[j])
        color_list.append(colors_array_without_duplicates)
    
    
        #To get add to cart button
        if(str_styles_images[str_styles_images.find('data-sold-out="')+15] == 't'):
            button_list.append('Absent')
        else:
            button_list.append('Present')
        
        #To get sizes
        sizes_array=[]
        if(str_styles_images[str_styles_images.find('data-sold-out="')+15] == 't'):
            sizes_list.append('Null')
        else:
            sizes_data = details.find(id = 'cctrl')
            size = sizes_data.find(id='size')
            options = str(size.find_all('option'))
            start_size = [i for i in range(len(options)) if options.startswith('<option value="', i)]
            end_size = [i for i in range(len(options)) if options.startswith('</option>', i)]
            for i in range(len(start_size)):
                sizes_array.append(options[start_size[i]+22 : end_size[i]])
            sizes_list.append(sizes_array)

    # If data is missing on the website
    else:
        titles_list.append('Null')
        price_list.append('Null')
        image_url_list.append('Null')
        color_list.append('Null')
        button_list.append('Null')
        sizes_list.append('Null')

# Creating class scraping
class scraping :
    # To get product urls        
    def get_url():
        all_items = soup.find(id = 'wrap')
        wrap = soup.find(id = 'wrap')
        shop = wrap.find_all(class_ = 'shop')
        shop_scroller_container = shop[0].find(id='shop-scroller-container')
        shop_scroller = shop_scroller_container.find(id = 'shop-scroller')
        
        jackets = shop_scroller.find_all(class_ = 'jackets') 
        for i in range(9):
            x = jackets[i].find('a')
            url_list.append('http://www.supremenewyork.com' + str(x)[9:32])
            get_other_details('http://www.supremenewyork.com' + str(x)[9:32])
        
        
        
        
        shirts = shop_scroller.find_all(class_ = 'shirts')
        for i in range(2):
            x = shirts[i].find('a')
            url_list.append('http://www.supremenewyork.com' + str(x)[9:31])
            get_other_details('http://www.supremenewyork.com' + str(x)[9:31])
            
            
        
        hats = shop_scroller.find_all(class_ = 'hats')
        for i in range(12):
            x = hats[i].find('a')
            url_list.append('http://www.supremenewyork.com' + str(x)[9:29])
            get_other_details('http://www.supremenewyork.com' + str(x)[9:29])
            
        
        sweatshirts = shop_scroller.find_all(class_ = 'sweatshirts')
        for i in range(7):
            x = sweatshirts[i].find('a')
            url_list.append('http://www.supremenewyork.com' + str(x)[9:36])
            get_other_details('http://www.supremenewyork.com' + str(x)[9:36])

        
        tops_sweaters = shop_scroller.find_all(class_ = 'tops/sweaters')
        for i in range(7):
            x = tops_sweaters[i].find('a')
            url_list.append('http://www.supremenewyork.com' + str(x)[9:38])
            get_other_details('http://www.supremenewyork.com' + str(x)[9:38])
            
            
        pants = shop_scroller.find_all(class_ = 'pants')
        for i in range(9):
            x = pants[i].find('a')
            url_list.append('http://www.supremenewyork.com' + str(x)[9:30])
            get_other_details('http://www.supremenewyork.com' + str(x)[9:30])

        
        bags = shop_scroller.find_all(class_ = 'bags')
        for i in range(9):
            x = bags[i].find('a')
            url_list.append('http://www.supremenewyork.com' + str(x)[9:29])
            get_other_details('http://www.supremenewyork.com' + str(x)[9:29])

        
        shoes = shop_scroller.find_all(class_ = 'shoes')
        for i in range(2):
            x = shoes[i].find('a')
            url_list.append('http://www.supremenewyork.com' + str(x)[9:30])
            get_other_details('http://www.supremenewyork.com' + str(x)[9:30])

        
        skate = shop_scroller.find_all(class_ = 'skate')
        for i in range(4):
            x = skate[i].find('a')
            url_list.append('http://www.supremenewyork.com' + str(x)[9:29])
            get_other_details('http://www.supremenewyork.com' + str(x)[9:29])

        
        accessories = shop_scroller.find_all(class_ = 'accessories')
        for i in range(15):
            x = accessories[i].find('a')
            url_list.append('http://www.supremenewyork.com' + str(x)[9:36])
            get_other_details('http://www.supremenewyork.com' + str(x)[9:36])
        

# Calling the function to start scraping
scraping.get_url()

# Storing the data into csv file
final_scraped_data = pd.DataFrame({'Title':titles_list,'Product_Url':url_list,'Price':price_list,'Colors':color_list,'Sizes':sizes_list,'All image url':image_url_list,'Add to cart button':button_list})
final_scraped_data.to_csv('scraped_final.csv')


# To send notification to discord-
token = "OTEzNDkxNTY2NjMzNTc0NDcy.YZ_RjQ.8kP65jUJ_i6psDa8OqCY3iQt3Tc"
def send_message(message):
    url = 'https://discord.com/api/v9/channels/913492086672748577/messages'
    data = {
        'content' : message
    }
    header = {
        'authorization' : token
    }

    requests.post(url, data=data, headers=header)

for i in range(len(url_list)):
    message_data = {
        '\n\n{}\n\n{}\n\nPrice\n{}\n\nSizes\n{}'.format(url_list[i],titles_list[i],price_list[i],sizes_list[i]),
    }
    send_message(message_data)

