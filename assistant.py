import ollama

def chat():
    print("🤖 AI Assistant Started!")
    print("Type 'quit' to exit\n")
    
    conversation_history = []
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye!")
            break
            
        conversation_history.append({
            'role': 'user',
            'content': user_input
        })
        
        response = ollama.chat(
            model='llama3.2:3b',
            messages=conversation_history
        )
        
        assistant_message = response['message']['content']
        conversation_history.append({
            'role': 'assistant',
            'content': assistant_message
        })
        
        print(f"\nAssistant: {assistant_message}\n")

if __name__ == "__main__":
    chat()