# Pull Request Analysis
### This script involves Web Scraping and Data Visualization of various Pull Requests which have been committed to this repo along with Dataset Generation and Machine Learning to bring out insights from the data.



## Check out the code [[here](https://github.com/Aditya-Komaravolu/PR-Analyzer/blob/main/PRScrapper.ipynb)].

## Step 1: Visit the target website

![image](https://user-images.githubusercontent.com/64011471/131397259-3eb7ffd1-b2c8-4cc2-915e-1415758c4a84.png)

 
## Step 2: Locate the PR markup using Debugger 
  
![image](https://user-images.githubusercontent.com/64011471/131397987-63ad1aa6-8edc-4ad6-bcf5-51117a39cbaa.png)

* Once we locate the required class for the PR containers, then we can use a simple for loop to extract the `<a>` tag which contains the actual reference link to the PR location.
* Later we combine `href` along with `base_url: https://github.com/` to get the complete website link for each pull request.
  
## Step 3: Creating a Pandas DataFrame 
  * Now that we have `PR Links` and `Status` ready, it is time to combine them and store them together as a DataFrame (in simple terms, a table).
  ![image](https://user-images.githubusercontent.com/64011471/131401426-ee775ce1-3a4f-4473-b2bb-c0695cf2d318.png)
  
## Step 4: Fetch all the Contributors for each PR
  * We need the names of the contributors to better understand the diversity of the repo.
  * For that, we can again follow step 2 and get the required parameters.
  * Use `BeautifulSoup` to get the required tags containing the data of the contributors.
  * Later update the DataFrame by adding a new column to represent the Contributors.
  
  ![image](https://user-images.githubusercontent.com/64011471/131402166-78c4e372-e4da-40e7-91ba-a8a89107156f.png)

  
 ## Step 5: Distinct Contributors along with Count
  * We need to find out all the distinct contributors where every PR can involve more than one contributor.
  * For that we can write a nested for loop to append only if the string is different from all the strings which were added to the list in before iterations.To refer codebase, click [[here](https://github.com/Aditya-Komaravolu/PR-Analyzer/blob/main/PRScrapper.ipynb)].
  * Once done, we now have to compute the total number of contributions were done by each contributor in all the PR's. 
  * To calculate the count, define a for loop which tallies each and every contributor with the the actual column in the DataFrame.
  
 ## Step 7: Create a JSON File
  * WE can store the contributors and the count as key-value pairs in a dictionary.
  * Later use file pointer and json package to dump the dictionary as a json object.
 
  ## Step 8: Visualizing Data
  * Now that we have PR status and Total number of contributions by each contributor, we can plot them for better visualization of the entire repo.
  * I prefer `Bar Plots` for the current situation because we have categorical variables to represent and what else is better than a bar graph!  :)

  * ### PR status:
  
    ![image](https://user-images.githubusercontent.com/64011471/131405268-1ff889ba-81a5-46e5-b37e-d727df5bed62.png)
  
  * ### Top 5 Contributors:
  
    ![image](https://user-images.githubusercontent.com/64011471/131405338-d630d7fa-6ac9-4bc5-b98d-dd4f768de181.png)


 ## <u>Additional Analysis</u>: Finding out the Average time taken for each Pull Request
 
 * To find out the start and end time, locate the time reference for every container in the DevTools.
  
   ![image](https://user-images.githubusercontent.com/64011471/131406319-db2f7d6a-9467-4bf2-8e5b-24773ed79c10.png)
 
 * Once we get the tag associated with the datetime, we can reapeat step 2 to get complete dates along with timestamp from every PR.
 
 ![image](https://user-images.githubusercontent.com/64011471/131406692-f3e690cf-0e3b-4971-9d22-9b1947806081.png)

 * Take minimum and maximum values from all the timestamps from every PR and subtract them to get the time taken to merge a PR.
 * If you want, you can convert it into Days H:M:S format by using the datetime package to convert the string obejct to a datetime object.
 * Datetime objects can be converted into seconds format by using `total_seconds`.
 
 ![image](https://user-images.githubusercontent.com/64011471/131408733-dc0eec0b-6843-41e1-8b79-50a2e42a69c4.png)

 
 ## Categorizing the Active PR time using KMeans Clustering
 * Now that we have the active PR time in seconds format, it is now easier to fit the data to model.
 * I choose KMeans because here we have active PR time in the form of clusters (atleast as per my initial observation) and since we are about to deal with uncategorised Pr time values, what's better than KMeans.
 * Pass the single-column 'Active PR Time(in Seconds)' to the model with `n_clusters=3`.
 * Later plot the centriods of those clusters and those values are itself the 'Average PR time' values.
 
 ![image](https://user-images.githubusercontent.com/64011471/131408811-0887cb50-5fcd-4b77-b853-2df2e85e66a0.png)
 
 * These three values describe the whole dataset where the average PR active period is: 
   * Either approx 3 days.
   * Or approx 28 days (a month).
   * Or approx 80 days or greater.
 
 Please see the code [[here]()] to get better insights and clarity.
 
