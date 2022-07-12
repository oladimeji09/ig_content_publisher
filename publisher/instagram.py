# @auto-fold regex \.\
# NOTE: https://developers.facebook.com/docs/instagram-api docs

import requests as r, json,time,json,ig_tags, random as rd
from python_helpers import python_helper as ph

from instagrapi import Client
cl = Client()
baseurl = 'https://graph.facebook.com/v11.0/'
ig_users = json.load(open(ph.root_fp+'/creds/creds.json')).get('ig_users')
ig_creds = json.load(open(ph.root_fp+'/creds/creds.json')).get('instagram')
user_token = open(ph.root_fp+"/creds/ig_access_token.txt", "r").read()
comment_log =ph.root_fp+'/ig_content_publisher/tests/comments_log.json'
delete_comment=ph.root_fp+'/ig_content_publisher/tests/delete_comment.json'

def generate_long_token(app_id,app_secret,user_token):
    """Use this to generate Long-Lived User Access Tokens"""
    resp = r.get(baseurl+"""oauth/access_token?grant_type=fb_exchange_token&client_id={0}&client_secret={1}&fb_exchange_token={2}""".format(app_id,app_secret,user_token))
    if resp.status_code == 200:
        with open(ph.root_fp+"/creds/ig_access_token.txt", "w") as f:
            try:
                f.write(resp.json()['access_token'])
            except:
                f.write(user_token)
                f.close()
        return resp.json()['access_token']
    else:
        print("Wrong user token no changes to ig_access_token.txt")

def get_page_tokens(app_id,app_secret,user_token):
    """Use this to retrieve page tokens for all pages in the account"""
    resp = r.get(baseurl+'me/accounts?access_token={}'.format(generate_long_token(app_id,app_secret,user_token)))
    return resp.json()

def get_ig_acc(page_id):
    """Retrieve instagram business ID and username"""
    resp = r.get(baseurl+"""{0}?fields=id,name,instagram_business_account,username&access_token={1}""".format(page_id,page_access_token))
    return resp.json().get('instagram_business_account')

def post_img_to_ig(ig_id,img_url,caption=''):
    """Send an image to instagram business account"""
    resp = r.post(baseurl+"""{0}/media?image_url={1}&caption={2}&access_token={3}""".format(ig_id,img_url,caption,page_access_token)) #generates creation_id
    if resp.status_code != 200:
        print(resp.json())
    else:
        resp = r.post(baseurl+"""{0}/media_publish?creation_id={1}&access_token={2}""".format(ig_id,resp.json().get('id'),page_access_token))
    return resp.json().get('id') if resp.status_code == 200 else  resp.json()

def get_ig_media(ig_id):
    """Retrieve instagram media"""
    resp = r.get(baseurl+"""{0}/media?access_token={1}""".format(ig_id,page_access_token))
    return resp.json()

def post_to_page(page_id,caption):
    """This will make a post to the page"""
    resp = r.post(baseurl+"""{0}/feed?message={1}&access_token={2}""".format(page_id,caption,page_access_token))
    return resp.json()

def get_ig_media(ig_id):
    """Retrieve a list IG Media ID relating to a media"""
    resp = r.get(baseurl+"""{0}?fields=media&access_token={1}""".format(ig_id,page_access_token))
    return resp.json().get('media').get('data') if resp.status_code == 200 else  resp.json()

def get_ig_media_meta(media_id):
    """Retrieve metadata relating to a Media ID"""
    resp = r.get(baseurl+"""{0}?fields=id,ig_id,media_product_type,media_type,media_url,permalink,thumbnail_url,timestamp,caption,comments_count,comments&access_token={1}""".format(media_id,page_access_token))
    resp.json()

def post_ig_media_comment(media_id,comment):
    """Post comment to Media ID"""
    resp = r.post(baseurl+"""{0}/comments?message={1}&access_token={2}""".format(media_id,comment,page_access_token))
    return resp.json().get('id') if resp.status_code == 200 else  resp.json()

def read_ig_media_comment(media_id):
    """Read comment to Media ID"""
    resp = r.get(baseurl+"""{0}/comments?access_token={1}""".format(media_id,page_access_token))
    return resp.json().get('data') if resp.status_code == 200 else  resp.json()

def delete_ig_media_comment(comment_id):
    """Post comment to Media ID"""
    resp = r.delete(baseurl+"""{0}?access_token={1}""".format(comment_id,page_access_token))
    return resp.json().get('success') if resp.status_code == 200 else  resp.json()

def get_token(user_name):
    """Return tokens based on username"""
    tokens = get_page_tokens(ig_creds.get('app_id'),ig_creds.get('app_secret'),user_token).get('data')
    for item in tokens:
        if  user_name.lower() == item.get('name').lower():
            global page_access_token
            page_access_token = item.get('access_token')
            return item

def get_post_quota(ig_id):
    """Return quota usage for a username"""
    resp = r.get(baseurl+'{}/content_publishing_limit?fields=quota_usage,config&access_token={}'.format(ig_id,page_access_token))
    return resp.json()

#todo:change this to you don't have to log in everyime
def login(username:str, password:str):
    """login and return cl"""
    cl.login(username, password)
    return cl

def logout():
    cl.logout()

def get_hashtag_medias_top(tags_list:list, N=5):
    """Get a list of top medias from hashtags"""
    if type(tags_list) is not list:
        raise ValueError("tags_list need to be a list")
    else:
        media_list = []
        for tag in tags_list:
            time.sleep(rd.randint(0, 200))
            try:
                medias = cl.hashtag_medias_top(tag, amount=N)
                for media in medias:
                    media_list.append(media)
            except:
                continue
        return media_list

def get_user_media(username_list:list, N=5):
    """Get a list of N Media for usernames"""
    if type(username_list) is not list:
        raise ValueError("username_list must be a list")
    else:
        media_list = []
        for username in username_list:
            time.sleep(rd.randint(0, 200))
            try:
                user_id = cl.user_id_from_username(username)
                medias  = cl.user_medias(user_id, N)
                for media in medias:
                    media_list.append(media)
            except:
                continue
        return media_list

def comment_on_media(media_list:list,comment:str, comment_fp=comment_log):
    """Comment on media and like the comment & post"""
    if type(media_list) is not list:
        raise ValueError("media_list must be a list")
    else:
        for media_id in media_list:
            time.sleep(rd.randint(0, 200))
            try:
                media_id = dict(media_id)
                with open(comment_fp,'r') as fp: #todo: find a way to make this file relative
                    if media_id.get('code') not in fp.read():
                        cl.media_like(media_id.get('pk'))
                        comment_id = dict(cl.media_comment(media_id.get('pk'), comment))
                        like_comment = cl.comment_like(comment_id.get('pk'))
                        with open(comment_fp,'a+') as fp:
                            json.dump({"commented_by_username": cl.username,"commented_by_id": cl.user_id,
                            "media_slug" : "www.instagram.com/p/"+media_id.get('code'),
                            "media_id":media_id.get('pk'), "comment_id": comment_id.get('pk'),
                            "media_owner_id": dict(media_id.get('user')).get('pk'),
                            "media_owner_username": dict(media_id.get('user')).get('username'),
                            "comment_date":comment_id.get('created_at_utc').strftime("%Y-%m-%d %H:%M")},fp)
                            fp.write('\n')
                        print('Comment written on post www.instagram.com/p/{} comment_id = {}'.format(media_id.get('code'),comment_id.get('pk') ))
                    else:
                        print('There is a comment on this post already')
            except:
                print('Error trying for {} '.format("www.instagram.com/p/"+dict(media_id).get('code')))
                continue

def delete_comment(media_id:str, media_comment_id:int, delete_comment_fp = delete_comment):
    """Delete comment on media"""
    info = dict(cl.media_info(media_id))
    cl.comment_bulk_delete(media_id, [media_comment_id])
    time.sleep(rd.randint(0, 200))
    with open(delete_comment_fp,'a+') as ft: # write the deleted line to file
        json.dump({
            "media_slug" : "www.instagram.com/p/"+info.get('code'),
            "media_id":media_id, "media_comment_id": media_comment_id,
            "media_owner_id": dict(info.get('user')).get('pk'),
            "media_owner_username": dict(info.get('user')).get('username'),
             "delete_date" :time.strftime("%Y-%m-%d %H:%M")},ft)
        ft.write('\n')
        print('Deleted comments on www.instagram.com/p/{} comment_id = {}'.format(info.get('code'),info.get('pk') ))

def delete_media(username:str,password:str,N=5):
    """Delete media from user"""
    login(username, password)
    media_list=get_user_media([username],N)
    for media in media_list:
        try:
            cl.media_delete(media.dict().get('pk'))
            print('Deleted Media on www.instagram.com/p/{}'.format(media.dict().get('code')))
            time.sleep(rd.randint(0, 200))
        except:
            continue
    logout()
    print('logged out')

def un_follow_user(user_id:int, follow ='follow'):
    """Follow or unfollow a user"""
    time.sleep(rd.randint(0, 200))
    return cl.user_follow(user_id) if follow == 'follow' else cl.user_unfollow(user_id)

def user_network(user_id:int, flow='following', N=25):
    """Return a list of followers or users following the said user."""
    time.sleep(rd.randint(0, 200))
    return cl.user_following(user_id, amount = N) if flow == 'following' else cl.user_followers(user_id,amount= N)

def user_info_by_urs(username:str):
    time.sleep(rd.randint(0, 200))
    return cl.user_info_by_username(username)

def follow_and_comment(username,password,tag_list,comment,num_media,comment_fp=comment_log,follow = 'Y'):
    """Follow accounts with media in hashtags and write comment"""
    login(username, password)
    medias = get_hashtag_medias_top(tag_list,num_media) # get media list using the public domain
    for user in medias:
        # comment_on_media([user],  comment,comment_fp= comment_log)
        if follow == 'Y':
            un_follow_user(user.dict().get('user').get('pk'))
            print('Followed user: '+ user.dict().get('user').get('username'))
        logout()
