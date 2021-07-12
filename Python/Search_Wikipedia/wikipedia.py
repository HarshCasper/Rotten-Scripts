# pip install wikipedia       
import wikipedia  

# taking the query input in the form of voice command from the user using the get_command function
query = input()

try:
    # checking if it contains the word 'wikipedia'
    if 'wikipedia' in query:
        print('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        
        # searching query on wikipedia and getting the results
        results = wikipedia.summary(query, sentences=5)
        print("According to Wikipedia...")
        print(results)

    else:
        print("Try again..\nFor example, write like this \"india country wikipedia\"")

except Exception as e:
    print("There is something wrong. Please try again...")
