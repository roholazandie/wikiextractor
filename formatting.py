import json
import spacy
import re
from os import listdir
from os.path import isfile, join
from glob import glob
import os

dataset_dir = "/home/rohola/codes/bert/dataset/output_data/"
result = [x for x in os.walk(dataset_dir)]
print(result)
#dataset_dir = "/home/rohola/codes/bert/dataset/output_data/"
#onlyfiles = [f for f in listdir(dataset_dir) if isfile(join(dataset_dir, f))]
#print(onlyfiles)

# nlp = spacy.load("en")
#
# with open("cleaned_wiki.txt", 'w') as file_writer:
#     with open("wiki_00") as file_reader:
#         for line in file_reader:
#             document = json.loads(line)
#             paragraphs = document["text"].split("\n\n")
#             paragraphs = [paragraph for paragraph in paragraphs if "[[File" not in paragraph
#                            and "[[Category" not in paragraph
#                            and paragraph]
#
#             paragraphs = [re.sub(r"\[\[(.*?)(\|(.*?))*\]\]", r"\1", paragraph) for paragraph in paragraphs]
#
#             document_text_cleaned = " ".join(paragraphs[1:])# the first item in the list is the title which should be removed
#             doc = nlp(document_text_cleaned)
#
#             for sent in doc.sents:
#                 file_writer.write(sent.text+"\n")
#
#         file_writer.write("\n")
#
