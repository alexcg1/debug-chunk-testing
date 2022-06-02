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

flow = Flow.load_config("flow.yml")

with flow:
    indexed_docs = flow.index(docs, show_progress=True)

for doc in indexed_docs:
    print(doc.text)
    for chunk in doc.chunks:
        print("\t", chunk.text)

with flow:
    results = flow.search(Document(text="wimble"))

    print(results)
    print(f"Matches returned: {len(results[0].matches)}")
    for match in results[0].matches:
        print(match.text)
