const fs=require('fs');
if(fs.existsSync('issueDetails.json'))
{
    console.log('YES');
}
else
{
    fs.writeFileSync('issueDetails.json',{});
    console.log('nO');
}