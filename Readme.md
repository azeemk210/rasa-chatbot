# Rasa Community Chatbot 🤖

This is a Rasa-powered chatbot designed to answer questions about community members based on their region and personal details. The bot dynamically reads from a CSV file containing community member information and can provide:

- Check if there are members in a specific region.
- List members from a particular region.
- Provide contact details for specific members.

## 📂 Project Structure

```
├── data/
│   └── community_members.csv      # List of community members
├── actions/
│   └── actions.py                 # Custom actions for dynamic responses
├── domain.yml                     # Intents, entities, slots, responses, and actions
├── nlu.yml                        # Natural language understanding training data
├── stories.yml                    # Example conversations (stories)
├── rules.yml                      # Rules for specific chatbot behavior
├── config.yml                     # Configuration for the pipeline and policies
├── credentials.yml                # Credentials for external services
├── endpoints.yml                  # Configures custom actions
├── README.md                      # Project documentation
```

## 🚀 How to Run the Chatbot

### 1️⃣ Install Dependencies
Make sure you have Python 3.8+ and Rasa installed:

```bash
pip install rasa
```

### 2️⃣ Train the Model
Train the chatbot model with:

```bash
rasa train
```

### 3️⃣ Run Action Server (Custom Actions)
Start the custom action server:

```bash
rasa run actions
```

### 4️⃣ Run the Chatbot
In a new terminal, start the Rasa shell:

```bash
rasa shell
```

### 5️⃣ Test Example Queries
Try asking the bot:

- "Are there any members in Italy?"
- "Who are the members in Germany?"
- "Provide details for John Doe."

## 📊 Dataset Format
The `community_members.csv` file should have the following format:

```csv
Name,Tag,Region,Email,Phone
John Doe,Community,Italy,john.doe@example.com,1234567890
Jane Smith,Community,Germany,jane.smith@example.com,2345678901
```

## 🛠️ Custom Actions
Custom actions are defined in `actions/actions.py`. These include:

- `action_check_region_members`: Check if members exist in a specific region.
- `action_list_members`: List members from a region.
- `action_provide_member_details`: Provide detailed contact information.

## 🔗 Useful Commands
- Train the model: `rasa train`
- Start the action server: `rasa run actions`
- Launch interactive shell: `rasa shell`
- Test endpoints: `curl http://localhost:5055/webhook`

## 🤝 Contributing
Feel free to fork this repository and submit pull requests. If you find a bug or need help, open an issue.

## 📄 License
This project is licensed under the MIT License.

---

Made with ❤️ using [Rasa](https://rasa.com/)
