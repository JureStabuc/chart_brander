# Chart brander
An app developed for the Office for National Statistics design team for branding images to use on social media. It takes an image from the web, adds social branding (title, source and logo) and returns the image in the browser. Make sure Chrome browser is installed. 

## How to run?

1. Open the terminal and make sure you have python version 3. To check type `python --version` into the terminal. If not install it by running `brew install python3` in terminal. [More details](https://docs.python-guide.org/starting/install3/osx/) about how to install brew. This should also install pip which we will use to install packages.

2. Install packages needed: `pip install Flask selenium Pillow`.

3. Navigate to the repository in the terminal `cd path to folder`.

4. When in folder run the app with `flask run` in terminal. 

5. Navigate to `http://127.0.0.1:5000/` in your browser.

6. Fill in the title, relative link to the chart e.g. `/peoplepopulationandcommunity/leisureandtourism/bulletins/overseastravelandtourism/januaryfebruaryandmarch2018provisionalresults/7c41529a`, source and click `submit`.

7. You should be redirected to a page with the generated image. For now, you cannot click `Save image as` as it won't save it. One workaround is to right click, `Copy image` and paste it to, for example, Photoshop. 
