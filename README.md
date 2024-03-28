# Content moderation

## Description

This application is a text moderation analyzer that uses Google Cloud's Natural Language API and Translate API. 
It takes Finnish text as input and analyzes it for potential moderation issues, such as profanity, hate speech, or violence. 
The application then translates the text to English and displays the moderation results, including the confidence level for each category. 
This tool can be useful for content creators, moderators, and anyone who needs to ensure that their text content is appropriate for a specific audience or platform.

To use the app: 
- Enter Finnish text in the text area. 
- Click the "Analyze: Text moderation" button. This will trigger the anaysis process. 
- View the moderation results.

![image](https://raw.githubusercontent.com/sandra-calvo/content_moderation/main/screencaptures/image1.png)


## Natural Language API vs Generative AI

It is also possible to use generative AI to do content moderation. For example by prompting:

### Natural Language + Translation API:

**Strengths:**

- Established and reliable: Natural Language Processing techniques for content moderation are well-established and constantly improving. They offer reliable detection of harmful content.
- Granular control: You have more control over the moderation process. Translation APIs are also well-developed, allowing for accurate translation between many languages.
- Transparency: You can understand how the system identifies harmful content based on the categories and sentiment analysis.

**Weaknesses:**

- Accuracy for nuanced content: Natural Language Processing can struggle with sarcasm, cultural context, and other nuances. This can lead to misidentification.
- Translation limitations: Translation accuracy can be affected by slang, idiomatic expressions, and humor. This can lead to misinterpreted content during moderation.
- Reliance on predefined categories: The system can only detect harmful content based on the categories it's trained on. New forms of abuse may go undetected.

### Generative AI:

**Strengths:**

- Potential for adaptability: Generative AI has the potential to adapt to new forms of harmful content and nuanced language.
- Content creation possibilities: Generative AI could be used to create alternative content to replace harmful content, promoting a more positive online environment.

**Weaknesses:**

- Less established: Generative AI for content moderation is a developing field. Its accuracy and reliability are still under development.
- Potential for bias: Generative AI models can inherit biases from the data they are trained on. This could lead to unfair moderation decisions.
- Lack of transparency: It can be difficult to understand how generative AI models identify harmful content, making it challenging to explain moderation decisions.

Keep in mind that NLP and translation aim to be deterministic. This means they provide the same output for a given input every time. They function like a set of rules, analyzing content based on predefined parameters.
Contrast this with generative AI, which introduces randomness in the process. Generative models use statistical probabilities to create responses, leading to potential variations in output for the same input.

## Run the Application locally 

### Install requirements

```bash
pip install -r requirements.txt
```

### Google Cloud Credentials
To run your code locally, which utilizes Google Cloud's Natural Language API and Translation API, you'll need to set up project credentials. 
Here's a step-by-step guide:

**1 .Create a Google Cloud Project (if you don't have one already):**

Go to the Google Cloud Console: https://console.cloud.google.com and sign in to your Google account.

If you don't have a project, click on "Create project" and follow the on-screen instructions to name and create a new project.

**2. Enable the APIs:**

In the Cloud Console navigation menu, go to "APIs & Services" and then "Library".
- Search for and enable the following APIs:
- "Cloud Natural Language API"
- "Cloud Translation API"
- Enabling these APIs allows your project to access them.

**3. Create Service Account Credentials:**

In the Cloud Console navigation menu, go to "IAM & Admin" and then "Service Accounts".
- Click "Create Service Account" and give it a descriptive name (e.g., "TextModerationServiceAccount").
- Click "Create" and then on the three vertical dots next to the newly created service account.
- Select "Create key" and choose the JSON format for the key. This will download a file named something like "text-moderation-credentials.json" to your local machine.
- This downloaded JSON file contains your credentials. Keep it secure and avoid sharing it publicly.

**4. Update your code:**
In the code you provided, there's a line that sets the path to the credential file:

```python
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/YOUR_PATH/key.json"
```
Replace this path with the actual location of your downloaded JSON credentials file on your computer.

### Run the application

```bash
streamlit run app.py
```

## Important Note 
This is not an officially supported Google product. The code in this repository is for demonstrative purposes only.

This project is licensed under the Apache License 2.0.
