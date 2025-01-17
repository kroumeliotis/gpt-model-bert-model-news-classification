import sqlite3
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

# Create a csv with the results
def create_csv():
    conn = sqlite3.connect('datasets/database.db')
    query = "SELECT * FROM reviews WHERE ft_type_100='test'"
    data = pd.read_sql_query(query, conn)
    conn.close()
    data.to_csv('datasets/research-results.csv', index=False)

def evaluate_results(original, prediction):
    data = pd.read_csv('datasets/research-results.csv')
    accuracy = round(accuracy_score(data[original], data[prediction]), 4)
    precision = round(precision_score(data[original], data[prediction], average='weighted'), 4)
    recall = round(recall_score(data[original], data[prediction], average='weighted'), 4)
    f1 = round(f1_score(data[original], data[prediction], average='weighted'), 4)
    return {'Accuracy': accuracy, 'Precision': precision, 'Recall': recall, 'f1': f1}


def scatterplot(model):
    df = pd.read_csv('datasets/research-results.csv')
    prediction_model = df[model]
    review_rating = df['review_rating']
    plt.scatter(review_rating, prediction_model, alpha=0.5)
    plt.xlabel('review_rating')
    plt.ylabel(model)
    # plt.title('Comparison of LLM Predictions with the Actual Rating Given by the Reviewer')
    plt.show()

create_csv()
print(f'base:gpt-3.5-turbo-1106: ' + str(evaluate_results('review_rating', 'gpt')))
print(f'base:llama-2-70b-chat: ' + str(evaluate_results('review_rating', 'llama')))
print(f'ft:gpt-3.5-turbo-1106 (100%): ' + str(evaluate_results('review_rating', 'ft_gpt_100')))
print(f'ft:llama-2-70b-chat (100%): ' + str(evaluate_results('review_rating', 'ft_llama_100')))
print(f'ft:bert-adam (100%): ' + str(evaluate_results('review_rating', 'ft_bert_adam_100')))
print(f'ft:bert-adamw (100%): ' + str(evaluate_results('review_rating', 'ft_bert_adamw_100')))
print(f'ft:bert-sgd (100%): ' + str(evaluate_results('review_rating', 'ft_bert_sgd_100')))
print(f'ft:roberta-adam (100%): ' + str(evaluate_results('review_rating', 'ft_roberta_adam_100')))
print(f'ft:roberta-adamw (100%): ' + str(evaluate_results('review_rating', 'ft_roberta_adamw_100')))
print(f'ft:roberta-sgd (100%): ' + str(evaluate_results('review_rating', 'ft_roberta_sgd_100')))
print(f'ft:gpt-3.5-turbo-1106 (50%): ' + str(evaluate_results('review_rating', 'ft_gpt_50')))
print(f'ft:llama-2-70b-chat (50%): ' + str(evaluate_results('review_rating', 'ft_llama_50')))
print(f'ft:bert-adam (50%): ' + str(evaluate_results('review_rating', 'ft_bert_adam_50')))
print(f'ft:bert-adamw (50%): ' + str(evaluate_results('review_rating', 'ft_bert_adamw_50')))
print(f'ft:bert-sgd (50%): ' + str(evaluate_results('review_rating', 'ft_bert_sgd_50')))
print(f'ft:roberta-adam (50%): ' + str(evaluate_results('review_rating', 'ft_roberta_adam_50')))
print(f'ft:roberta-adamw (50%): ' + str(evaluate_results('review_rating', 'ft_roberta_adamw_50')))
print(f'ft:roberta-sgd (50%): ' + str(evaluate_results('review_rating', 'ft_roberta_sgd_50')))



# print('Base Model Predictions')
# print(f'llama-2-70b-chat: ' + str(evaluate_results('review_rating', 'llama')))
# print(f'gpt-3.5-turbo-1106: ' + str(evaluate_results('review_rating', 'gpt')))
# print('Predictions by Models Fine-Tuned on 50% of the Training Dataset')
# print(f'Llama 2 Fine-Tuned: ' + str(evaluate_results('review_rating', 'ft_llama_50')))
# print(f'GPT 3.5 Fine-Tuned: ' + str(evaluate_results('review_rating', 'ft_gpt_50')))
# print('Predictions by Models Fine-Tuned on 100% of the Training Dataset')
# print(f'Llama 2 Fine-Tuned: ' + str(evaluate_results('review_rating', 'ft_llama_100')))
# print(f'GPT 3.5 Fine-Tuned: ' + str(evaluate_results('review_rating', 'ft_gpt_100')))
