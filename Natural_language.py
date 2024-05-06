import streamlit as st
from transformers import pipeline
st.markdown("""
    # <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    """,unsafe_allow_html=True)
st.markdown('''
  <header class="navbar sticky-top bg-danger flex-md-nowrap p-0 shadow" data-bs-theme="dark">
  <a class="navbar-brand col-md-3 col-lg-2 me-0 px-3 fs-6 text-white" href="#">Deepak Rana</a>

  <ul class="navbar-nav flex-row d-md-none">
    <li class="nav-item text-nowrap">
      <button class="nav-link px-3 text-white" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSearch" aria-controls="navbarSearch" aria-expanded="false" aria-label="Toggle search">
        <svg class="bi"><use xlink:href="#search"></use></svg>
      </button>
    </li>
    <li class="nav-item text-nowrap">
      <button class="nav-link px-3 text-white" type="button" data-bs-toggle="offcanvas" data-bs-target="#sidebarMenu" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation">
        <svg class="bi"><use xlink:href="#list"></use></svg>
      </button>
    </li>
  </ul>

  <div id="navbarSearch" class="navbar-search w-100 collapse">
    <input class="form-control w-100 rounded-0 border-0" type="text" placeholder="Search" aria-label="Search">
  </div>
</header>''',unsafe_allow_html=True)
# import streamlit as st

def main():
    # st.title("Streamlit App with Slider Navigation")

    # Add a slider widget to select a project
    selected_project = st.sidebar.radio("Navigation", ["Sentiment Analysis", "Named Entity Recognition (NER)","Language Translation To French"])
    st.sidebar.write('Project 1: Sentiment-analysis Using Natural Language')
    st.sidebar.write('Project 2: Named Entity Recognition (NER)')
    st.sidebar.write('Project 3: Language Translation To French')
    # Display content based on the selected project
    if selected_project =="Sentiment Analysis" :
        st.write("Project 1: Sentiment-analysis Using Natural Language")
        # Load sentiment analysis pipeline
        sentiment_analysis_pipeline = pipeline("sentiment-analysis")

        # Streamlit app title and description
        st.title("Sentiment Analysis App")
        st.write("Enter some text below to analyze its sentiment.")

        # Text input for user
        text_input = st.text_area("Enter text:","This product is terrible. I regret buying it.")

        # Perform sentiment analysis when the user submits the text
        if st.button("Analyze"):
            if text_input.strip() == "":
                st.warning("Please enter some text.")
            else:
                # Perform sentiment analysis on the input text
                sentiment_result = sentiment_analysis_pipeline(text_input)[0]
                
                # Display the sentiment result
                st.write("Sentiment:", sentiment_result['label'])
                st.write("Confidence Score:", sentiment_result['score'])
                # Add content specific to Project 1

    elif selected_project =="Named Entity Recognition (NER)":
        st.write("Project 2: Named Entity Recognition (NER)")
        # Add content specific to Project 2
        st.title("Named Entity Recognition (NER)")

        # Load NER pipeline
        ner_pipeline = pipeline("ner")

        # Text input for NER
        text_input = st.text_area("Enter text:", "Apple Inc. is an American multinational technology company headquartered in Cupertino, California.")

        # Perform NER when the user submits the text
        if st.button("Perform NER"):
            ner_results = ner_pipeline(text_input)
            st.write(ner_results)
    elif selected_project =='Language Translation To French':
        st.write("Project 3: Description of Project 3 goes here...")
        # Add content specific to Project 3
        st.title("Language Translation To French")

        # Load Translation pipeline for English to Hindi
        translation_pipeline = pipeline("translation_en_to_fr")

        # Text input for translation
        english_text = st.text_area("Enter English text:", "The quick brown fox jumps over the lazy dog.")

        # Perform Translation when the user submits the text
        if st.button("Translate"):
            translation_result = translation_pipeline(english_text)
            st.write("Translated Text:", translation_result[0]['translation_text'])

if __name__ == "__main__":
    main()

#
st.subheader("Made BY Deepak Kumar")
