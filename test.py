import google.generativeai as genai
genai.configure(api_key="AIzaSyBYnQi_0ARDIrlIaGw--ETJ6MgpSQgUXDE")

models = genai.list_models()
for m in models:
    print(m.name, m.supported_generation_methods)
