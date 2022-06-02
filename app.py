from jina import Flow
from docarray import Document, DocumentArray

docs = DocumentArray(
    [
        Document(
            text="foo",
            chunks=DocumentArray([Document(text="bar"), Document(text="baz")]),
        ),
        Document(
            text="thing",
            chunks=DocumentArray([Document(text="bar"), Document(text="baz")]),
        ),
        Document(
            text="plonk",
            chunks=DocumentArray([Document(text="bar"), Document(text="baz")]),
        ),
    ]
)

flow = Flow.load_config("flow-chunks.yml")

with flow:
    response = flow.index(docs, show_progress=True)

for doc in response:
    print(doc.text)
    for chunk in doc.chunks:
        print("\t", chunk.text)

with flow:
    results = flow.search(Document(text="wimble"))

    for match in results[0].matches:
        print(match.text)
