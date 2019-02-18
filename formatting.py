import json
import spacy
import re
from os import listdir
from os.path import isfile, join
from glob import glob
import os

dataset_dir = "/home/rohola/codes/bert/dataset/output_data/"

nlp = spacy.load("en")

for root, directories, filenames in os.walk(dataset_dir):
    for filename in filenames:

        with open("cleaned_wiki.txt", 'w') as file_writer:
            with open(os.path.join(root,filename)) as file_reader:
                for line in file_reader:
                    document = json.loads(line)
                    paragraphs = document["text"].split("\n\n")
                    paragraphs = [paragraph for paragraph in paragraphs if "[[File" not in paragraph
                                   and "[[Category" not in paragraph
                                   and paragraph]

                    paragraphs = [re.sub(r"\[\[(.*?)(\|(.*?))*\]\]", r"\1", paragraph) for paragraph in paragraphs]

                    document_text_cleaned = " ".join(paragraphs[1:])# the first item in the list is the title which should be removed
                    doc = nlp(document_text_cleaned)

                    for sent in doc.sents:
                        file_writer.write(sent.text+"\n")

                    print(paragraphs[0] + "done!")
                    file_writer.write("\n")

                break

