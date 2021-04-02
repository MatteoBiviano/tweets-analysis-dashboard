import streamlit as st
from PIL import Image
from utility import *
import streamlit.components.v1 as components

def main():

	df_original = load_data("data/airline_sentiment.csv", encoding = 'unicode_escape')
	df_final = load_data("data/final_dataset.csv")

	st.sidebar.title("Menu")
	sentiment = st.sidebar.selectbox(
	    '',
	    ["Home", "Data Analysis", "Text Analysis"], index = 0)
	if(sentiment == "Data Analysis"):
		st.sidebar.subheader("Which data analysis do you want to explore?")
		data_analysis = st.sidebar.selectbox(
			'', 
			["1. Show random tweet by Sentiment",
			"2. Number of tweets by Sentiment",
			"3. Number of tweets by Airline",
			"4. Tweet Locations",
			"5. Negative reason by Airline",
			"6. Airline by Sentiment",
			"7. Negative reasons by DateTime"], index = 0)
		switch_data_analysis(data_analysis[0], df_original, st)

	elif(sentiment == "Text Analysis"):
		st.sidebar.subheader("Which text analysis do you want to explore?")
		text_analysis = st.sidebar.selectbox(
			'', 
			["1. Word count distribution",
			 "2. '@' count",
			 "3. Word Cloud by sentiment",
			 "4. Word Cloud by negative reason",
			 "5. Frequency count"], index = 0)
		switch_text_analysis(text_analysis[0], df_final, st)

	else:
		set_background(True, "Twitter US Airline Analysis")

if __name__ == '__main__':
    main()
