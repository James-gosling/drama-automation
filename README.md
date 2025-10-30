# 🎬 Drama Automation

An automated system for creating engaging drama videos with Text-to-Speech (TTS) and short-form content optimization.

## 📋 Overview

Drama Automation is a Python-based toolkit that streamlines the creation of drama videos for social media platforms. It combines text-to-speech synthesis, video editing, and automated workflows to produce professional-quality short-form content.

### ✨ Features

- 🎙️ **Text-to-Speech Integration**: Generate natural-sounding voiceovers from scripts
- 🎥 **Automated Video Creation**: Combine audio, images, and effects into polished videos
- 📱 **Social Media Optimization**: Optimized output for YouTube Shorts, TikTok, and Instagram Reels
- 🔄 **Batch Processing**: Process multiple scripts efficiently
- 🎨 **Customizable Templates**: Easy-to-modify templates for different styles
- ☁️ **Google Colab Support**: Run in the cloud without local setup

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- (Optional) Google Colab account for cloud execution

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/James-gosling/drama-automation.git
   cd drama-automation
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**
   ```bash
   python -c "import moviepy, gtts; print('Dependencies installed successfully!')"
   ```

### Using Google Colab

1. Open one of the notebooks in the `/notebooks` directory
2. Click "Open in Colab" badge (if available)
3. Run the setup cells to install dependencies
4. Follow the notebook instructions

## 📖 Usage

### Using Notebooks

The primary way to use this project is through the interactive Jupyter notebooks:

1. Navigate to the `/notebooks` directory
2. Open `drama_video_creator.ipynb` in Jupyter or Google Colab
3. Follow the step-by-step instructions in the notebook
4. Customize parameters as needed (voice, background, effects)
5. Run all cells to generate your video

### Example Workflow

```python
# Example code structure (to be implemented in notebooks)

# 1. Load or create your script
script = """
[Character A]: I can't believe you did this!
[Character B]: I had no choice...
"""

# 2. Generate TTS audio using gTTS
from gtts import gTTS
tts = gTTS(text=script, lang='en')
tts.save("output/audio/dialogue.mp3")

# 3. Create video using MoviePy
from moviepy.editor import *
# Combine audio, background, and text overlays
# Export final video to output/videos/
```

## 📁 Project Structure

```
drama-automation/
├── notebooks/          # Jupyter notebooks for interactive use
│   ├── drama_video_creator.ipynb
│   ├── video_editor.ipynb
│   └── batch_processor.ipynb
├── assets/            # Media assets (images, audio, fonts)
│   ├── images/
│   ├── audio/
│   ├── fonts/
│   └── templates/
├── output/            # Generated videos and intermediate files
│   ├── videos/
│   ├── audio/
│   └── previews/
├── requirements.txt   # Python dependencies
├── .gitignore        # Git ignore rules
├── LICENSE           # MIT License
└── README.md         # This file
```

## 🎨 Example Outputs

### Sample Drama Video
- **Duration**: 15-60 seconds
- **Format**: MP4, vertical (9:16) for mobile
- **Audio**: AI-generated TTS with background music
- **Style**: Dramatic text overlays with transitions

### Example Script Format

```
[Character A]: I can't believe you did this!
[Character B]: I had no choice...
[Character A]: There's always a choice!
[Narrator]: What will happen next?
```

## ⚙️ Configuration

You can configure the automation by modifying parameters directly in the notebooks or by creating environment variables:

### Environment Variables (Optional)

Create a `.env` file in the root directory for custom settings:

```env
# TTS Settings
TTS_ENGINE=gtts
TTS_LANGUAGE=en
TTS_VOICE=female

# Video Settings
VIDEO_WIDTH=1080
VIDEO_HEIGHT=1920
VIDEO_FPS=30

# Output Settings
OUTPUT_FORMAT=mp4
OUTPUT_QUALITY=high
```

### Notebook Parameters

Most settings can be configured directly in the notebook cells:
- Voice selection and language
- Video dimensions and quality
- Background images and music
- Text overlay styles and animations

## 🛠️ Advanced Features

### Custom Voice Profiles
- Support for multiple TTS engines (gTTS, pyttsx3)
- Custom voice speed and pitch adjustment
- Multiple language support

### Video Effects
- Text animations and transitions
- Background music integration
- Subtitle generation
- Color grading and filters

### Export Options
- Multiple format support (MP4, MOV, AVI)
- Resolution presets for different platforms
- Automatic compression and optimization

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Text-to-Speech powered by gTTS
- Video processing with MoviePy
- Image handling with Pillow
- Audio processing with pydub

## 📧 Support

For questions, issues, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review example notebooks

## 🔄 Roadmap

- [ ] Add more TTS engine options
- [ ] Implement AI-powered script generation
- [ ] Add video template marketplace
- [ ] Support for multi-language videos
- [ ] Real-time preview functionality
- [ ] Mobile app integration

---

**Made with ❤️ for content creators**
