import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def get_llama_response(input_text, no_words, blog_style):
    try:
        llm = CTransformers(model="models\llama-2-7b-chat.ggmlv3.q8_0.bin", model_type='llama', config={'max_new_tokens': 256, 'temperature': 0.01})
        template = """Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words."""
        prompt = PromptTemplate(input_variables=["blog_style", "input_text", "no_words"], template=template)
        response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
        return response
    except Exception as e:
        return f"Error: {str(e)}"

st.set_page_config(page_title="Generate Blogs", page_icon='✍', layout='centered', initial_sidebar_state='collapsed')
st.header("Generate Blogs 📝")

input_text = st.text_input("Enter your Topic for the Blog")
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('Number of Words')

with col2:
    blog_style = st.selectbox('Writing the blog for', ('Researchers', 'Data Scientist', 'Common People'), index=0)


submit = st.button("Generate")

if submit:
    response = get_llama_response(input_text, no_words, blog_style)
    st.write(response)
st.empty()