import time,sys
from python_helpers import python_helper as ph
sys.path.insert(0,ph.root_fp+'ig_content_publisher/publisher')
import instagram as ig, txt_to_img as tt,json

token = ig.get_token('le_bad_joker')
ig_ig = ig.get_ig_acc(token.get('id')).get('id')
ig.get_post_quota(ig_ig)

# caption ='@musk is now the 1st richest person in the world, with a total estimated networth at $275156.389.\nHis networth has decreased by $-3,B (👎-1.28%) 💘 \nUpdated @ 12/11/2021 14:51 GMT'
# post_img_to_ig(ig_ig,img_url,caption)



img=  tt.create_img(img_path='ig_content_publisher/imgs/2880x1800-air-force-dark-blue-solid-color-background.jpg')
tt.check_contrast(img,'white')
tt.choose_img(img,'white')
tt.save_upload_img(img, 'love','png' )
# /home/oolao/github/working_files
