import os
import pickle
import re


class InvertedIndex:
    def __init__(self, movies):
        self.movies = movies
        self.index = {}
        self.docmap = {}

    def __add_document(self, doc_id, text):
        tokens = re.findall(r"\w+", text.lower())
        for token in tokens:
            if token not in self.index:
                self.index[token] = set()
            self.index[token].add(doc_id)

    def get_documents(self, term):
        return sorted(self.index.get(term.lower(), set()))

    def build(self):
        for m in self.movies:
            doc_id = m["id"]
            self.docmap[doc_id] = m
            self.__add_document(doc_id, f"{m['title']} {m['description']}")

    def save(self):
        os.makedirs("cache", exist_ok=True)

        with open("cache/index.pkl", "wb") as f:
            pickle.dump(self.index, f)

        with open("cache/docmap.pkl", "wb") as f:
            pickle.dump(self.docmap, f)

    def functionality(self):
        print("This is some crazy function that does more then one thing.")