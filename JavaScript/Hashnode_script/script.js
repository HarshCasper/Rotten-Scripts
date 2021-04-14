// all requires
const fetch = require("node-fetch");
const ObjectsToCsv=require("objects-to-csv");


//variables required
var page=0;
var post_count=process.argv[2];



// Working Function
fetchPosts=async(post_count)=> {
    var posts_data=[]; // stores posts
    var count=0;
    var current_post_count=0;

    while(current_post_count<post_count)
    {
        const query=`{
            storiesFeed(type:BEST
                page:${page}){
                title
                brief
                author{
                  name
                }
              }
        }`

        const response = await fetch('https://api.hashnode.com', {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
            },
            body: JSON.stringify({ query }),
        })
    
        const ApiResponse=await response.json();
        
        var posts=ApiResponse.data.storiesFeed;

        current_post_count+=posts.length;

        page++;

        for(var post of posts){
            count++;

            var post_object={}

            post_object["title"]=post["title"];

            post_object["brief"]=post["brief"].split("\n").join(" ");

            post_object["author"]=post.author["name"];

            posts_data.push(post_object)

            if(count>=post_count)
            break;
        }
    }

    const csv=new ObjectsToCsv(posts_data)

    await csv.toDisk("./output.csv")

}

fetchPosts(post_count);