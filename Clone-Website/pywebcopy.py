from pywebcopy import save_webpage

kwargs = {'project_name': 'website-clone'}

save_webpage(

    # url pf the website
    url=input("Enter website you want to clone: "),

    # folder where the copy will be saved
    project_folder='/',
    **kwargs
)
