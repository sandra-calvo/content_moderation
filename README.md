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

![image](https://raw.githubusercontent.com/sandra-calvo/product_descriptions_genai/main/screencaptures/image1.png)


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



## Important Note 
This is not an officially supported Google product. The code in this repository is for demonstrative purposes only.

This project is licensed under the Apache License 2.0.
