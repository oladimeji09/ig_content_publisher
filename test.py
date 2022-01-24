import instagram
token = get_token('uk_travel_redlist')
token = get_token('everyday_joker')
token = get_token('top_10_billionaires')
ig_ig = get_ig_acc(token.get('id')).get('id')
get_post_quota(ig_ig)

caption ='@musk is now the 1st richest person in the world, with a total estimated networth at $275156.389.\nHis networth has decreased by $-3,B (👎-1.28%) 💘 \nUpdated @ 12/11/2021 14:51 GMT'
post_img_to_ig(ig_ig,img_url,caption)


users = json.load(open(ph.root_fp+'/creds/creds.json')).get('ig_users')
username = users.get('top_10_billionaires').get('user_name')
password = users.get('top_10_billionaires').get('password')
delete_media(username,password,173)
follow_and_comment(username, password,['money'], 'hey baby', 3)
get_hashtag_medias_top(['money'])
login(username,password)

import txt_to_img as tt

img=  tt.create_img(img_path='IG-content-publisher/backgrounds/2880x1800-air-force-dark-blue-solid-color-background.jpg')
tt.check_contrast(img,'white')
tt.choose_img(img,'white')
tt.save_upload_img(img, 'love','png' )
