import streamlit as st
import replicate
import os
from PIL import Image
import io
import requests
from pathlib import Path

# Load environment variables from .env file if it exists
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    st.warning("💡 Tip: Install python-dotenv for easier .env file support: `pip install python-dotenv`")

# Set page config
st.set_page_config(page_title="🐱 Cat Transformer", layout="wide", initial_sidebar_state="expanded")
st.title("🐱 Cat Transformer - Nano Banana AI")
st.subheader("Transform your cat photos with AI magic!")

# Check for API token
api_token = os.getenv("REPLICATE_API_TOKEN")
if not api_token:
    st.error("❌ REPLICATE_API_TOKEN not found!")
    st.info("""
    **Setup instructions:**
    
    1. Get your free API token from https://replicate.com
    2. Option A - Set environment variable:
       - macOS/Linux: `export REPLICATE_API_TOKEN=your_token_here`
       - Windows: `set REPLICATE_API_TOKEN=your_token_here`
    
    3. Option B - Create a `.env` file:
       - Copy `.env.example` to `.env`
       - Paste your token after the `=` sign
       - Install: `pip install python-dotenv`
    """)
    st.stop()

# Initialize Replicate client
os.environ["REPLICATE_API_TOKEN"] = api_token

# Sidebar for settings and info
with st.sidebar:
    st.header("⚙️ Settings & Info")
    
    st.subheader("📊 About Nano Banana")
    st.info(
        "**Model:** Google Nano Banana (Gemini 2.5 Flash Image)\n\n"
        "This AI model excels at:\n"
        "✨ Realistic transformations\n"
        "🎨 Style changes\n"
        "🌍 Scene preservation\n"
        "🎭 Character consistency"
    )
    
    st.divider()
    
    st.subheader("📈 Usage Tips")
    with st.expander("✍️ Writing Better Prompts", expanded=False):
        st.markdown("""
        **Do's:**
        - Be specific about style (watercolor, oil painting, cartoon)
        - Include mood and atmosphere
        - Mention lighting details
        - Use artistic references
        
        **Don'ts:**
        - Too vague descriptions
        - Conflicting instructions
        - Overly long prompts (keep it concise)
        """)
    
    st.divider()
    
    # Show API status
    if api_token:
        st.success("✅ API Token loaded successfully")
    
    # Link to resources
    st.markdown("""
    **Resources:**
    - [Replicate Docs](https://replicate.com/docs)
    - [Nano Banana Model](https://replicate.com/google/nano-banana)
    - [Get API Token](https://replicate.com/account/api-tokens)
    """)

# Main content area - two columns
col1, col2 = st.columns(2, gap="large")

with col1:
    st.header("📸 Step 1: Upload Cat Photo")
    uploaded_file = st.file_uploader(
        "Choose a cat image",
        type=["jpg", "jpeg", "png", "webp"],
        help="Upload a photo of your cat that you want to transform"
    )
    
    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Original cat photo", use_column_width=True)
        
        # Show image info
        st.caption(f"📐 Size: {image.size[0]}×{image.size[1]}px | 💾 {len(uploaded_file.getvalue())/1024:.1f}KB")

with col2:
    st.header("✨ Step 2: Describe the Transformation")
    
    # Transformation prompt
    prompt = st.text_area(
        "What do you want to do with the cat?",
        placeholder="Examples:\n- Make the cat look like a superhero\n- Transform the cat into a cartoon character\n- Make the cat look fancy in a royal outfit\n- Paint the cat in oil painting style\n- Make the cat look like it's in space",
        height=150,
        help="Be creative and descriptive! The more detailed, the better results."
    )
    
    # Preset prompts
    st.subheader("💡 Quick Ideas:")
    
    presets = {
        "🎨 Artistic": "Transform the cat into a beautiful watercolor painting style artwork",
        "🚀 Space": "Make the cat an astronaut in space with a helmet and stars around",
        "👑 Royal": "Make the cat look like royalty wearing a crown and royal outfit",
        "🦸 Hero": "Transform the cat into a superhero with a cape and mask",
        "🎭 Cartoon": "Turn the cat into a cute cartoon character with big expressive eyes",
        "🌈 Rainbow": "Make the cat multicolored and rainbow-like with magical effects",
    }
    
    cols = st.columns(3)
    for idx, (label, preset_prompt) in enumerate(presets.items()):
        with cols[idx % 3]:
            if st.button(label, use_container_width=True, key=f"preset_{idx}"):
                prompt = preset_prompt
                st.rerun()

# Process button section
st.divider()

col_process1, col_process2, col_process3 = st.columns([1, 2, 1])

with col_process2:
    process_button = st.button(
        "🚀 Transform the Cat!",
        use_container_width=True,
        type="primary",
        disabled=(uploaded_file is None or not prompt.strip())
    )

# Process the transformation
if process_button:
    if uploaded_file is None:
        st.error("❌ Please upload a cat photo first!")
    elif not prompt.strip():
        st.error("❌ Please describe what you want to do with the cat!")
    else:
        # Get image bytes
        image_bytes = uploaded_file.getvalue()
        
        with st.spinner("🎨 AI is transforming your cat... This may take a moment..."):
            try:
                import base64
                
                # Determine the image type
                if uploaded_file.type in ['image/jpeg', 'image/jpg']:
                    image_type = 'jpeg'
                elif uploaded_file.type == 'image/png':
                    image_type = 'png'
                elif uploaded_file.type == 'image/webp':
                    image_type = 'webp'
                else:
                    image_type = 'jpeg'  # default
                
                # Encode image to base64
                image_base64 = base64.b64encode(image_bytes).decode("utf-8")
                image_data_url = f"data:image/{image_type};base64,{image_base64}"
                
                # Run the model
                output = replicate.run(
                    "google/nano-banana",
                    input={
                        "prompt": prompt,
                        "image_input": [image_data_url]
                    }
                )
                
                # Display results
                st.success("✅ Transformation complete!")
                
                # Create two columns for before/after
                result_col1, result_col2 = st.columns(2)
                
                with result_col1:
                    st.subheader("Original")
                    st.image(image, use_column_width=True)
                
                with result_col2:
                    st.subheader("Transformed ✨")
                    
                    # Get the result URL
                    if hasattr(output, 'url'):
                        result_url = output.url()
                    else:
                        result_url = str(output)
                    
                    # Display the result
                    st.image(result_url, use_column_width=True)
                    
                    # Download button
                    try:
                        result_response = requests.get(result_url, stream=True, timeout=10)
                        if result_response.status_code == 200:
                            result_image = Image.open(io.BytesIO(result_response.content))
                            img_byte_arr = io.BytesIO()
                            result_image.save(img_byte_arr, format='PNG')
                            img_byte_arr.seek(0)
                            
                            st.download_button(
                                label="📥 Download Transformed Cat",
                                data=img_byte_arr,
                                file_name="transformed_cat.png",
                                mime="image/png",
                                use_container_width=True
                            )
                    except Exception as e:
                        st.info(f"💾 [Open result image]({result_url})")
                
                # Show the prompt used
                st.divider()
                st.subheader("📝 What we told the AI:")
                st.info(prompt)
                
            except Exception as e:
                error_msg = str(e)
                st.error(f"❌ Error during transformation: {error_msg}")
                
                st.warning("""
                **Common issues:**
                - Invalid API token (check REPLICATE_API_TOKEN)
                - Rate limit exceeded (wait a few minutes)
                - Large image file (try compressing it)
                - Internet connection issue
                
                **Try:**
                1. Verify your API token is correct
                2. Try a simpler prompt
                3. Use a smaller image file
                4. Wait a moment and try again
                """)

# Footer
st.divider()
col_foot1, col_foot2, col_foot3 = st.columns(3)

with col_foot1:
    st.markdown("""
    ### 🎓 How it works
    Uses **Google's Nano Banana** (Gemini 2.5 Flash Image) via Replicate API
    """)

with col_foot2:
    st.markdown("""
    ### 📚 Tips
    - Be specific & descriptive
    - Include art style names
    - Mention lighting & mood
    - Keep prompts focused
    """)

with col_foot3:
    st.markdown("""
    ### 🔗 Links
    - [Replicate](https://replicate.com)
    - [Nano Banana](https://replicate.com/google/nano-banana)
    - [Google AI](https://ai.google.dev)
    """)

st.markdown("---")
st.caption("🐱 Cat Transformer v1.0 | Powered by Google Nano Banana & Replicate")
