import streamlit as st
from multipage import MultiPage
import pages

# App layout settings
st.set_page_config(page_title='Apothemata',\
                    page_icon='chart_with_upwards_trend',\
                    layout='wide',\
                    initial_sidebar_state='auto')

# Create an instance of the app 
app = MultiPage()
home = pages.home(title = 'Home')
checkStock = pages.checkStock(title = 'Check your stocks')
trade = pages.trade(title = 'Trade')

# Add all your application here
app.add_page(home)
app.add_page(checkStock)
app.add_page(trade)

# The main app
app.run()

# Features:
# Highest moving stock
# Source code link to git
# Popular stocks
# Dowload dataset
# if not correct ticker give message
# little live-data game
# learn css/html to put all css markdowns in context
# improve search engine
# get common stocks json file to search in it


# YOLO trade page:
# How risky you are? - I have diadomnd hands, Lets go to the MOON
# show timeline and buy/sell popups, position, P/L
# YOLO Backtest 
# YOLO start strading: Trading suggestions

# 1. Fix Downlkoad_vade lixicon
# 2. Fix samsung - cannot find it
# 3. Show company names which are boouht/sold, as tickers are weird A, AA,UK?
# 4. when changing data source in checkStocks should not hit cache load data!