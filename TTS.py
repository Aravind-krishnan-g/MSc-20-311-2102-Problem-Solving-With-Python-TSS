#!/usr/bin/env python
# coding: utf-8

# # TEXT TO SPEECH (T.T.S)
# <br>Convert Text to Speech. Take words as input on digital devices and converts them into audio or speech with a button click/finger touch.

# In[ ]:


# pip install gTTS pyttsx3 


# ## IMPORTING LIBRARIES

# Documentation of these libraries: [gtts](https://gtts.readthedocs.io/en/latest/) and [streamlit](https://docs.streamlit.io/en/stable/index.html)

# In[1]:


from gtts import gTTS
import streamlit as st


# ## MAIN CODE

# In[2]:


class tts:
    
    # function containing web app framework
    def display(self):
        
        st.title("Text To Speech (T.T.S) Web Application") # setting title
        exp= st.beta_expander("About") # 'About' section contains details about the project
        exp.write("This web application was developed using google's [T.T.S engine](https://gtts.readthedocs.io/en/latest/) and [streamlit](https://docs.streamlit.io/en/stable/index.html) web application framework. The app uses T.T.S engine to convert text data to audio file and read the file from the system for playing it using streamlit widgets.")
        exp.write(" This project was done as a part of Msc-Problem solving with python course.") 
        exp.write("You can check out the work at [github](https://github.com/Aravind-krishnan-g/MSc-20-311-2102-python-project-TTS)")
        
        txt=st.text_area("Enter the text to be converted into speech") # entering text to convert 
        if(txt): # checking whether text was entered
            if(st.button("Convert to speech")): # condition for button press
                try:
                    t1 =gTTS(txt)   
                    t1.save("file.mp3") # saving audio file
                    audio_file = open('file.mp3', 'rb') 
                    audio_bytes = audio_file.read() # reading the audio
                    st.success('Done!') # showing message
                    st.audio(audio_bytes, format='audio/mp3') # widget to play audio
                except:
                    st.error('Error occured. Please try a different text to convert!') # display error if necessary


# ## DRIVER CODE

# In[3]:


class_object = tts() # creating object of class
class_object.display() # running web app

