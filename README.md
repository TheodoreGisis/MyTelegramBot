# MyTelegramBot


## Description 
In this project, our goal is to create from scratch a Telegram bot that returns stock marker prices and useful information about the weather of some cities. Our bot is returning proper data for two Greek cities, Thessaloniki and Athens. Let's get deep on what is this data! First, bot is printing the temperature in Celsius for the city that you choose. The second data is the feel temperature, also in Celsius and the third is one little description of what is the weather (cloudy, rainy etc.) About the second action, the bot is capable to return the prices for a specific stock, that user decide, for the previous 5 minutes.

## Required Libraries
* math  
* JSON
* requests
* yfinance
* aiogram
* aiogram.types

## Create Bot
Open Telegram from your phone or your PC.

**Step 1.** Enter @Botfather in the search tab and decide this bot, and click start to activate Botfather.

**Step 2.** Select or type the /newbot command and send it.

**Step 3.** Select a name for your bot — your subscribers will see it in the conversation. And decide a username for your bot — the bot can be found by its username in searches. The username must be unique and end with the word “bot.”

**Step 4.** After you select a suitable name for your bot — the bot is created. You will receive a message with a link to your bot t.me/<bot_username>, recommendations to set up a profile picture, description, and a list of commands to manage your new bot.
To connect a bot to SendPulse you need a token. Copy your token value and find more information about connecting your bot to SendPulse in the last section of this article.

## Weather 

For weather information, we used openweathermap API. This API allows you to get the full historical weather data archive by any location on the globe. For more information about openweathermap you can search [here](https://en.wikipedia.org/wiki/OpenWeatherMap). Details about the API you can find in [documentations](https://openweathermap.org/api). 

https://user-images.githubusercontent.com/82917321/190393017-5ec6785a-d381-4909-b07b-8961746fee8c.mp4

## Stock

For stock market we use yfinance.Yfinance is a popular open source library developed by Ran Aroussi as a means to access the financial data available on Yahoo Finance.
Yahoo Finance offers an excellent range of market data on stocks, bonds, currencies and cryptocurrencies. It also offers market news, reports, and analysis and additionally options and fundamentals data-setting it apart from some of its competitors.

We used yfinance to collect the close price for a stock that user choose, for a period of 5 minutes. After downloading the data, we print the necessary information to the user.

More information you can find on yfinance's [documentations](https://python-yahoofinance.readthedocs.io/en/latest/api.html).


https://user-images.githubusercontent.com/82917321/190438859-2d58ef17-fe19-4a46-a3d4-8d081517a9e8.mp4
