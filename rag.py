from langchain.document_loaders import GitLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma

def file_filter(file_path):
    return file_path.endswith('.mdx')

# document loader
loader = GitLoader(
    clone_url='https://github.com/langchain-ai/langchain',
    repo_path='./langchain',
    branch='master',
    file_filter=file_filter,
)
raw_docs = loader.load()
#print(len(raw_docs))

# document transformers
text_splitter = CharacterTextSplitter(chunk_size=10000, chunk_overlap=0)
docs = text_splitter.split_documents(raw_docs)
# print(len(docs))

# text embedding & vector store
embeddings = OpenAIEmbeddings()
query = "AWSのS3からデータを読み込むためのDocumentLoaderはありますか？"
vector = embeddings.embed_query(query)
# print(len(vector))
# print(vector)
db = Chroma.from_documents(docs, embeddings)

# Retrievers
retriever = db.as_retriever()
context_docs = retriever.get_relevant_documents(query)
print(f"len = {len(context_docs)}")
print(f"metadata = {context_docs[0].metadata}")
print(context_docs[0].page_content)