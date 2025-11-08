# 🐱 Cat Transformer - AI Image Editor

Transform your cat photos with Google's Nano Banana AI! Describe what you want to do with your cat photo, and let the AI make it happen.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)

## ✨ Features

- 📸 **Upload Cat Photos** - Support for JPG, PNG, and WEBP formats
- ✍️ **Natural Language Descriptions** - Just describe what you want
- 🎨 **AI-Powered Editing** - Google's Nano Banana (Gemini 2.5 Flash Image)
- 💾 **Download Results** - Save your transformed cats
- 💡 **6 Preset Ideas** - Quick inspiration buttons
- 🚀 **Cloud Hosted** - No installation needed, runs on Streamlit Cloud

## 🚀 Try It Online

**[👉 Click here to open the app](https://share.streamlit.io)** (replace with your actual URL after deployment)

No installation needed! Just upload a cat photo and start transforming.

## 🎨 Example Transformations

- "Make the cat look like a superhero with a cape"
- "Transform the cat into a beautiful watercolor painting"
- "Make the cat look royal with a crown and royal outfit"
- "Turn the cat into a cute cartoon character"
- "Make the cat look like an astronaut in space"
- "Paint the cat in oil painting style"

## 🏠 Run Locally

### Prerequisites
- Python 3.8 or higher
- Git
- Free Replicate API token

### Step 1: Get Replicate API Token

1. Go to https://replicate.com
2. Sign up (free - no credit card required)
3. Navigate to Account → API tokens
4. Copy your API token

### Step 2: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/cat-transformer.git
cd cat-transformer
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up API Token

**Option A: Environment Variable (recommended)**
```bash
# macOS/Linux
export REPLICATE_API_TOKEN=r8_xxxxxxxxxxxxx

# Windows (Command Prompt)
set REPLICATE_API_TOKEN=r8_xxxxxxxxxxxxx

# Windows (PowerShell)
$env:REPLICATE_API_TOKEN="r8_xxxxxxxxxxxxx"
```

**Option B: .env File**
```bash
# Copy the example file
cp .env.example .env

# Edit .env and paste your token
REPLICATE_API_TOKEN=r8_xxxxxxxxxxxxx
```

### Step 5: Run the App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 📦 Deployment on Streamlit Cloud

### Quick Setup

1. Push this repository to GitHub (make sure it's public)
2. Go to https://share.streamlit.io
3. Click "New app"
4. Select your repository and set main file to `app.py`
5. Click "Deploy"
6. Once deployed, go to Settings → Secrets and add:
   ```
   REPLICATE_API_TOKEN=your_token_here
   ```

**See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed instructions.**

## 🔒 Security

⚠️ **Never commit your API token to GitHub!**

- The `REPLICATE_API_TOKEN` environment variable is loaded automatically
- On Streamlit Cloud, use the Secrets feature (not environment variables)
- The `.env` file is in `.gitignore` for safety
- Use `.env.example` as a template

## 📋 Project Structure

```
cat-transformer/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── .env.example                    # Template for environment variables
├── .gitignore                      # Git ignore rules
├── README.md                       # This file
├── DEPLOYMENT_GUIDE.md             # Detailed deployment instructions
├── SETUP_GUIDE.md                  # Local setup guide
└── streamlit_config.toml          # Streamlit configuration
```

## 🛠️ Technologies Used

- **Streamlit** - Web framework for building data apps
- **Google Nano Banana** - AI model for image generation/editing
- **Replicate API** - API access to AI models
- **Pillow** - Image processing
- **Python 3.8+** - Programming language

## 📚 How It Works

1. You upload a cat photo
2. You describe what you want to transform
3. The app sends the image and description to Google's Nano Banana model
4. The AI generates a transformed version
5. You can download and share the result

The Nano Banana model is incredibly good at:
- ✨ Understanding natural language descriptions
- 🎨 Maintaining character consistency
- 🌍 Preserving scene context
- 💎 Creating photorealistic results

## ⚡ Tips for Best Results

### Writing Better Prompts

**❌ Bad prompts:**
- "change the cat"
- "make it pretty"
- "edit the image"

**✅ Good prompts:**
- "Make the cat look like a medieval knight wearing armor"
- "Transform the cat into a photorealistic wild tiger"
- "Paint the cat as if it were in a Victorian oil painting"

### Best Practices

- Be specific about the style (watercolor, oil painting, cartoon, etc.)
- Include mood and atmosphere details
- Mention lighting conditions
- Use artistic references when possible
- Keep descriptions concise and focused
- Don't use too many contradictory instructions

## 🆘 Troubleshooting

### "REPLICATE_API_TOKEN not set"
- Ensure you've set the environment variable correctly
- Or create a `.env` file with your token
- Restart the terminal after setting environment variables

### "Error during transformation"
- Check that your API token is valid
- Make sure your internet connection is stable
- Try with a smaller image file
- Use a simpler, more focused prompt
- Wait a moment and try again (rate limits may apply on free tier)

### Image format not supported
- Use JPG, PNG, or WEBP formats
- Ensure the image is not corrupted
- Try compressing large images to under 10MB

### App not starting
- Check Python version (3.8+)
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Look for syntax errors in the console

## 📊 Limits

- **Free Replicate tier**: Limited requests per day
- **File size**: Max ~50MB for upload (recommended < 10MB)
- **Processing time**: Usually 5-30 seconds per image
- **Supported formats**: JPG, PNG, WEBP

## 💡 Future Ideas

- Batch processing multiple images
- History of transformations
- Favorite templates/prompts
- Image gallery/showcase
- Advanced editing tools
- Before/after slider
- User feedback system

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Fork the repository
- Create a feature branch (`git checkout -b feature/amazing-feature`)
- Commit your changes (`git commit -m 'Add amazing feature'`)
- Push to the branch (`git push origin feature/amazing-feature`)
- Open a Pull Request

## 📞 Support

If you encounter any issues:
1. Check the [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
2. Check the [SETUP_GUIDE.md](SETUP_GUIDE.md)
3. Review the troubleshooting section above
4. Open an issue on GitHub

## 🔗 Useful Links

- [Streamlit Documentation](https://docs.streamlit.io)
- [Replicate API Docs](https://replicate.com/docs)
- [Google AI Models](https://ai.google.dev)
- [Nano Banana Model](https://replicate.com/google/nano-banana)
- [Streamlit Community Cloud](https://share.streamlit.io)

## 🎉 Credits

- Built with [Streamlit](https://streamlit.io)
- Powered by [Google Nano Banana](https://replicate.com/google/nano-banana)
- Hosted on [Streamlit Cloud](https://share.streamlit.io)

---

**Happy cat transforming! 🐱✨**

Made with ❤️ for cat lovers everywhere
