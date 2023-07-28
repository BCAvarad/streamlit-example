import openai
import streamlit as st
openai.api_key="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"

def BasicGeneration(userPrompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": userPrompt}]
    )
    return completion.choices[0].message.content


st.title("VS's Notes BOT-1.0")


sub=st.text_input("Enter The Subject Name:")

topic=st.text_input("Enter The Topic Name:")


if st.button("Get Note's"):
    with st.spinner("Making Note's..."):

        base_prompt=f"""
        i am BCA student and you are my mentor \
        i will provide you name of subject.so that you can help me in that particular subject.\
        name of subject: {sub}
        according to subject i will provide you topic from that particular subject\
        your task is to give information about that topic.\
        perform the following actions:
        1-summarize or overview the topic.
        2-simple and easy defination of topic.
        3-explain the working of topic in simple words.
        4-show the syntax and give some example of topic
        5-if need give other important information like types.if topic have types so also explain types as above format.
        use simple tone that is easy to understand.
        Separate your answers with line breaks.


                topic: {topic}
        """

    output_gpt=BasicGeneration(base_prompt)
#print(output_gpt)
     

    st.text_area("Note's", output_gpt,
                     height=500)
    st.success('Done!')
