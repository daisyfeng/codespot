<?php
function the_video_url($post_id) {
  $post = get_post($post_id);
  if(!empty($post)) {
    $content = $post->post_content;
    $r = "/<embed type=\"application\/x-shockwave-flash\" width=\"\d.*?\" height=\"\d.*?\" src=\"(\S.*?)\" \S.*?>/i";
    if(preg_match($r,$content,$match))
      print_r($match);
  }
  }
    