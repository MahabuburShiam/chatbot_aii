import nltk
from nltk.corpus import stopwords
from collections import Counter
import string

nltk.download('stopwords')



def parse_chat_log(file_path):
    user_messages = []
    ai_messages = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith("User:"):
                user_messages.append(line[5:].strip())
            elif line.startswith("AI:"):
                ai_messages.append(line[3:].strip())

    return user_messages, ai_messages

def message_statistics(user_msgs, ai_msgs):
    total = len(user_msgs) + len(ai_msgs)
    return {
        "total": total,
        "user": len(user_msgs),
        "ai": len(ai_msgs)
    }


def extract_keywords(user_msgs, ai_msgs, top_n=5):
    stop_words = set(stopwords.words('english'))
    all_text = ' '.join(user_msgs + ai_msgs).lower()
    words = all_text.translate(str.maketrans('', '', string.punctuation)).split()
    filtered_words = [word for word in words if word not in stop_words]
    freq = Counter(filtered_words)
    return freq.most_common(top_n)


def generate_summary(stats, keywords):
    print("Summary:")
    print(f"- The conversation had {stats['total']} exchanges.")
    print(f"- User sent {stats['user']} messages, AI sent {stats['ai']}.")
    print("- Most common keywords:", ', '.join([word for word, _ in keywords]))



if __name__ == "__main__":
    file_path = r"E:\chatbot\ai-chat-log-summarizer\samples\chat.txt"
    user_msgs, ai_msgs = parse_chat_log(file_path)

    stats = message_statistics(user_msgs, ai_msgs)

    print("Summary:")
    print(f"- Total messages: {stats['total']}")
    print(f"- User messages: {stats['user']}")
    print(f"- AI messages: {stats['ai']}")
