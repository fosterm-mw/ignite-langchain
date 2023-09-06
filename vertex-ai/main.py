from langchain.llms import VertexAI
from langchain import PromptTemplate, LLMChain
template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = VertexAI()

llm_chain = LLMChain(prompt=prompt, llm=llm)
llm_chain = LLMChain(prompt=prompt, llm=llm)
question = "What NHL team won the Stanley Cup in the year Liam Gallagher was born?"

output = llm_chain.run(question)
print("output is: ", output)

