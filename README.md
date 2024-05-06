
**The application allows users to select from three different projects:**

**Sentiment Analysis:** Users can input text, and the application analyzes its sentiment using a pre-trained sentiment analysis pipeline from the Transformers library. It displays the sentiment label (e.g., positive, negative) and the confidence score.
![Screenshot 2024-05-06 170228](https://github.com/depak-kumar/Semantic_NLP_wwbapp/assets/129481998/34a1afef-bc70-457c-9d41-9499aed70b0c)


**Named Entity Recognition (NER):** Users can input text, and the application identifies named entities such as organizations, persons, and locations using a pre-trained NER pipeline. It displays the identified entities and their corresponding labels.
![Screenshot 2024-05-06 170300](https://github.com/depak-kumar/Semantic_NLP_wwbapp/assets/129481998/f1fe0318-d676-4e9a-abd2-3cdfc9b90738)

**Language Translation To French:** Users can input English text, and the application translates it into French using a pre-trained translation pipeline. It displays the translated text.
The application features a responsive user interface with navigation options on the sidebar for selecting different projects. Each project section includes a text input area and a button for executing the corresponding NLP task. Results are displayed dynamically below the input areas.
![Screenshot 2024-05-06 170354](https://github.com/depak-kumar/Semantic_NLP_wwbapp/assets/129481998/729c4066-e787-4c83-922f-7aae132ab49a)
**Project 1: Sentiment Analysis**

**Flow:**
Users input text into a text area provided by the application.
Upon clicking the "Analyze" button, the application triggers a sentiment analysis process using a pre-trained pipeline from the Hugging Face Transformers library.
The sentiment analysis model analyzes the input text and predicts its sentiment label (e.g., positive, negative) along with a confidence score.
The sentiment label and confidence score are displayed to the user.
**Role of AI:**
Sentiment analysis utilizes AI techniques to automatically determine the sentiment expressed in a piece of text.
The AI model trained on sentiment analysis data learns to classify text into different sentiment categories, such as positive, negative, or neutral, based on patterns in the text.
The role of AI in this project is to process and analyze textual data to extract sentiment-related information, providing valuable insights into the sentiment expressed by users.

**Project 2: Named Entity Recognition (NER)**

**Flow:**
Users input text into a text area provided by the application.
Upon clicking the "Perform NER" button, the application triggers a named entity recognition process using a pre-trained NER pipeline from the Hugging Face Transformers library.
The NER model analyzes the input text and identifies named entities such as organizations, persons, and locations.
The identified entities and their corresponding labels are displayed to the user.
Role of AI:
Named Entity Recognition (NER) involves the identification and classification of named entities within text.
AI models trained on NER tasks learn to recognize and categorize entities such as people, organizations, locations, dates, and more.
The role of AI in this project is to automatically process text and extract named entities, providing valuable information about specific entities mentioned in the text.

**Project 3: Language Translation To French**

**Flow:**
Users input English text into a text area provided by the application.
Upon clicking the "Translate" button, the application triggers a language translation process using a pre-trained translation pipeline from the Hugging Face Transformers library.
The translation model translates the input English text into French.
The translated text is displayed to the user.
**Role of AI:**
Language translation involves converting text from one language to another while preserving its meaning and context.
AI models trained on translation tasks learn to understand the structure and semantics of languages and generate translations that accurately convey the original meaning.
The role of AI in this project is to automatically translate English text into French, enabling users to communicate effectively across language barriers.
