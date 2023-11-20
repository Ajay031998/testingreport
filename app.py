
from flask import Flask, render_template, request
import openai

# Set your OpenAI API key
openai.api_key = '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'

# Define a prompt
# prompt = "Translate the following English text to French: 'Hello, how are you?'"
prompt = '''Transform the following text to Reference Report. 
Reference Report : 
General health status is normal. No reported symptoms of acute illness.
Vital signs within normal ranges.
Allergies: None reported.
Immunizations up to date.
Recent laboratory tests (if any) fall within normal parameters.
No remarkable findings in the cardiovascular and respiratory system examination.
Gastrointestinal and neurological examinations show no abnormalities
Example:
Input Text: 45 year old male ; complains of intermittent chest pain and shortness of breath. BP reads 140/90 ; cholesterol levels are high ; Slight irregularities are noted in ECG. Cardiologist suggests stress test, Chest Xray and recommends dietary changes. 
Output Report : 45-year-old male presenting with intermittent chest pain and shortness of breath.\n
Vital signs: Blood pressure slightly elevated at 140/90.\n
Allergies: None reported.\n
Immunizations up to date.\n
Laboratory tests indicate high cholesterol levels. ECG shows slight irregularities.\n
No remarkable findings in the cardiovascular and respiratory system examination.\n
Gastrointestinal and neurological examinations show no abnormalities.\n
Cardiologist suggests a stress test, Chest Xray and recommends dietary changes.\n
Example:
Input Text: 52-year-old female; experiencing cough, fever, and difficulty breathing. BP reads 120/80; recent chest X-ray shows opacities consistent with COVID-19. Neurological exam reveals reduced reflexes and muscle weakness, suggestive of Guillain-Barré syndrome.Recommends COVID-19 treatment protocol and further neurological evaluation for Guillain-Barré syndrome. 
Output Report : 52-year-old female presenting with cough, fever, and difficulty breathing.\n
Vital signs: Blood pressure normal at 120/80.\n
Allergies: None reported.\n
Immunizations up to date.\n
Chest X-ray reveals opacities consistent with COVID-19 infection.\n
Neurological examination indicates reduced reflexes and muscle weakness, suggestive of Guillain-Barré syndrome.\n
Recommends COVID-19 treatment protocol and further neurological evaluation for Guillain-Barré syndrome.\n
'''


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    input_text = ""
    output_text = ""

    if request.method == 'POST':
        input_text = request.form.get('text_input', '')
        # Process the input text as needed (you can perform any operation here)
        
        prompt1 = prompt+'\nInput Text:'+input_text+'\nOutput Report:'
        # Request completion from GPT-3
        response = openai.Completion.create(
            engine="text-davinci-002",  # Choose the GPT-3 engine
            prompt=prompt1,
            max_tokens=110,  # Adjust as needed
            n=1  # Number of completions to generate
        )

        # Extract the generated text from the response
        output_text = response['choices'][0]['text']
        # print(output_text)

        # For demonstration, we'll just capitalize the input text
        # output_text = input_text.upper()

    return render_template('index.html', input_text=input_text, output_text=output_text)

if __name__ == '__main__':
    app.run(debug=True)
