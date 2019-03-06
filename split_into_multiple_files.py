



# num_texts = 0
# with open("/media/data/rohola_data/cleaned_wiki.txt") as file_reader:
#     for line in file_reader:
#         if not line.rstrip():
#             num_texts +=1

num_texts = 3956334

chunk_size = num_texts//24

chunk_num = 0
num_texts = 0
with open("/media/data/rohola_data/cleaned_wiki.txt") as file_reader:
    for line in file_reader:
        if not line.rstrip():
            num_texts += 1
        chunk_num = num_texts//chunk_size
        with open("/media/data/rohola_data/chunk_"+str(chunk_num)+".txt", 'w') as file_writer:
            file_writer.write(line)