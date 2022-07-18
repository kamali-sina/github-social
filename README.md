# github-social

Check out your GitHub account as a social media account! Read more to find out what we can do for you.

## How To Install

Our package is published on PyPI, so you can install it with pip:

```bash
    pip install github-social
```

## features

Do you want to findout which one of your friends don't follow you back? Use the code below to find out!

```python
    from githubsocial.GithubUser import GithubUser

    GithubUser("YOUR_USERNAME").get_following_followers_diff()
```

You can also get a list of your followers and followings by running:

```python
        from githubsocial.GithubUser import GithubUser
    
        followers = GithubUser("YOUR_USERNAME").get_followers()
        followings = GithubUser("YOUR_USERNAME").get_followings()
```
