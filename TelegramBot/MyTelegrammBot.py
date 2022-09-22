import math
import json
import requests
import yfinance as yf
from aiogram import Bot, Dispatcher, executor, types 
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


#API Initialize
API_TELEGRAM=""

bot = Bot(token="")
dp = Dispatcher(bot)

#Creating buttons 
BTN_WEATHER = InlineKeyboardButton('Weather', callback_data='Weather')
BTN_STOCK = InlineKeyboardButton('Stock', callback_data='Stock')
BTN_CITY = InlineKeyboardButton("City",callback_data="city")
BTN_TEMPERATURE = InlineKeyboardButton("Temp",callback_data="temperature")
BTN_FEEL_TEMPERATURE = InlineKeyboardButton("Feel_Temp",callback_data="Feel_Temp")
BTN_DESCRIPTION = InlineKeyboardButton("Description",callback_data="Description")
BTN_CITY = InlineKeyboardButton("City",callback_data="City")
BTN_ATHENS = InlineKeyboardButton("Athens",callback_data="Athens")
BTN_THESSALONIKI = InlineKeyboardButton("Thessaloniki",callback_data="Thessaloniki")

#Keyboard inline creator
Keyboard_inline = InlineKeyboardMarkup().add(BTN_WEATHER,BTN_STOCK)
Keyboard_inline_number2 = InlineKeyboardMarkup().add(BTN_CITY)
Keyboard_inline_number3 = InlineKeyboardMarkup().add(BTN_ATHENS,BTN_THESSALONIKI)
Keyboard_inline_number4 = InlineKeyboardMarkup().add(BTN_TEMPERATURE,BTN_FEEL_TEMPERATURE,BTN_DESCRIPTION)


@dp.message_handler(commands=['help'])
async def show_help_menu(message:types.Message):
    await message.reply(help_menu(),reply_markup=Keyboard_inline)

#Print the first message tha user gone see when he starts bot
@dp.message_handler(commands=['start'])
async def show_weather(message: types.Message):
        await message.reply("Hi User!!\nWhat can i do for you?\n",reply_markup=Keyboard_inline)

#Inline button for "Weather"
@dp.callback_query_handler(text="Weather")
async def call_back_weather(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,text="Weather",reply_markup=Keyboard_inline_number2)

#Inline button for "City"
@dp.callback_query_handler(text="City")
async def call_back_city(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,text="Choose city",reply_markup=Keyboard_inline_number3)

#Inline button for "Athens"
@dp.callback_query_handler(text="Athens")
async def call_back_weather(callback_query: types.CallbackQuery):
    global text
    text = "Athens"
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,text="What information do you want?",reply_markup=Keyboard_inline_number4)

##Inline button that describes what is the weathes
@dp.callback_query_handler(text="Description")
async def call_back_discription(callback_query: types.CallbackQuery):
    global text
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,text=print_weather(text),reply_markup=Keyboard_inline_number2)

#Inline button for "Thessaloniki"
@dp.callback_query_handler(text="Thessaloniki")
async def call_back_weather(callback_query: types.CallbackQuery):
    global text
    text = "Thessaloniki"
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,text="What information do you want?",reply_markup=Keyboard_inline_number4)

#Inline button for "Feeling temperature"
@dp.callback_query_handler(text="Feel_Temp")
async def show_feel_temperature(callback_query: types.CallbackQuery):
   await bot.answer_callback_query(callback_query.id)
   await bot.send_message(callback_query.from_user.id,text="Feel Temp :"+ str(feels_like(text))+" C",reply_markup=Keyboard_inline_number2)

#Inline button for "Temperature"
@dp.callback_query_handler(text="temperature")
async def call_back_weather(callback_query: types.CallbackQuery):
    global text
    if not text:
        text = ""
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,text="Temp :"+str(print_temperature(text))+" C",reply_markup=Keyboard_inline_number2)


@dp.message_handler(commands=['temperature'])
async def show_weather(message: types.Message):
        await message.answer(text="Weather", reply_markup=Keyboard_inline)

def help_menu():
    message = ("ABOUT WEATHER:\n"
                "* /start ---->Bot starting/restart\n"
                "*City ----> Choose the city \n*Temp ----> Temperature of the city \n*Feel_Temp ---->Feel temperature of the city" 
                "\n*Description  ----> Details about the weather\n\n"
                "ABOUT STOCK:\n Type 'price' and the name of the stock")
    return message


#making request to "openweathermap" and return a json file with information about the weather 
def make_request(city):
    try:
        API_URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=f1e2b57287808b69594762b0f0fe4acf'.format(city.capitalize())
        request = requests.get(API_URL)
        final = request.json()       
        return json.dumps(final,indent=2)             
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

#Taking the feeling temperature value froma json 
def feels_like(city):
    feel  = json.loads(make_request(city))
    if "main" in feel:
        return  math.ceil((feel['main']['feels_like'] -273.15)*100)/100
      
#Taking the value of temperature from json and converted in to Celcius
def print_temperature(city):
    take_temperature = json.loads(make_request(city))
    if "main" in take_temperature:
       return  math.ceil((take_temperature['main']['temp'] -273.15)*100)/100

#Taking informations about the weather
def print_weather(city):
    take_weather = json.loads(make_request(city))
    if "weather" in take_weather:
        return take_weather["weather"][0]['description']


def stock_request(message):
    request =message.text.split()
    if len(request) < 2 or request[0].lower() not in "price":
        return False
    else:
        return True

@dp.message_handler(stock_request)
async def send_price(message):
    request = message.text.split()[1]
    data= yf.download(tickers=request, period='5m',interval='1m')
    if data.size>0:
        data=data.reset_index()
        data["format_date"] = data["Datetime"].dt.strftime('%m/%d %I: %M %p')
        data.set_index("format_date",inplace=True)
        print(data.to_string())
        await bot.send_message(message.chat.id , data['Close'].to_string(header=False))
    else:
        await bot.send_message(message.chat.id, "No data!")

@dp.callback_query_handler(text="Stock")
async def call_back_weather(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,text="Just print 'price' + 'your stock name'",reply_markup=Keyboard_inline)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
   

