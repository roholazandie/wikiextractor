import json
import spacy
import re
from os import listdir
from os.path import isfile, join
from glob import glob
import os

dataset_dir = "/home/rohola/codes/bert/dataset/output_data/"

nlp = spacy.load("en")
min_acceptable_sentence = 10
min_sentences_per_doc = 3

for root, directories, filenames in os.walk(dataset_dir):
    for filename in filenames:

        with open("cleaned_wiki.txt", 'w') as file_writer:
            with open(os.path.join(root,filename)) as file_reader:
                for line in file_reader:
                    has_any_sentence = False
                    document = json.loads(line)
                    paragraphs = document["text"].split("\n\n")
                    paragraphs = [paragraph.rstrip() for paragraph in paragraphs if "[[File" not in paragraph
                                   and "[[Category" not in paragraph
                                   and len(paragraph)!=0]

                    paragraphs = [re.sub(r"\[\[(.*?)(\|(.*?))*\]\]", r"\1", paragraph) for paragraph in paragraphs]



                    document_text_cleaned = " ".join(paragraphs[1:])# the first item in the list is the title which should be removed
                    document_text_cleaned = document_text_cleaned.replace("[", "").replace("]", "")
                    doc = nlp(document_text_cleaned)
                    sentences = [sent.text for sent in doc.sents]
                    if len(sentences) > min_sentences_per_doc:#skip refer to entries
                        for sent in sentences:
                            if len(sent) > min_acceptable_sentence:
                                if sent.strip():
                                    file_writer.write(sent.rstrip()+"\n")
                                    has_any_sentence = True

                    print(paragraphs[0] + "done!")
                    if has_any_sentence:
                        file_writer.write("\n")
                    else:
                        print("This one doesnt have any sentence" + os.path.join(root,filename))

