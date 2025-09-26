# from dotenv import load_dotenv

# load_dotenv()
# import base64
# import streamlit as st
# import os
# import io
# from PIL import Image 
# import pdf2image
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# def get_gemini_response(input,pdf_cotent,prompt):
#     model=genai.GenerativeModel('gemini-2.0-flash-lite')
#     response=model.generate_content([input,pdf_content[0],prompt])
#     return response.text

# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         ## Convert the PDF to image
#         images=pdf2image.convert_from_bytes(uploaded_file.read())

#         first_page=images[0]

#         # Convert to bytes
#         img_byte_arr = io.BytesIO()
#         first_page.save(img_byte_arr, format='JPEG')
#         img_byte_arr = img_byte_arr.getvalue()

#         pdf_parts = [
#             {
#                 "mime_type": "image/jpeg",
#                 "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
#             }
#         ]
#         return pdf_parts
#     else:
#         raise FileNotFoundError("No file uploaded")

# ## Streamlit App

# st.set_page_config(page_title="ATS Resume EXpert")
# st.header("ATS Tracking System")
# input_text=st.text_area("Job Description: ",key="input")
# uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


# if uploaded_file is not None:
#     st.write("PDF Uploaded Successfully")


# submit1 = st.button("Tell Me About the Resume")

# #submit2 = st.button("How Can I Improvise my Skills")

# submit3 = st.button("Percentage match")

# input_prompt1 = """
#  You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
#   Please share your professional evaluation on whether the candidate's profile aligns with the role. 
#  Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
# """

# input_prompt3 = """
# You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
# your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
# the job description. First the output should come as percentage and then keywords missing and last final thoughts.
# """

# if submit1:
#     if uploaded_file is not None:
#         pdf_content=input_pdf_setup(uploaded_file)
#         response=get_gemini_response(input_prompt1,pdf_content,input_text)
#         st.subheader("The Repsonse is")
#         st.write(response)
#     else:
#         st.write("Please uplaod the resume")

# elif submit3:
#     if uploaded_file is not None:
#         pdf_content=input_pdf_setup(uploaded_file)
#         response=get_gemini_response(input_prompt3,pdf_content,input_text)
#         st.subheader("The Repsonse is")
#         st.write(response)
#     else:
#         st.write("Please uplaod the resume")



   




from dotenv import load_dotenv
load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Custom CSS for styling
def load_css():
    st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 0rem;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .title-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        text-align: center;
    }
    
    .main-title {
        color: white;
        font-size: 3rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        color: rgba(255, 255, 255, 0.8);
        font-size: 1.2rem;
        margin-bottom: 1rem;
    }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }
    
    .metric-card {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem 0;
    }
    
    .success-message {
        background: linear-gradient(45deg, #56ab2f, #a8e6cf);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
        font-weight: bold;
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        font-weight: bold;
        transition: all 0.3s ease;
        width: 100%;
        margin: 0.25rem 0;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    
    .sidebar .stSelectbox {
        background: rgba(0, 0,0 , 0.6);
        border-radius: 10px;
    }
    
    .response-container {
        background: rgba(0, 0, 0, 0.6);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        border-left: 5px solid #4ECDC4;
    }
    
    .stats-container {
        background: rgba(0, 0, 0, 0.6);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-2.0-flash-lite')
    response = model.generate_content([input_text, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert the PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]
        
        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Enhanced prompts
def get_prompts():
    return {
        "resume_analysis": """
        You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description.
        Please provide a comprehensive analysis including:
        1. Overall profile alignment with the role
        2. Key strengths of the candidate
        3. Areas for improvement
        4. Specific skills that match the job requirements
        5. Professional recommendation
        """,
        
        "percentage_match": """
        You are a skilled ATS (Applicant Tracking System) scanner with deep understanding of data science and ATS functionality.
        Evaluate the resume against the job description and provide:
        1. Match percentage (0-100%)
        2. Keywords found vs missing
        3. Critical skills assessment
        4. Recommendations for improvement
        5. Final ATS compatibility score
        """,
        
        "skills_improvement": """
        As a Career Development Specialist, analyze the resume and job description to provide:
        1. Skills gap analysis
        2. Specific skills to develop
        3. Learning path recommendations
        4. Industry trends to consider
        5. Actionable improvement suggestions
        """,
        
        "keyword_optimization": """
        As an ATS optimization expert, analyze the resume and suggest:
        1. Important keywords missing from resume
        2. Keyword density recommendations
        3. Industry-specific terms to include
        4. Action verbs to use
        5. Formatting suggestions for ATS compatibility
        """,
        
        "interview_preparation": """
        As an Interview Coach, based on the resume and job description, provide:
        1. Potential interview questions
        2. How to highlight relevant experience
        3. Stories/examples to prepare
        4. Questions to ask the interviewer
        5. Areas to research about the company/role
        """,
        
        "salary_insights": """
        As a Compensation Analyst, provide insights based on the role and candidate profile:
        1. Market salary range for this position
        2. Factors affecting compensation
        3. Negotiation points based on candidate's profile
        4. Benefits to consider
        5. Geographic salary variations
        """
    }

def main():
    # Page configuration
    st.set_page_config(
        page_title="AI-Powered ATS Resume Analyzer",
        page_icon="🎯",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Load custom CSS
    load_css()
    
    # Header section
    st.markdown("""
    <div class="title-container">
        <h1 class="main-title">🎯 AI-Powered ATS Resume Analyzer</h1>
        <p class="subtitle">Optimize your resume for Applicant Tracking Systems with AI insights</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 📊 Analysis Options")
        analysis_type = st.selectbox(
            "Choose Analysis Type:",
            ["Resume Overview", "ATS Match Score", "Skills Development", "Keyword Optimization", "Interview Prep", "Salary Insights"]
        )
        
        st.markdown("### 📈 Quick Stats")
        if 'analysis_count' not in st.session_state:
            st.session_state.analysis_count = 0
        
        st.markdown(f"""
        <div class="stats-container">
            <p style="color: white; margin: 0;"><strong>Analyses Performed:</strong> {st.session_state.analysis_count}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 💡 Pro Tips")
        tips = [
            "Use industry-specific keywords",
            "Include quantifiable achievements",
            "Tailor resume for each application",
            "Use standard section headings",
            "Save as PDF format"
        ]
        for tip in tips:
            st.markdown(f"• {tip}")
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown("### 📝 Job Description")
        input_text = st.text_area(
            "Paste the job description here:",
            key="input",
            height=200,
            placeholder="Enter the complete job description including requirements, responsibilities, and qualifications..."
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown("### 📄 Resume Upload")
        uploaded_file = st.file_uploader(
            "Upload your resume (PDF only):",
            type=["pdf"],
            help="Please ensure your resume is in PDF format for best results"
        )
        
        if uploaded_file is not None:
            st.markdown("""
            <div class="success-message">
                ✅ Resume uploaded successfully!
            </div>
            """, unsafe_allow_html=True)
            
            # Display file info
            st.info(f"📋 File: {uploaded_file.name} ({uploaded_file.size} bytes)")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Analysis buttons
    st.markdown("### 🔍 Choose Your Analysis")
    
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    
    with col1:
        submit1 = st.button("📋 Resume Analysis", key="btn1")
    with col2:
        submit2 = st.button("📊 ATS Match Score", key="btn2")
    with col3:
        submit3 = st.button("🚀 Skills Development", key="btn3")
    with col4:
        submit4 = st.button("🔑 Keyword Optimization", key="btn4")
    with col5:
        submit5 = st.button("💼 Interview Preparation", key="btn5")
    with col6:
        submit6 = st.button("💰 Salary Insights", key="btn6")
    
    # Get prompts
    prompts = get_prompts()
    
    # Analysis logic
    def perform_analysis(prompt_key, title, icon):
        if uploaded_file is not None and input_text.strip():
            with st.spinner(f"Analyzing your resume... {icon}"):
                try:
                    pdf_content = input_pdf_setup(uploaded_file)
                    response = get_gemini_response(prompts[prompt_key], pdf_content, input_text)
                    
                    st.markdown(f"""
                    <div class="response-container">
                        <h3>{icon} {title}</h3>
                        {response}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.session_state.analysis_count += 1
                    st.success("Analysis completed successfully!")
                    
                except Exception as e:
                    st.error(f"Error during analysis: {str(e)}")
        else:
            missing = []
            if not uploaded_file:
                missing.append("resume")
            if not input_text.strip():
                missing.append("job description")
            
            st.warning(f"Please provide: {', '.join(missing)}")
    
    # Handle button clicks
    if submit1:
        perform_analysis("resume_analysis", "Resume Analysis", "📋")
    elif submit2:
        perform_analysis("percentage_match", "ATS Match Score", "📊")
    elif submit3:
        perform_analysis("skills_improvement", "Skills Development Plan", "🚀")
    elif submit4:
        perform_analysis("keyword_optimization", "Keyword Optimization", "🔑")
    elif submit5:
        perform_analysis("interview_preparation", "Interview Preparation", "💼")
    elif submit6:
        perform_analysis("salary_insights", "Salary & Compensation Insights", "💰")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: rgba(255,255,255,0.7); padding: 2rem;">
        <p>🚀 Powered by AI | Built with Streamlit | Enhance your career prospects</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
