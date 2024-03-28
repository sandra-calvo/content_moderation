# Copyright 2024 Sandra Calvo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import streamlit as st
import os
from google.cloud import language_v1
from google.cloud import translate_v2 as translate

# Your Google Cloud project ID (needed for both APIs)
project_id = "YOUR_PROJECT_ID" 

# Set your Google Cloud Platform project ID.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/YOUR_PATH/key.json"

def analyze_for_moderation(text, target_language="en"):
    # Translation step (if needed)
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target_language, source_language="fi")
    translated_text = result['translatedText']

    # Print the translation
    st.write(f"**Translated Text: {translated_text}**")

    # Text Moderation step
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=translated_text, type_=language_v1.Document.Type.PLAIN_TEXT)

    response = client.moderate_text(document=document)

    # Print the moderation results
    for category in response.moderation_categories:
        confidence_value = category.confidence * 100
        st.write(f"Category: {category.name} (Confidence: {confidence_value:.1f}%)") 
        st.progress(category.confidence)

# UI Elements
st.title("Finnish Text Moderation Analyzer")
user_input = st.text_area("Enter text in Finnish:", height=100)

if st.button("Analyze: Text Moderation"):
    # Call your analysis function
    analyze_for_moderation(user_input) 
