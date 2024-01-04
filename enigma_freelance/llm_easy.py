import requests
from bs4 import BeautifulSoup
from transformers import DistilBertTokenizer, DistilBertForQuestionAnswering
import torch

url = "https://www.freelancer.com" + "/projects/research-writing/condense-rewrite-the-current-evident"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Find the div with class='PageProjectViewLogout-detail'
project_detail_div = soup.find('div', class_='PageProjectViewLogout-detail')

# Check if the div is found before proceeding
if project_detail_div:
    # Find all <p> elements within the project_detail_div
    paragraphs = project_detail_div.find_all('p')

    # Extract and process the text content from each <p> element
    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
    model = DistilBertForQuestionAnswering.from_pretrained('distilbert-base-uncased')

    is_easy_and_can_be_completed_by_python = True

    for paragraph in paragraphs:
        project_description = paragraph.text
        input_ids = torch.tensor(tokenizer.encode(project_description, "Can this project be completed easily and by Python?")).unsqueeze(0)  # Batch size 1
        start_scores, end_scores = model(input_ids)

        # Get the most likely beginning and end of the answer
        min_start_index, min_start_score = min((start_index, start_score) for start_index, start_score in enumerate(start_scores[0]))
        max_end_index, max_end_score = max((end_index, end_score) for end_index, end_score in enumerate(end_scores[0][min_start_index:]))

        answer_start = min_start_index + min_start_index
        answer_end = answer_start + (max_end_index - min_start_index)
        answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids.squeeze().tolist()[answer_start:answer_end + 1]))

        if "no" in answer.lower():
            is_easy_and_can_be_completed_by_python = False
            break

    print("Can the project be completed easily and by Python?", is_easy_and_can_be_completed_by_python)
else:
    print("Project detail div not found on the page.")
