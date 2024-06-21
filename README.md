# Webpage Content Analyzer

Have you ever found yourself lost in a sea of information, struggling to find specific details on a lengthy webpage? The Webpage Content Analyzer is here to help! 

This tool simplifies the process of extracting useful information from any webpage, allowing you to ask direct questions and receive precise answers.

## Problem Solved

Finding specific information on a webpage can be like looking for a needle in a haystack. This tool addresses that problem by:

1. **Summarizing Content**: Quickly get a summary of any webpage, saving you time and effort.
2. **Retrieving Specific Information**: Instantly find answers to specific questions without having to read through the entire page.
3. **Efficient Research**: Perfect for students, researchers, and professionals who need to extract relevant information quickly.

## Situations Where This Tool Can Save You

1. **Research Projects**: Easily gather specific information from multiple sources without manually reading through each one.
2. **Content Summarization**: Quickly get the gist of long articles, research papers, or news stories.
3. **Competitive Analysis**: Efficiently extract relevant data from competitor websites.
4. **Learning New Topics**: Ask questions about complex topics and get straightforward answers from detailed articles.
5. **Quick Information Retrieval**: Instantly find specific data points or answers to your queries on any webpage.

## Installation and Setup

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.11 or higher
- An OpenAI API key

### Step-by-Step Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Stevealila/any-webpage-analyzer.git
   cd any-webpage-analyzer
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the project root directory and [add your OpenAI API key](https://platform.openai.com/api-keys):

   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

### Running the Application Locally

1. **Run the Streamlit App**

   ```
   streamlit run app.py
   ```

2. **Open the Web Interface**

   Open your browser and navigate to `http://localhost:8501` to access the application.

## Usage

1. **Enter the Webpage URL**

   In the "Enter the webpage URL:" field, input the URL of the webpage you want to analyze.

2. **Enter Your Question**

   In the "Enter your question:" field, type the question you want to ask about the content of the webpage.

3. **Analyze**

   Click the "Analyze" button to start the analysis. The application will load the webpage content, process it, and provide an answer to your question.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [OpenAI](https://www.openai.com/) for the GPT-4 model.
- [LangChain](https://www.langchain.com/) for the document processing and retrieval frameworks.
- [Streamlit](https://www.streamlit.io/) for the web application framework.