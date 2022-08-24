# Opening statement
I wanted to start this off by expressing my gratitude for the opportunity that you are considering me for.
This test has been a pure pleasure to take, and is different from all other company interviews I have ever done.
 
# Challenge 1
    Goal:
        1: Return List when you have multiple json objects.
        2: Return Object when you only have the one json object. (unique ID ensures only 1 result possible)
    Approach:
        In the src/mongoflask.py file there was a list() surrounding the cursor object making that always return as a list.
        I could either separate the logic of checking to see if there was only one result during the find_restaurants() execution or I could just write the restaurant() function to check and strip it once it got there.
 
        I saw a potential for wanting to search on more fields then just id.  So I took a new option,
        I have created restaurant_wide_search() which is registered under the api path of /api/v2/restaurant/<field>/<search>
 
        All 3 endpoints point at a solution that works for them.
        If no parameter is given, the entirety of the collection is searched
        If an unique ID is requested (via the api /api/v1/restaurant/<id>) 1 result is returned
        However you can also look up /api/v1/restaurant/type_of_food/ch which will return to you all case insensitive results of foods groups that start with ch
 
        I utilize urlparse in a way that allows characters and spaces to be represented by their %codes. I thought about implementing the version that uses + instead but decided that further discussion with the project leaders would be needed.  Treating this like a POC there was no need to stress on perfection yet.
 
        urlparse import gets wrapped up in a tray: except: due to python 2.7 needing to import it slightly differently.  There are likely better ways to handle this but I would instead suggest moving away from 2.7 compatibility if possible, or at least picking 1 version of python to run this on.
 
        Utilizing a regex match and to check if a number is float or not. It is now possible to search by rating. This was the most requested feature in my head.  Further work will need to be done to make the code more pretty and elegant, but this is a functional POC.
       
    Faults:
        If you are searching for an address you must get to at least 1 non numeric character.  This could be fixed but was low priority.
 
        I wasn't sure if I would want the text lookup when searching fields, to also allow the finding of the middle of strings. It's an easy fix if you want it. But that seemed like it should be discussed with the project manager and application architects to determine what expected results are.
    Thoughts:
        I was excited to make my own tests, but I thought about it and wasn't sure if that would be frowned upon for messing with how you wanted to automate the testing of my code.
        I liked this exercise. It was a lot of fun to try and extrapolate outwards where the limits could be pushed
 
# Challenge 2
    Goal:
        Setup a ci/cd pipeline with unit tests and artifacts.
    Approach:
        I utilized a github bucket integrated with CircleCI for the cicd. I placed a png in assets showing the connection and some builds.
    Thoughts:
        This was fun, I hadn't used CircleCI before (usually been in a bamboo shop). It was cool.
 
# Challenge 3/4/5
    Goal:
        Dockerize ALL THE THINGS!
    Approach:
        I basically completed these all at once. Find your groove, and get too it.
        Setup a user so our apps aren't using root.
    Faults:
        I would have liked to set up some secret handling, but decided to stick a little better to the parameters at hand. KISS!
    Thoughts:
        Pleasant, covered all the bases. Allowed me to groove into something from scratch.
        Makes me really want to play with docker more.  I don't get to do that enough.
 
# Challenge 6
    Goal:
        K8S it all.
    Approach:
        Use the tools you have at hand.
        And If you don't learn some new ones.
        I've never used minikube/microk8s/dockerk8s before. I played for a while here.
        Have helm initiate a project, clean up the cruft
        Use the k8s tool to work with docker compose files
        Clean up the Kruft and fix all the data so that it's actually what you want. (Honestly I use it more as a checklist so I don't forget anything. I end up tweaking most fields most of the time anyway.)
        Realize you haven't set up any sort of artifactory yet.  Use your free image space on docker hub.  And then learn how to integrate CircleCI. (I decided to leave the key in the config, but it's been marked as inactive.  Just wanted an easy way to turn it back on if you are wanting to do/discuss anything around that.)
        I got creative (compared to where I've been) in my liberal use of the :tag, since I wanted it to stay free.
 
# Conclusion (mostly)
    This is by far the best intro to a company I have ever been a part of. I didn't have to sweat about missing keystrokes because you have 5 people looking at you when you mistype words.  I got to do this at my pace and when I could get it done (I found my best grooves at the quiet hours of 1-5am).
    This test reminds me a lot of the RHEL test I took way too many years ago.  And I really wish that I had this test sooner in life; it would have made my dive into all of these technologies easier if this was how I had been introduced to them.
 
    I hope I have answered these questions satisfactorily,
    Thank you for your time.
 
    --Jason Verde
 
 
one last thing
# Bug Fix
I did want to point out one potential bug that I found along my travels.  In the README.md you mention on line 114 that running the command
```bash
curl localhost:8080/api/v1/restaurant/55f14313c7447c3da705224b | jq
```
to gather a single record.  By default the application will actually return an error
To solve this error I found that in the file src/mongoflask.py on line 29 changing
```python
query["_id"] = ObjectId(id)
```
to
```python
query["_id"] = ObjectId(_id)
```
was required for the baseline (pre challenges) to work properly.