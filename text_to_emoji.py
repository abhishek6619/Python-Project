import emoji

def text_to_emoji(sentence):
    words = sentence.split()
    emoji_dict = {
        "happy": "😊", "sad": "😢", "love": "❤️", "angry": "😡", "sun": "☀️",
        "heart": "💖", "star": "⭐", "fire": "🔥", "cool": "😎", "laugh": "😂",
        "cry": "😭", "dog": "🐶", "cat": "🐱", "pizza": "🍕", "coffee": "☕"
    }
    
    emoji_sentence = " ".join([emoji_dict.get(word.lower(), word) for word in words])
    return emoji_sentence

if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    print("Emoji Output:", text_to_emoji(user_input))
