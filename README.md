# Word-Cloud-With-Python
Creating a motivational word cloud with Python
This project generates a custom word cloud based on predefined word frequencies and applies specific colors to each word. The word cloud is created using Python libraries and is visualized using matplotlib.

Project Overview
This script generates a word cloud that reflects motivational words and phrases. Each word has a specific frequency and color, representing different aspects of success and dedication. The color scheme is customizable, making it easy to adapt the visual theme to your preferences.

Installation
To run this project, you’ll need to install the following dependencies:
pip install wordcloud matplotlib numpy

Code Details
The main script:

Defines Word Frequencies: Each word's frequency is set in the word_freq dictionary.

Customizes Colors: Colors are applied to each word based on the color_function.

Generates the Word Cloud: The WordCloud function generates an image based on frequencies and color preferences.

Displays the Word Cloud: The word cloud is displayed in a plot with matplotlib.

Saves the Output: The generated word cloud image is saved as wordcloud2.png.

Key Variables
word_freq: Contains words and their frequency.
color_function: A function that assigns a color to each word based on its name.

Running the Project
To run the project, execute the script in a Python environment. The word cloud image will display on your screen and be saved as wordcloud2.png in the current directory.
