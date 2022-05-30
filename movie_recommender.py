#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


# Main Function for scraping
def web_scraping(emotion, category):  
    
    # IMDB urls for specific categories
    if(emotion == "Positive"):
        if(category == "Romance"):
            urlhere = 'http://www.imdb.com/search/title?genres=romance&title_type=feature&sort=moviemeter, asc'
        elif(category == "Family"):
            urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
        elif(category == "Fantasy"):
            urlhere = 'http://www.imdb.com/search/title?genres=fantasy&title_type=feature&sort=moviemeter, asc'
        
    elif(emotion == "Negative"):
        if(category == "Animation"):
            urlhere = 'http://www.imdb.com/search/title?genres=animation&title_type=feature&sort=moviemeter, asc'
        elif(category == "Comedy"):
            urlhere = 'http://www.imdb.com/search/title?genres=comedy&title_type=feature&sort=moviemeter, asc'
        elif(category == "Drama"):
            urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'

    elif(emotion == "Neutral"):
        if(category == "Thriller"):
            urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
        elif(category == "Mystery"):
            urlhere = 'http://www.imdb.com/search/title?genres=mystery&title_type=feature&sort=moviemeter, asc'
        elif(category == "Horror"):
            urlhere = 'http://www.imdb.com/search/title?genres=horror&title_type=feature&sort=moviemeter, asc'
    
    # HTTP request to get the data of
    # the whole page
    response = requests.get(urlhere)
     # Parsing the data using
    # BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    movie_name = []
    year = []
    time = []
    rating = []
    
    # Extracting movie data from the HTML script
    movie_data = soup.findAll('div', attrs= {'class': 'lister-item mode-advanced'})
    
    for store in movie_data:
        name = store.h3.a.text
        movie_name.append(name)
        
        year_of_release = store.h3.find('span', class_ = 'lister-item-year text-muted unbold').text.replace('(', '').replace(')', '')
        year.append(year_of_release)
        
        runtime = store.p.find('span', class_ = 'runtime')
        time.append(runtime)
        
        rate = store.find('strong')
        rating.append(rate)
        
    movie_df = pd.DataFrame({'Movie Name': movie_name, 'Year of Release': year, 'Watchtime': time, 'Movie Rating': rating})

    return movie_df


# In[5]:


def movie_recomm(emotion):

    if emotion == 'Positive':
        print("Categories under this emotion are: Romance, Family and Fantasy")
        category = input("Enter one category: ")
        print("*********************************************")
        print()
        movie_lst = web_scraping(emotion, category)
        print(movie_lst.head(3))
        
        for i in range(0,len(movie_lst),3):
            print("\n--------------------------------------------------------------------------------")
            watched = int(input("Press 1 if you have watched these movies and 2 if not "))
            print("--------------------------------------------------------------------------------")
            
            if watched == 1:
                i+=3
                print(movie_lst.iloc[i:i+3, :])
            else:
                print("\nThanks for trying our recommender system!")
                break
        
    elif emotion == 'Negative':
        print("Categories under this emotion are: Animation, Comedy, Drama")
        category = input("Enter one category: ")
        print("*********************************************")
        print()
        movie_lst = web_scraping(emotion, category)
        print(movie_lst.head(3))
        
        for i in range(0,len(movie_lst),3):
            print("\n--------------------------------------------------------------------------------")
            watched = int(input("Press 1 if you have watched these movies and 2 if not "))
            print("--------------------------------------------------------------------------------")
            
            if watched == 1:
                i+=3
                print(movie_lst.iloc[i:i+3, :])
            else:
                print("\nThanks for trying our recommender system!")
                break
        
    elif emotion == 'Neutral':
        print("Categories under this emotion are: Thriller, Mystery, Horror")
        category = input("Enter one category: ")
        print("*********************************************")
        print()
        movie_lst = web_scraping(emotion, category)
        print(movie_lst.head(3))
        
        for i in range(0,len(movie_lst),3):
            print("\n--------------------------------------------------------------------------------")
            watched = int(input("Press 1 if you have watched these movies and 2 if not "))
            print("--------------------------------------------------------------------------------")
            
            if watched == 1:
                i+=3
                print(movie_lst.iloc[i:i+3, :])
            else:
                print("\nThanks for trying our recommender system!")
                break





