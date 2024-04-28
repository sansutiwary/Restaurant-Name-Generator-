from langchain_community.llms import GooglePalm 
from langchain.prompts import PromptTemplate 
from langchain.chains import SequentialChain 
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import LLMChain 
API_KEY = "Your API KEY"
LLM = GoogleGenerativeAI(google_api_key=API_KEY, temperature=0.7 , model="gemini-pro")

def generateResturant(cuisine):


    promt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template= """I want to open a resturant for {cuisine} food . Suggest a fancy name for this. only one name """
    )

    name_chain = LLMChain(llm=LLM, prompt=promt_template_name , output_key='resturant_name')  # type: ignore

    promt_template_item = PromptTemplate(
        input_variables=['resturant_name'],
        template= """Suggest some menu item for resturant name {resturant_name}. return it comma separated only 10 item"""
    )

    item_name_chain = LLMChain(llm=LLM , prompt=promt_template_item , output_key='menu_item')    # type: ignore

    chain = SequentialChain(chains=[name_chain,item_name_chain] , input_variables=['cuisine'] , output_variables=['resturant_name' , 'menu_item'])
    response = chain({'cuisine':cuisine})
    return response



