import pyterrier as pt

from corpus import Corpus
from indexing.hit import Hit
from indexing.index import Indexer


class BM25Indexer(Indexer):
    corpus: Corpus
    index_file_path: str
    indexer = None
    threads: int = 1

    def __init__(self, corpus: Corpus, index_file_path: str):
        self.corpus = corpus
        self.index_file_path = index_file_path
        self.indexer = pt.IterDictIndexer(self.index_file_path, meta=["id"], fields=[
                                          "contents"], wmodel="BM25", threads=self.threads)

    def index(self):
        self.indexer.index(self.corpus, meta=["id"], fields=["contents"])

    def query(self, query: str) -> list[type[Hit]]:
        raw_results = pt.BatchRetrieve(
            self.indexer, metadata=["id"]).search(query)
        results = [0] * len(raw_results)
        for i in range(len(results)):
            results[i] = Hit(raw_results["id"][i], raw_results["score"][i])
        return results
