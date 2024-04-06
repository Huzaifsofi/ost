import os

cv_file = []
cv_doc_file = []
cv_pdf_file = []

def print_all_filenames(folder_path):
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return
    
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            cv_file.append(filename)
            print(filename)


def file_def(file_list):
    for files in file_list:
        if files.lower().endswith('.docx'):
            print(files)
            print('doc')
        elif files.lower().endswith('.pdf'):
            print(files)
            print('pdf')

folder_path = "Sample2"
print_all_filenames(folder_path)
print("change")
file_def(cv_file)