from textblob import TextBlob
import streamlit as st


input_text = st.text_area('Type your text here: ')

def model(text=input_text):
    
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
    
    if subjectivity < 0.40:
        subjectivity_class = 'closer to objective'
    
    elif subjectivity > 0.90:
        subjectivity_class = 'closer to subjective'
        
    elif (subjectivity >= 0.25) & (subjectivity <= 0.75):
        subjectivity_class = 'hard to detect subjectivity'
        
    return {'polarity':polarity, 'polarity_class':polarity_class, 
            'subjectivity':subjectivity, 'subjectivity_class':subjectivity_class}


def output(results=results):
    
    comment_polarity = ''
    
    if results['polarity_class'] == 'negative':
        comment_polarity = 'There are sertain markers that your text has negative connotation. You can try using more neutral or positive words.'

    if results['polarity_class'] == 'positive':
        comment_polarity = 'There are sertain markers that your text has positive connotation. You can reduce this level by adding more neutral words.'

    if results['polarity_class'] == 'neutral':
        comment_polarity = 'There are sertain markers that your text has neutral connotation. You can change this level by adding negative or positive words.'
        
        return f"""
The analysis of polarity has shown that your text is {results['polarity_class']}.

The polarity score is {results['polarity']}. {comment_polarity}

the analysis of subjectivity has shown that your text is {results['subjectivity_class']}.

The subjectivity score is {results['subjectivity']}.
           """



results = model()
output_text = output()

st.write(output_text)