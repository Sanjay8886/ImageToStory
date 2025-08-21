# Image to Audio Story Converter

## **Introduction**
This project allows you to **turn images into audio stories**. It employs **image-to-text conversion**, **language models**, and **text-to-speech synthesis** to create an engaging experience. Users can **upload an image**, extract text from it, **generate a short story** based on the extracted text, and **listen to the generated story as an audio clip**.

---

## **Setup**

1. **Clone the Repository**:
```sh
git clone https://github.com/Sanjay8886/ImageToStory.git
cd ImageToStory
```
2. **Create Virtual Environment**:
   ```sh
   python -m venv venv
   ```
3. **Activate Virtual Environment**:
   ```sh
   venv\Scripts\activate
   ```

4. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the project directory and add your Hugging Face API token:
   ```
   HUGGINGFACEHUB_API_TOKEN=your_token_here
   ```

## Usage
1. **Run the Streamlit App**:
   ```sh
   streamlit run app.py
   ```

2. **Upload an Image**:
   - Use the interface to upload an image.
   - The app will process the image, extract text, and generate a story.

3. **Experience the Story**:
   - View the extracted scenario and the generated story in expandable sections.
   - Listen to the generated story as an audio clip.
