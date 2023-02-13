from textblob import TextBlob
import streamlit as st
st.set_page_config(page_title="Mood Master", page_icon=":grinning:")

st.title(":grinning: Mood Master App")
st.subheader("This app helps you identify emotional connotation of your text as well as its subjectivity. Enter your text in the area below and get the summary of the analysis")
st.caption('Please, write your text without quotes. The results summary will contain:')
st.caption('The polarity score of your text where **-1** is very negative and **1** is very positive')
st.caption('The subjectivity score where **0** is very objective and **1** is very subjective')

input_text = st.text_input('Enter your text here: ')


def model(text):
    
    analysis = TextBlob(text).sentiment
    polarity = round(analysis[0], 2)
    subjectivity = round(analysis[1], 2)
    
    polarity_class = ''
    subjectivity_class = ''
    
    if polarity < -0.5:
        polarity_class = 'negative'
    
    elif (polarity >= - 0.5) & (polarity <= 0.5):
        polarity_class = 'neutral'
        
    elif polarity > 0.5:
        polarity_class = 'positive'
    
    if subjectivity < 0.25:
        subjectivity_class = 'closer to objective'
    
    elif subjectivity > 0.75:
        subjectivity_class = 'closer to subjective'
        
    elif (subjectivity >= 0.25) & (subjectivity <= 0.75):
        subjectivity_class = 'hard to detect its subjectivity'
        
    return {'polarity':polarity, 'polarity_class':polarity_class, 
            'subjectivity':subjectivity, 'subjectivity_class':subjectivity_class}


model_results = model(input_text)


def output(results):
    
    comment_polarity = ''
    
    if results['polarity_class'] == 'negative':
        comment_polarity = 'There are sertain markers that your text has negative connotation. You can try using more neutral or positive words.'

    if results['polarity_class'] == 'positive':
        comment_polarity = 'There are sertain markers that your text has positive connotation. You can reduce this level by adding more neutral words.'

    if results['polarity_class'] == 'neutral':
        comment_polarity = 'There are sertain markers that your text has neutral connotation. You can change this level by adding negative or positive words.'
        
        return f"""
The analysis of polarity has shown that your text is {results['polarity_class']}.

The polarity score is {results['polarity']}. 
{comment_polarity}

The analysis of subjectivity has shown that your text is {results['subjectivity_class']}.

The subjectivity score is {results['subjectivity']}.
           """


if input_text:

    output_results = output(model_results)

    output_text = st.caption(output_results)