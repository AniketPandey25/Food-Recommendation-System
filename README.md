# FOOD RECOMMENDATION SERVICE
It's a food recommendation app that gives you various recipes based on your search and demand. Just put your thought in the search bar and you will have more recipes realted to it. Also, if your day is not going that good just put in a picture of yourself and it will give you recipes to lighten your mood.

# Prerequisite
1. Install Git https://git-scm.com/downloads
2. Install Docker https://www.docker.com/products/docker-desktop
3. Install Docker Compose https://docs.docker.com/compose/install/#install-compose
4. Create an AWS IAM User with full Rekognition access https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html

# Start Service
1. Clone repository to your local device
`git clone https://github.com/AniketPandey25/Food-Recommendation-System.git`

2. Change directory
`cd Food-Recommendation-System`

3. Modify **docker-compose.yml**  
>Replace existing AWS_ACCESS_KEY_ID with your IAM User AWS_ACCESS_KEY_ID in **line 39**  

>Replace existing AWS_SECRET_ACCESS_KEY with your IAM User AWS_SECRET_ACCESS_KEY in **line 40**  

4. Build containers
`docker-compose build --no-cache --pull`

5. Run containers
`docker-compose up`

6. Open http://localhost:8080 in the browser

# Test Service
Please wait for 10-20 seconds before searching for recipes once you open http://localhost:8080. Please pick the option only from the dropdown menu after searching.
## Search Recipe
- Search for recipe in search box by entering keywords.

![Search Demo](https://jtp-technical-project-bucket.s3.ap-south-1.amazonaws.com/images/search.png)
## Select Recipe
- Select recipe from search box
- Wait for 15-20 seconds to get recommendation

![Select Recipe Demo](https://jtp-technical-project-bucket.s3.ap-south-1.amazonaws.com/images/select_recipe.png)
## Select Recipe and Cook Time
- Select recipe and cook time from search box
- Wait for 15-20 seconds to get recommendation

![Select Recipe and Cook time Demo](https://jtp-technical-project-bucket.s3.ap-south-1.amazonaws.com/images/select_recipe_cooktime.png)
## Upload an Image
You can upload an image of yours which should be in **png** or **jpg** format only and if the system finds that you are **upset** then it will suggest you some recipe otherwise it won't return any result.

![Upload Image Demo](https://jtp-technical-project-bucket.s3.ap-south-1.amazonaws.com/images/upload_image.png)
## Demo
The demo given below would help you go through the process with ease.
[Demo](https://jtp-technical-project-bucket.s3.ap-south-1.amazonaws.com/videos/demo_functionality.mkv)

# Stop Service
1. Change directory
`cd Food-Recommendation-System`

2. Stop containers
`docker-compose down --volumes`

# Future Work
If the service is developed further there are a few changes that could possibly enhance its performance such as implementing some kind of caching machenism for backend and frontend and machine learning can be used to provide more accurate recommendation.

# References
- https://docs.mongoengine.org/apireference.html
- https://angular.io/docs
- https://flask.palletsprojects.com/en/2.0.x/#api-reference
- https://medium.com/swlh/how-to-set-up-a-react-app-with-a-flask-and-mongodb-backend-using-docker-19b356180199
- https://stackoverflow.com/questions/31259783/how-to-execute-a-block-of-code-only-once-in-flask
- https://stackoverflow.com/questions/25594893/how-to-enable-cors-in-flask#:~:text=from%20flask%20import%20Flask%20from,cross%2Dorigin%2Dworld!%22
- https://material.angular.io/components/select/overview
- https://material.angular.io/components/autocomplete/overview
- https://material.angular.io/components/card/overview
- https://material.angular.io/components/button/overview
- https://angular.io/guide/inputs-outputs
- https://stackoverflow.com/questions/39738974/emit-event-from-parent-to-child
- https://www.kaggle.com/sooryaprakash12/cleaned-indian-recipes-dataset

# Issue in the last review
 Python backend service timed out. To solve this problem I changed `gunicorn --bind 0.0.0.0:5000 app:app` to `gunicorn --bind 0.0.0.0:5000 --timeout 300 app:app` https://stackoverflow.com/questions/10855197/gunicorn-worker-timeout-error
