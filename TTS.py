#!/usr/bin/env python
# coding: utf-8

# # QUESTION
# <br>Convert Text to Speech. Take words as input on digital devices and converts them into audio or speech with a button click/finger touch.

# ### 1. Install necessary python modules

# In[22]:


# pip install gTTS  


# In[21]:


# pip install pyttsx3 


# ### 2. Import necessary libraries

# In[9]:


# importing libraries

from gtts import gTTS
import streamlit as st
from PIL import Image 
import requests


# ### 3. Text to speech app using streamlit

# In[ ]:


st.title("Text To Speech (T.T.S) Web Application")
# url='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Google_Text_to_Speech_logo.svg/1200px-Google_Text_to_Speech_logo.svg.png'
# image = Image.open(requests.get(url, stream=True).raw)
exp= st.beta_expander("About")
# col1, col2,  = exp.beta_columns(2)
# col1.image(image,use_column_width=True)
exp.write("This web application was developed using google's [T.T.S engine](https://gtts.readthedocs.io/en/latest/) and [streamlit](https://docs.streamlit.io/en/stable/index.html) web application framework.")
exp.write(" The app uses T.T.S engine to convert text data to audio file and read the file from the system for playing it using streamlit widgets.")
exp.write(" This project was done as a part of Msc-Problem solving with python course.") 
exp.write("You can check out the work at [github](https://github.com/Aravind-krishnan-g/MSc-20-311-2102-python-project-TTS)")
txt=st.text_area("Enter the text to be converted into speech")
if(txt):
    if(st.button("Convert to speech")):
        try:
            t1 =gTTS(txt)  
            t1.save("file.mp3") 
            audio_file = open('file.mp3', 'rb')
            audio_bytes = audio_file.read()
            st.success('Done!')
            st.audio(audio_bytes, format='audio/mp3')
        except:
            st.error('Error occured. Please try a different text to convert!')

